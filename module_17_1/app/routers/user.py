from module_17_1.app.models.task import Task
from module_17_1.app.models.user import User
from module_17_1.app.schemas import CreateTask, UpdateTask
# from module_17_1.app.backend.db import get_db

from fastapi import APIRouter

router = APIRouter(prefix='/user', tags=['user'])


@router.get('/')
async def all_users():
    pass


@router.get('/user_id')
async def user_by_id():
    pass


@router.post('/create')
async def create_user():
    pass


@router.put('/update')
async def update_user():
    pass


@router.delete('/delete')
async def delete_user():
    pass

