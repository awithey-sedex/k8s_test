FROM python:3.6-alpine

WORKDIR /var
ENV BACKENDURL=http://is-prime-backend:5000
ENV PORT=5000
ENV REQUESTTIMEOUT=2

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY *.py ./

EXPOSE 5000

CMD python /var/web.py