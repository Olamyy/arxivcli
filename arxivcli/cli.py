import click
from arxivcli.arxiv import Arxiv
import tableprint


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
@click.argument('action', default='query', required=True, type=str)
@click.option('--search-query', '-sq', default="", help="Search Query : Text query to search", required=False, type=str)
@click.option('--id_list', '-id', required=False, help="ID(s) of paper(s) to return", default=None)
@click.option('--start', '-st', is_flag=False, help="What paper number should query return?", default=0)
@click.option('--max-results', '-mr', is_flag=False, help="Maximum Result of papers to return", default=10)
@click.option('--sort-by', '-sb', is_flag=False, help="Result sorting condition. Should be one of 'relevance', 'lastUpdatedDate', 'submittedDate'", default="relevance")
@click.option('--sort-order', '-so', is_flag=False, help="Result sorting order. Should be one of 'ascending'' or 'descending'", default="descending")
def main(action, v, sq, id, st, mr, sb, so):
    """A cli package for accessing and quering arxiv papers."""
    message = "Welcome To Arxiv CLI"
    kwargs = {"start": st, "max_result": mr, "sort_by": sb, "sort_order": so}
    if action == "query":
        arxiv = Arxiv(**kwargs)
        q = arxiv.query()
        print(q)
    if action == "download":
        arxiv = Arxiv(**kwargs)
        arxiv_query = arxiv.query()[0]
        arxiv.download(arxiv_query)
        tableprint.banner("Successfully Downloaded Paper : {0}".format(arxiv_query['title']))
