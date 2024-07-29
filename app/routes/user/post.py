from fastapi import APIRouter, status, HTTPException, Depends, Form
from sqlalchemy.orm import Session
from services.crud.user_service import UserService
from services.crud.personal_service import PersonService
from services.crud.request_service import RequestService
from database.database import get_db
from schemas.user import UserCreate, UserResponse, UserSignin
from worker.tasks import handle_request as celery_handle_request
from fastapi.security import OAuth2PasswordRequestForm
from schemas.user import TokenResponse

user_post_route = APIRouter(tags=['User'])


def get_user_service(db: Session = Depends(get_db)) -> UserService:
    return UserService(db)


def get_person_service(user_service: UserService = Depends(get_user_service)) -> PersonService:
    current_user = user_service.get_current_user()
    return PersonService(user_service.session, current_user)


def get_request_service(db: Session = Depends(get_db)) -> RequestService:
    return RequestService(db)


@user_post_route.post("/signup", response_model=UserResponse)
async def signup(data: UserCreate, user_service: UserService = Depends(get_user_service)):
    if user_service.get_user_by_email(data.email) is not None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='User exists')
    user = user_service.create_user(username=data.username, password=data.password, first_name=data.first_name, last_name=data.last_name, email=data.email)
    return UserResponse.from_orm(user)


@user_post_route.post("/signin", response_model=TokenResponse)
async def signin(form_data: OAuth2PasswordRequestForm = Depends(), user_service: UserService = Depends(get_user_service)):
    try:
        token_data = user_service.login(email=form_data.username, password=form_data.password)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))
    return token_data


@user_post_route.post("/handle_request", response_model=dict)
async def handle_request(data: str, model: str, user_service: UserService = Depends(get_user_service)):
    try:
        current_user = user_service.get_current_user()
        task = celery_handle_request.apply_async(args=[data, model, current_user.username])
        return {"message": "Task sent to worker"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@user_post_route.post("/logout", response_model=dict)
async def logout(user_service: UserService = Depends(get_user_service)):
    try:
        user_service.logout()
        return {"message": "Вы успешно вышли из профиля"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))




