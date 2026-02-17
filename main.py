from fastapi import FastAPI
from routers import user_router, product_router
from core.exception import register_exception_handlers

app = FastAPI(title="FastAPI CRUD API")

API_V1_PREFIX = "/api/v1"
API_PREFIX = "/api"

register_exception_handlers(app)


app.include_router(
    user_router.router,
    prefix=API_PREFIX,
    tags=["Users"]
)

app.include_router(
    product_router.router,
    prefix=API_PREFIX,
    tags=["Products"]
)
