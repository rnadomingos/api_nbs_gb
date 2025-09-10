from sqlalchemy import text

stmt_vehicle_delivered = text(
  """
  SELECT TRUNC(
           NVL(
               NVL(eva.data_baixa, eva.data_agendada),
               v.data_venda
           )
       ) AS data_entrega
  FROM nbs.ev_agendados eva
       JOIN nbs.veiculos v
         ON v.cod_cliente = eva.cod_cliente
        AND v.chassi_resumido = eva.chassi_resumido
  WHERE v.status = 'V'
    AND eva.status IN ('E', 'A', 'N')
    AND eva.cod_cliente = :cod_client  -- CÓDIGO DO CLIENTE (CPF ou CNPJ numérico)
    AND v.chassi_completo = :vin -- CHASSI COMPLETO DO VEÍCULO
    AND ROWNUM = 1
  ORDER BY TRUNC(
                NVL(
                    NVL(eva.data_baixa, eva.data_agendada),
                    v.data_venda
                )
            ) DESC
  """
)
