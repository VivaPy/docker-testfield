FROM python:3.10-slim

WORKDIR /pyapp

RUN pip install -r requirements.txt

COPY ./requirements.txt .


COPY . .

EXPOSE 8000

CMD ["python", "server.py"]