from datetime import date
from typing import List
from pydantic import BaseModel


class VehicleRequest(BaseModel):
    vin: str
    cod_client: int

    class Config:
           from_attributes = True
           
class VehicleSoldResponse(BaseModel):
    vendido: bool

    class Config:
           from_attributes = True

class VehicleDeliveredResponse(BaseModel):
    entregue: date
    
    class Config:
           from_attributes = True