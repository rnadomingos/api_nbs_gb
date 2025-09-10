from sqlalchemy.exc import ArgumentError, SQLAlchemyError
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError


from src.data.sql.sql_vehicle_sold import stmt_vehicle_sold
from src.data.sql.sql_vehicle_delivered import stmt_vehicle_delivered
#from src.infra.databases.oracle_nbs import engine

def get_nbs_vehicle_sold(db: Session, vin: str, cod_client: int):

    if not vin:
         raise ArgumentError("Must provide vehicle VIN.")
    
    if not cod_client:
         raise ArgumentError("Must provide client code.")

    try:
        result = db.execute(stmt_vehicle_sold, {"vin": vin, "cod_client": cod_client})
        rows = result.mappings().first()  # retorna lista de dicionários
        return rows       
        # with engine.connect() as conn, conn.begin():
        #     result = conn.execute(stmt_vehicle_sold, {"vin": vin, "cod_client": cod_client})
        #     rows = result.mappings().all()  # retorna lista de dicionários
        #     return rows       
    except SQLAlchemyError as e:
            print("Error loading data:")
            print(e.__class__.__name__, "-", e._message)
            raise


def get_nbs_vehicle_delivered(db: Session, vin: str, cod_client: int):

    if not vin:
         raise ArgumentError("Must provide vehicle VIN.")
    
    if not cod_client:
         raise ArgumentError("Must provide client code.")

    try:
        result = db.execute(stmt_vehicle_delivered, {"vin": vin, "cod_client": cod_client})
        rows = result.mappings().first()  # retorna lista de dicionários
        return rows       
       
    except SQLAlchemyError as e:
            print("Error loading data:")
            print(e.__class__.__name__, "-", e._message)
            raise