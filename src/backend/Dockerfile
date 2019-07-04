FROM python:3.6-alpine

WORKDIR /var

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY *.py ./

EXPOSE 5000

CMD python /var/backend.py