from string import ascii_letters, digits

from random import choices


async def short_link_generator() -> str:
    full_symbols_string = ascii_letters + digits
    
    short_link = "".join(choices(full_symbols_string, k=6))
    
    return short_link