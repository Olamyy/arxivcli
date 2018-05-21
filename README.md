# arxivcli

A cli package for accessing and quering arxiv papers.


# Installation

If you don't use `pipenv`, you're missing out.
Here are [installation instructions](https://github.com/pypa/pipenv/tree/master/pipenv).

To install from `pypa`:
       
    $ pipenv install arxivcli


To build from source, clone the repo and run:

    $ pipenv --three
    $ pipenv install
    $ pip setup.py install


# Usage

To use it:

    $ arxivcli --help

```
Usage: arxivcli [OPTIONS] ACTION

  A cli package for accessing and quering arxiv papers.

Options:
  --v                        Verbose
  -o, --output TEXT          Tabulate query result.
  -q, --search-query TEXT    Search Query : Text query to search
  -id, --ids TEXT            ID(s) of paper(s) to return
  -st, --start INTEGER       What paper number should query return?
  -mr, --max-result INTEGER  Maximum Result of papers to return
  -sb, --sort-by TEXT        Result sorting condition. Should be one of
                             'relevance', 'lastUpdatedDate', 'submittedDate'
  -so, --sort-order TEXT     Result sorting order. Should be one of
                             'ascending'' or 'descending'
  --help                     Show this message and exit.
⏎                                                               
```