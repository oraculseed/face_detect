FROM python:3.8-slim

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD [ "uvicorn tst:app --reload --port 8089 --host 0.0.0.0" ]
