from src.models.basemodel import Property
from dataclasses import dataclass

@dataclass(frozen=False)
class Dubizzle(Property):
    posted_date: int
    detail_url: str
    image_url: str
    furnished: bool
    agent_id: int
    agent_name:str
    promoted: bool
    listing_id: str
    rent_is_paid_short: str
    rent_is_paid_name: str
