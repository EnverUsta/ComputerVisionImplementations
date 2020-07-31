FROM python:3.7

MAINTAINER Enver Usta <enver.usta@outlook.com>

WORKDIR /usr/src/app

COPY images .
COPY feature-matching.py .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "./feature-matching.py"]


