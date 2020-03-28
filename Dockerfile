FROM python:3.7.2-slim

COPY . eveno
WORKDIR /eveno

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
RUN python3 test_users.py


ENTRYPOINT ["python", "run.py"]