"""FastAPI application entrypoint and routes."""

from typing import List
from fastapi import FastAPI, HTTPException, status
from my_project import __version__
from my_project.models import HealthResponse, Item, ItemCreate
from my_project.service import item_service

app = FastAPI(
    title="my-project API",
    description="A modern Python REST API built with FastAPI",
    version=__version__,
)


@app.get("/", tags=["General"])
def read_root():
    """Root endpoint welcoming visitors."""
    return {
        "message": "Welcome to my-project API",
        "version": __version__,
        "documentation": "/docs",
    }


@app.get("/health", response_model=HealthResponse, tags=["Monitoring"])
def check_health():
    """Health check endpoint for monitoring."""
    return HealthResponse(status="ok", version=__version__)


@app.get("/items", response_model=List[Item], tags=["Items"])
def get_items():
    """Retrieve all items."""
    return item_service.list_items()


@app.get("/items/{item_id}", response_model=Item, tags=["Items"])
def get_item(item_id: int):
    """Retrieve an item by ID."""
    item = item_service.get_item(item_id)
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with ID {item_id} not found",
        )
    return item


@app.post("/items", response_model=Item, status_code=status.HTTP_201_CREATED, tags=["Items"])
def create_item(item_in: ItemCreate):
    """Create a new item."""
    return item_service.create_item(item_in)


@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Items"])
def delete_item(item_id: int):
    """Delete an item by ID."""
    deleted = item_service.delete_item(item_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with ID {item_id} not found",
        )
    return None
