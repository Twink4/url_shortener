from fastapi import APIRouter, HTTPException, Response, status
from fastapi.responses import RedirectResponse

from src.core.database import DependsSession
from src.schemas.url_schema import FullLinkSchema, ShortLinkSchema
from src.utils.shortener import short_link_id_generator, short_link_generator
from src.services.url_shortener import UrlService


router = APIRouter(
    prefix="/url_shortener"
)


@router.post("/")
async def shorter(link: FullLinkSchema, session: DependsSession):
    short_url_id: str = await short_link_id_generator()
    full_url = str(link.full_url)
    short_url = await short_link_generator(short_url_id)

    response = await UrlService.add_link_to_database(short_url_id, short_url, full_url, session)
    if not response:
        raise HTTPException(500, detail="failed to create a record in the database")
    return Response(status_code=status.HTTP_201_CREATED)


@router.get("/{short_id}")
async def view(short_id: str, session: DependsSession):
    response = await UrlService.get_link_from_id(short_id, session)
    if not response:
        raise HTTPException(404, detail="short link not found")
    return RedirectResponse(response.UrlModel.full_link, status_code=307)
