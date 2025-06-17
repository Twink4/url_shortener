from sqlalchemy import select

from src.core.database import get_async_session, DependsSession
from src.models.url_models import UrlModel


class UrlService:
    model = UrlModel


    @classmethod
    async def add_link_to_database(cls, url_id: str, short_url: str, full_url:str,  session: DependsSession):
        new_url = cls.model(id=url_id, short_link=short_url, full_link=full_url)
        session.add(new_url)
        await session.commit()
        await session.refresh(new_url)  # если нужно получить id или другие поля
        return new_url
        
    
    @classmethod
    async def get_link_from_id(cls, id: str, session: DependsSession):
        query = select(cls.model).filter_by(id=id) # type: ignore
        result = await session.execute(query)
        return result.mappings().one_or_none()