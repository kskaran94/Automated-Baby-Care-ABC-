FROM python:3.6

COPY . /app

RUN apt-get update
# RUN apt-get install -y mysql-server libmysqlclient-dev
RUN pip3 install --upgrade pip
RUN pip3 install -r /app/requirements.txt

CMD ["python", "/app/Project/ABC.py"]
