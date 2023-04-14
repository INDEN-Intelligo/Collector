FROM python:3.9.1-alpine3.12

WORKDIR /usr/app/src
COPY ./ ./

RUN pip install -r requirements.txt

EXPOSE 5001

CMD ["python", "main.py"]
