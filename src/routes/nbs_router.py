from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from src.infra.middleware.deps import CurrentUser
from src.infra.databases.oracle_nbs import SessionOra
from src.data.schemas.nbs_schemas import (
    VehicleRequest, 
    VehicleSoldResponse, 
    VehicleDeliveredResponse, 
    ScheduledReviewResponse, 
    ScheduledReviewRequest)
from src.controller import nbs_controller

nbs_router = APIRouter()

@nbs_router.post("/vehicle_sold", response_model=VehicleSoldResponse, tags=["NBS"])
async def vehicle_sold(current_user: CurrentUser, session: SessionOra, vehicle: VehicleRequest):
    """
    Route to check if the customer's vehicle has been sold. 
    """    
    # verify_admin = current_user.is_admin

    # if not verify_admin: # type: ignore
    #     raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized user")

    db_vehicle_sold = nbs_controller.get_nbs_vehicle_sold(db=session, vin=vehicle.vin, cod_client=vehicle.cod_client) # type: ignore
    if not db_vehicle_sold:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return db_vehicle_sold

@nbs_router.post("/vehicle_delivered", response_model=VehicleDeliveredResponse, tags=["NBS"])
async def vehicle_delivered(current_user: CurrentUser, session: SessionOra, vehicle: VehicleRequest):
    """
    Route to check if the customer's vehicle has been delivered. 
    """    
    # verify_admin = current_user.is_admin

    # if not verify_admin: # type: ignore
    #     raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized user")

    db_vehicle_delivered = nbs_controller.get_nbs_vehicle_delivered(db=session, vin=vehicle.vin, cod_client=vehicle.cod_client) # type: ignore
    if not db_vehicle_delivered:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return db_vehicle_delivered


@nbs_router.post("/scheduled_review", response_model=ScheduledReviewResponse, tags=["NBS"])
async def scheduled_review(current_user: CurrentUser, session: SessionOra, vehicle: ScheduledReviewRequest):
    """
    Route to check if the vehicle has been scheduled review
    """ 
    db_scheduled_review = nbs_controller.get_nbs_scheduled_review(db=session, vin=vehicle.vin)
    if not db_scheduled_review:
        return { "revisao_agendada": False }
    else: 
        return { "revisao_agendada": True }

