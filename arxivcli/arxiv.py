
import feedparser
import sys

if sys.version_info <= (2, 7):
    from urllib import urlencode
    from urllib import urlretrieve
else:
    from urllib.parse import urlencode
    from urllib.request import urlretrieve


class Arxiv(object):
    def __init__(self, **kwargs):
        self.root_url = 'http://export.arxiv.org/api/'
        self.search_query = kwargs.get('search_query')
        self.ids = kwargs.get("ids")
        self.start = kwargs.get("start")
        self.max_result = kwargs.get("max_result")
        self.sort_by = kwargs.get("sort_by")
        self.sort_order = kwargs.get("sort_order")

        url_args = {"search_query": self.search_query,
                    "start": self.start,
                    "max_results": self.max_result,
                    "sortBy": self.sort_by,
                    "sortOrder": self.sort_order}
        if self.search_query:
            url_args["search_query"] = self.search_query
        if self.ids:
            url_args["id_list"] = self.ids

        self.query_url_args = urlencode(url_args)
        self.request_url = self.root_url + "query?" + self.query_url_args

    def query(self, prune=True):
        results = feedparser.parse(self.root_url + 'query?' + self.query_url_args)
        if results.get('status') != 200:
                # TODO: better error reporting
                print("HTTP Error " + str(results.get('status', 'no status')) + " in query")
                sys.exit()
        else:
            results = results['entries']
        for result in results:
            # Renamings and modifications
            self.modify_query_result(result)
            if prune:
                self.prune_query_result(result)
            return results

    def modify_query_result(self, result):
        result['pdf_url'] = None
        for link in result['links']:
            if 'title' in link and link['title'] == 'pdf':
                result['pdf_url'] = link['href']
        result['affiliation'] = result.pop('arxiv_affiliation', 'None')
        result['arxiv_url'] = result.pop('link')
        result['title'] = result['title'].rstrip('\n')
        result['summary'] = result['summary'].rstrip('\n')
        result['authors'] = [d['name'] for d in result['authors']]
        if 'arxiv_comment' in result:
            result['arxiv_comment'] = result['arxiv_comment'].rstrip('\n')
        else:
            result['arxiv_comment'] = None
        if 'arxiv_journal_ref' in result:
            result['journal_reference'] = result.pop('arxiv_journal_ref')
        else:
            result['journal_reference'] = None
        if 'arxiv_doi' in result:
            result['doi'] = result.pop('arxiv_doi')
        else:
            result['doi'] = None

    def prune_query_result(self, result):
        prune_keys = ['updated_parsed',
                      'published_parsed',
                      'arxiv_primary_category',
                      'summary_detail',
                      'author',
                      'author_detail',
                      'links',
                      'guidislink',
                      'title_detail',
                      'tags',
                      'id']
        for key in prune_keys:
            try:
                del result[key]
            except KeyError:
                pass

    def to_slug(self, title):
        # Remove special characters
        filename = ''.join(c if c.isalnum() else '_' for c in title)
        # delete duplicate underscores
        filename = '_'.join(list(filter(None, filename.split('_'))))
        return filename

    def download(self, obj, dirname='./', prepend_id=False, slugify=False):
        # Downloads file in obj (can be result or unique page) if it has a .pdf link
        if 'pdf_url' in obj and 'title' in obj and obj['pdf_url'] and obj['title']:
            filename = obj['title']
            if slugify:
                filename = self.to_slug(filename)
            if prepend_id:
                filename = obj['arxiv_url'].split('/')[-1] + '-' + filename
            filename = dirname + filename + '.pdf'
            # Download
            urlretrieve(obj['pdf_url'], filename)
            return filename
        else:
            print("Object obj has no PDF URL, or has no title")
            sys.exit()

    def plot_ngram(self, **kwargs):
        pass