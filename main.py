from fastapi import FastAPI, Request, status
from .views import userApi
from .config import page_assets
from apilytics.fastapi import ApilyticsMiddleware
# from .wfScheduler import sch

import os, sqlite3

app = FastAPI()
# app.scheduler = sch
app.add_middleware(ApilyticsMiddleware, api_key=os.getenv("792fcbc9-89e6-448b-acbb-440721f66816"))

app.mount("/page_assets", page_assets, name="page_assets")

app.include_router(userApi.router, tags=["users"])


