FROM python:3.12.1

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

RUN apt-get update && apt-get install -y libaio1 unzip && rm -rf /var/lib/apt/lists/*


# Baixa e instala Oracle Instant Client
RUN curl -o /tmp/instantclient.zip https://download.oracle.com/otn_software/linux/instantclient/2390000/instantclient-basic-linux.x64-23.9.0.25.07.zip \
    && unzip /tmp/instantclient.zip -d /opt/oracle \
    && rm /tmp/instantclient.zip

ENV LD_LIBRARY_PATH=/opt/oracle/instantclient_23_9

COPY . /app

CMD [ "uvicorn", "src.server:app", "--host", "0.0.0.0", "--port", "8000" ]