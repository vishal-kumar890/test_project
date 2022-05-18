from fastapi import FastAPI, Request, status
from .views import userApi
from .config import page_assets,settings
from apilytics.fastapi import ApilyticsMiddleware

import os, sqlite3

app = FastAPI()
# app.scheduler = sch
app.add_middleware(ApilyticsMiddleware, api_key=settings.api_key)

app.mount("/page_assets", page_assets, name="page_assets")

app.include_router(userApi.router, tags=["users"])


