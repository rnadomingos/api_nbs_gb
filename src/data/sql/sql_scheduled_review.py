from sqlalchemy import text

stmt_scheduled_review = text(
  """
  SELECT 'S' as revisao_agendada FROM (
    SELECT 1 FROM OS_AGENDA AGENDA
      WHERE trunc(AGENDA.DATA_AGENDADA)>=trunc(SYSDATE)
      AND AGENDA.CHASSI = :vin
      AND rownum = '1'
    )
"""
)
