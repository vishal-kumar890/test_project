import os
from pathlib import Path
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from typing import Optional
from pydantic import BaseSettings

class Settings(BaseSettings):
    api_key : Optional[str] = None
    
    class Config:
        env_file = ".env"


settings = Settings()

current_dir = os.path.dirname(__file__)
dir_name = os.path.split(current_dir)[1]
print("dir_name",dir_name,os.getcwd())
templates = Jinja2Templates(directory=f"./{dir_name}/templates")
page_assets = StaticFiles(directory=f"./{dir_name}/page_assets")

