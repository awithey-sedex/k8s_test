FROM python:3.6-alpine

WORKDIR /var
ENV APIENDPOINTURL=http://is-prime-service:5000
ENV PORT=5000

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY *.py ./

EXPOSE 5000

CMD python /var/api_rest.py