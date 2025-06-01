from fastapi import FastAPI
from .database import Base, engine
from .routers import lists, items
from fastapi.middleware.cors import CORSMiddleware
from fastapi_mcp import FastApiMCP

import logging
logging.basicConfig(level=logging.DEBUG)

Base.metadata.create_all(bind=engine)

app = FastAPI(title="TodoList + MCP (FastAPI)", debug=True)

app.include_router(lists.router)
app.include_router(items.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the TodoList API with MCP (FastAPI)!"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/hello")
def read_root():
    return {"message": "Hello from FastAPI"}

# Add MCP server to the FastAPI app
mcp = FastApiMCP(
    app,
    name="Item API MCP",
    description="MCP server for the Item API",
    describe_full_response_schema=True,
    describe_all_responses=True,
)

mcp.mount()

mcp.setup_server()