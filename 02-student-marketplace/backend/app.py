"""
Student Marketplace — FastAPI backend.

Run with:
    uvicorn app:app --reload --port 5000
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from database import init_db
from models import ItemCreate, ItemOut, get_all_items, get_item_by_id, create_item

app = FastAPI(
    title="Student Marketplace API",
    description="Buy and sell second-hand items on campus.",
    version="0.1.0",
)

# Allow all origins so the Android / iOS emulators can reach the server.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup():
    init_db()


# ---------- Endpoints ----------


@app.get("/items", response_model=list[ItemOut])
def list_items():
    """Return all marketplace items, newest first."""
    return get_all_items()


@app.get("/items/{item_id}", response_model=ItemOut)
def item_detail(item_id: int):
    """Return a single item by its id."""
    item = get_item_by_id(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.post("/items", response_model=ItemOut, status_code=201)
def add_item(item: ItemCreate):
    """Create a new marketplace listing."""
    return create_item(item)
