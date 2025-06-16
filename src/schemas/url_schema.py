from pydantic import BaseModel, AnyUrl


class FullLinkSchema(BaseModel):
    full_url: AnyUrl
    
    
class ShortLinkSchema(BaseModel):
    short_url: AnyUrl