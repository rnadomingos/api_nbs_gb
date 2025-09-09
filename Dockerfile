FROM python:3.12.1

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app

CMD [ "uvicorn", "src.server:app", "--host", "0.0.0.0", "--port", "8000" ]