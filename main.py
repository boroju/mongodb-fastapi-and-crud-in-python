from fastapi import FastAPI
from routes.user import user
from docs import tags_metadata

app = FastAPI(
  title="FastAPI & Mongo CRUD",
  description="A simple RestAPI using FastAPI and MongoDB",
  version="0.0.1",
  openapi_tags=tags_metadata
)

app.include_router(user)

