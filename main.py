from fastapi import FastAPI

from api import db_api, auth_api
from common import models
from common.session import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(db_api.router)
app.include_router(auth_api.router)
