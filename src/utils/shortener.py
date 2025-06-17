from string import ascii_letters, digits

from random import choices

from src.core.config import settings


async def short_link_id_generator() -> str:
    full_symbols_string = ascii_letters + digits
    
    short_link = "".join(choices(full_symbols_string, k=10))
    
    return short_link


async def short_link_generator(url_id: str) -> str:
    return f"https://{settings.server_config.domain}/{url_id}"

