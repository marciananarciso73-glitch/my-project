"""Business logic and in-memory store for items."""

from typing import Dict, List, Optional
from my_project.models import Item, ItemCreate


class ItemService:
    """Manages collection of items."""

    def __init__(self) -> None:
        self._items: Dict[int, Item] = {}
        self._counter: int = 1
        self._seed_default_items()

    def _seed_default_items(self) -> None:
        """Seed initial items for demo purposes."""
        self.create_item(ItemCreate(title="Welcome to my-project", description="Get started with your Python app", completed=True))
        self.create_item(ItemCreate(title="Explore API docs", description="Visit /docs for Swagger UI documentation", completed=False))

    def list_items(self) -> List[Item]:
        """Return all items."""
        return list(self._items.values())

    def get_item(self, item_id: int) -> Optional[Item]:
        """Get an item by ID."""
        return self._items.get(item_id)

    def create_item(self, item_in: ItemCreate) -> Item:
        """Create and store a new item."""
        new_id = self._counter
        self._counter += 1
        item = Item(
            id=new_id,
            title=item_in.title,
            description=item_in.description,
            completed=item_in.completed,
        )
        self._items[new_id] = item
        return item

    def delete_item(self, item_id: int) -> bool:
        """Delete an item by ID. Returns True if deleted, False if not found."""
        if item_id in self._items:
            del self._items[item_id]
            return True
        return False


# Global singleton instance for simple state handling
item_service = ItemService()
