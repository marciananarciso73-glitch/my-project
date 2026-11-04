"""Command-line interface for my-project."""

import click
import uvicorn
from my_project import __version__
from my_project.models import ItemCreate
from my_project.service import item_service


@click.group()
def cli():
    """my-project CLI tool."""
    pass


@cli.command("version")
def version():
    """Display application version."""
    click.echo(f"my-project version {__version__}")


@cli.command("serve")
@click.option("--host", default="127.0.0.1", help="Host to bind the server to.", show_default=True)
@click.option("--port", default=8000, type=int, help="Port to bind the server to.", show_default=True)
@click.option("--reload", is_flag=True, default=False, help="Enable auto-reload for development.")
def serve(host: str, port: int, reload: bool):
    """Run the FastAPI web application server."""
    click.echo(f"Starting server on http://{host}:{port} ...")
    uvicorn.run("my_project.main:app", host=host, port=port, reload=reload)


@cli.group("items")
def items():
    """Manage items via CLI."""
    pass


@items.command("list")
def list_items():
    """List all current items."""
    all_items = item_service.list_items()
    if not all_items:
        click.echo("No items found.")
        return

    click.echo(f"Found {len(all_items)} item(s):")
    for item in all_items:
        status_char = "✓" if item.completed else " "
        click.echo(f"  [{status_char}] ID {item.id}: {item.title}")
        if item.description:
            click.echo(f"      Description: {item.description}")


@items.command("add")
@click.argument("title")
@click.option("--description", "-d", default=None, help="Optional description for the item.")
@click.option("--completed", "-c", is_flag=True, default=False, help="Mark item as completed.")
def add_item(title: str, description: str | None, completed: bool):
    """Add a new item."""
    created = item_service.create_item(ItemCreate(title=title, description=description, completed=completed))
    click.echo(f"Created item #{created.id}: {created.title}")


if __name__ == "__main__":
    cli()
