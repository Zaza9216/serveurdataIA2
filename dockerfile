FROM python:3.3

WORKDIR /DataAPI

COPY . /DataAPI

RUN pip install --no-cache-dir requirements.txt

EXPOSE 80

ENV NAME World

CMD ["python", "app.py"]
