from pydantic import BaseModel


# Input schema (user sends to API)
class ProductData(BaseModel):
    price: float
    avg_price: float
    price_std: float
    total_purchases: int
    total_events: int
    user_activity: int
    user_purchases: int
    conversion_rate: float
    price_deviation: float
    event_type_purchase: int
    event_type_view: int


# Output schema (API returns)
class PredictionOutput(BaseModel):
    purchase_probability: float
    predicted_price: float
    suggested_price: float