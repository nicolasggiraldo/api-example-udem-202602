from pydantic import BaseModel

class InputData(BaseModel):
    lot_size: int
    bedrooms: int