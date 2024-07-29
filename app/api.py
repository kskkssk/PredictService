from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.home.get import home_route
from routes.user.post import user_post_route
from routes.user.delete import (user_delete_route)
from routes.user.get import user_get_route
from routes.balance.get import balance_get_route
from routes.balance.post import balance_post_route
from database.database import init_db
import uvicorn

app = FastAPI()

app.include_router(home_route)
app.include_router(user_post_route, prefix='/users') #префикс чтобы не было коллизий
app.include_router(user_get_route, prefix='/users') #префикс чтобы не было коллизий
app.include_router(user_delete_route, prefix='/users') #префикс чтобы не было коллизий
app.include_router(balance_get_route, prefix='/balances')
app.include_router(balance_post_route, prefix='/balances')
app.on_event('startup')

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


def startup():
    init_db()


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8083)
