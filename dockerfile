FROM python:3.3

WORKDIR /serveurdataIA2

COPY . /serveurdataIA2/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

ENV NAME World

CMD ["python", "app.py"]