from fastapi import APIRouter

from .url_shortener import router as url_shortener_router

routers: list[APIRouter] = [
    url_shortener_router
]