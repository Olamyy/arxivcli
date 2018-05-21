import click
from arxivcli.arxiv import Arxiv
import tableprint
import pprint


@click.command()
@click.option('--as-cowboy', '-c', is_flag=True, help='Greet as a cowboy.')
@click.argument('name', default='world', required=True)
@click.argument('search_query', default='world', required=False)
def mained(name, as_cowboy):
    """A cli package for accessing and quering arxiv papers."""
    greet = 'Howdy' if as_cowboy else 'Hello'
    click.echo('{0}, {1}.'.format(greet, name))


@click.command()
@click.option('--v', is_flag=True, help="Verbose")
@click.option('--output', '-o', default='tabulate', help="Tabulate query result.")
@click.argument('action', default='query', required=True, type=str)
@click.option('--search-query', '-q', default="", help="Search Query : Text query to search", required=False, type=str)
@click.option('--ids', '-id', required=False, help="ID(s) of paper(s) to return", default=None)
@click.option('--start', '-st', is_flag=False, help="What paper number should query return?", default=0)
@click.option('--max-result', '-mr', is_flag=False, help="Maximum Result of papers to return", default=10)
@click.option('--sort-by', '-sb', is_flag=False, help="Result sorting condition. Should be one of 'relevance', 'lastUpdatedDate', 'submittedDate'", default="relevance")
@click.option('--sort-order', '-so', is_flag=False, help="Result sorting order. Should be one of 'ascending'' or 'descending'", default="descending")
def main(action, search_query, ids, start, max_result, sort_by, sort_order, v, output):
    """A cli package for accessing and quering arxiv papers."""
    if v: click.echo("Building query parameters \n")
    kwargs = {"start": start, "max_result": max_result,
              "sort_by": sort_by, "sort_order": sort_order, "search_query": search_query, "ids": ids}
    print(kwargs)
    if v: click.echo("Parameters built \n")
    if action == "query":
        arxiv = Arxiv(**kwargs)
        text = """The provided query parameters are {0}  .\nThe request url is {1} \n""".format(arxiv.query_url_args, arxiv.request_url)
        if v: click.echo(text)
        query_result = arxiv.query()
        if v: click.echo("Query Complete  \n{} result \n".format("Printing raw as list" if output == "list" else "Printing raw as json" if output == "json" else "Tabulating"))
        if output == "list":
            print(query_result)
        elif output == "json":
            import json
            output = json.dumps(query_result)
            print(output)
        else:
            click.echo("Tabulating is currently not supported. It should be by tomorrow. Rolling back to pprint")
            pprint.pprint(query_result)

    if action == "download":
        arxiv = Arxiv(**kwargs)
        text = """The provided query parameters are {0}  .\nThe request url is {1} \n""".format(arxiv.query_url_args, arxiv.request_url)
        if v: click.echo(text)
        arxiv_query = arxiv.query()[0]
        if v: click.echo("Query Complete\n")
        if v: click.echo("Downloading Paper\n")
        arxiv.download(arxiv_query)
        tableprint.banner("Successfully Downloaded Paper : {0}".format(arxiv_query['title']))

    if action == "get_paper":
        arxiv = Arxiv(**kwargs)
        arxiv_query = arxiv.query()[0]
        pprint.pprint(arxiv_query)