FROM python:3.7.2-slim

COPY . eveno
WORKDIR /eveno

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python test_users.py


ENTRYPOINT ["python", "run.py"]