FROM python:3

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r ./public/requirements.txt

CMD ["python", "./public/app.py"]