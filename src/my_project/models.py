"""Data models and schemas."""

from typing import Optional
from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    """Health check response schema."""
    status: str = Field(default="ok", description="Application health status")
    version: str = Field(..., description="Application version")


class ItemCreate(BaseModel):
    """Schema for creating a new item."""
    title: str = Field(..., min_length=1, max_length=100, description="Title of the item")
    description: Optional[str] = Field(None, max_length=500, description="Optional description")
    completed: bool = Field(default=False, description="Whether the item is completed")


class Item(ItemCreate):
    """Complete Item schema including system generated ID."""
    id: int = Field(..., description="Unique identifier for the item")
