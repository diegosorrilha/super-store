FROM python:3.7.4-slim-stretch

RUN apt-get update && apt-get install -y gcc python-dev git openssh-client default-libmysqlclient-dev

RUN mkdir /api

WORKDIR /api

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /api

CMD ["python", "app.py"]
