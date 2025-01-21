FROM python:3.13

WORKDIR /DataAPI

COPY . /DataAPI

RUN pip install --no-cache-dir requirements.txt

EXPOSE 80

CMD ["python", "app.py"]
