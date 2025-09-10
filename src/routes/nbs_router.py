from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from src.infra.middleware.deps import CurrentUser
from src.infra.databases.oracle_nbs import SessionOra
from src.data.schemas.nbs_schemas import VehicleRequest
from src.controller import nbs_controller

nbs_router = APIRouter()

@nbs_router.post("/vehicle_sold", tags=["NBS"])
async def vehicle_sold(current_user: CurrentUser, session: SessionOra, vehicle: VehicleRequest):
    """
    Route to create users. To create, the user must be admin. 
    """    
    verify_admin = current_user.is_admin

    if not verify_admin: # type: ignore
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized user")

    db_vehicle_sold = nbs_controller.get_nbs_vehicle_sold(db=session, vin=vehicle.vin, cod_client=vehicle.cod_client) # type: ignore
    if not db_vehicle_sold:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return db_vehicle_sold
