# from ..core import security as sc
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.responses import RedirectResponse
from fastapi import Request, Depends, HTTPException, status, Form, APIRouter
from ..config import templates



router = APIRouter()

@router.get('/')
async def series_setup(request: Request): 
        return templates.TemplateResponse("user-management.html", {"request": request,
                                                                    "title": "Series Setup"})


@router.post('/sum')
async def get_sum(data:dict ,request: Request):
        num1 = float(data['first_num']) 
        num2 = float(data['second_num']) 
        return num1+num2


@router.post('/multiply')
async def get_multiplication(data:dict ,request: Request): 
        num1 = float(data['first_num']) 
        num2 = float(data['second_num']) 
        return num1*num2

@router.post('/subtract')
async def get_subtraction(data:dict ,request: Request): 
        num1 = float(data['first_num']) 
        num2 = float(data['second_num']) 
        return num1-num2       
