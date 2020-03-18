from dataclasses import dataclass

@dataclass(frozen=False)
class Property:
    #prop_type: str
    source: str
    listing_type: str
    listing_name: str
    building: str
    lat: float
    lng: float
    city_id: int
    city: str
    country: str
    developer: str
    num_bedrooms: int
    num_bathrooms: int
    area_sqft: float
    price: int
    price_currency: str
    categories_ids: list
    categories_tags: list
    categories_names: list
    neighborhoods_ids: list
    neighborhoods_names: list
