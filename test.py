import pytest
from click.testing import CliRunner
from arxivcli import cli


@pytest.fixture
def runner():
    return CliRunner()

