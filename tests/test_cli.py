"""Unit tests for the CLI commands."""

from click.testing import CliRunner
from my_project.cli import cli
from my_project import __version__


def test_cli_version():
    runner = CliRunner()
    result = runner.invoke(cli, ["version"])
    assert result.exit_code == 0
    assert f"my-project version {__version__}" in result.output


def test_cli_items_list():
    runner = CliRunner()
    result = runner.invoke(cli, ["items", "list"])
    assert result.exit_code == 0
    assert "Found" in result.output


def test_cli_items_add():
    runner = CliRunner()
    result = runner.invoke(cli, ["items", "add", "CLI Test Item", "-d", "Added via test"])
    assert result.exit_code == 0
    assert "Created item #" in result.output
    assert "CLI Test Item" in result.output
