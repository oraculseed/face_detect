FROM python:3.7
WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .
ENTRYPOINT ./docker-starter.sh
EXPOSE 8089
