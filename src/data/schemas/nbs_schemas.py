from datetime import date
from typing import Optional
from pydantic import BaseModel, ConfigDict


class VehicleRequest(BaseModel):
    vin: str
    cod_client: int
    
    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra = {
            "examples": [
                {
                    "vin": "SAL1ABAG6EA707050",
                    "cod_client": "12345678909"
                }
            ]
        }
    )
           
class VehicleSoldResponse(BaseModel):
    vendido: Optional[str] = None

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra = {
            "examples": [
                {
                    "vendido": "S",
                }
            ]
        }
    )

class VehicleDeliveredResponse(BaseModel):
    data_entrega: Optional[date] = None
    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "examples": [
                {
                    "data_entrega": "YYYY-MM-DD",
                }
            ]
        }
    )


class ScheduledReviewRequest(BaseModel):
    vin: str
    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "examples": [
                {
                    "vin": "SAL1ABAG6EA707050",
                }
            ]
        }
    )    

class ScheduledReviewResponse(BaseModel):
    revisao_agendada: Optional[bool] = None
    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "examples": [
                {
                    "revisao_agendada": "S",
                }
            ]
        }
    )        

class VehicleSoldBySaleDateRequest(BaseModel):
    sale_date_ini: str
    sale_date_end: str
    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "examples": [
                {
                    "sale_date_ini": "01012025",
                    "sale_date_end": "19122025"
                }
            ]
        }
    )        