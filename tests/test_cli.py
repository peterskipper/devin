import pytest
from click.testing import CliRunner
from devin import cli


@pytest.fixture
def runner():
    return CliRunner()


def test_devin(runner):
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert not result.exception


def test_more_devin(runner):
    result = runner.invoke(cli.main, ['--more-devin'])
    assert result.exit_code == 0
    assert not result.exception
    assert result.output.strip()[-24:] == " It's a good good album."
