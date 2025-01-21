FROM python:3.3

WORKDIR /DataAPI

COPY . /DataAPI

RUN pip install --no-cache-dir --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org -r requirements.txt

EXPOSE 80

ENV NAME World

CMD ["python3", "app.py"]
