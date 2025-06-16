from fastapi import APIRouter

from src.schemas.url_schema import FullLinkSchema, ShortLinkSchema

from src.services.shortener import short_link_generator


router = APIRouter(
    prefix="/url_shortener"
)


@router.post("/")
async def shorter(link: FullLinkSchema):
    return await short_link_generator()


@router.get("/{short_id}")
async def view(short_id: str):
    ...