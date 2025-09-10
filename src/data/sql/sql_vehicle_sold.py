from sqlalchemy import text

stmt_vehicle_sold = text(
  """
  SELECT nvl(frota.vendido,'N') as produto_vendido_cliente, frota.* FROM
         ( SELECT cfx.cod_cliente,
                  cfx.chassi,
                  cfx.vendido,
                  ROW_NUMBER() OVER (PARTITION BY cfx.chassi,cfx.cod_cliente ORDER BY cfx.data_compra) as rn
             FROM clientes_frota cfx ) frota
  WHERE frota.chassi = :vin
    and   frota.cod_cliente = :cod_client
    and   frota.rn = 1
"""
)
