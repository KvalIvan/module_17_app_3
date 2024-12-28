from module_17_1.app.models.task import Task
from module_17_1.app.models.user import User
from module_17_1.app.schemas import CreateTask, UpdateTask


from fastapi import APIRouter

router = APIRouter(prefix='/task', tags=['task'])


@router.get('/')
async def all_tasks():
    pass


@router.get('/task_id')
async def task_by_id():
    pass


@router.post('/create')
async def create_task():
    pass


@router.put('/update')
async def update_task():
    pass


@router.delete('/delete')
async def delete_task():
    pass

