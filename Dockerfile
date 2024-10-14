FROM python:3.10-slim

WORKDIR /pyapp

COPY . .

COPY ./requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "server.py"]