FROM python:3.6

MAINTAINER Enver Usta <enver.usta@outlook.com>

#COPY images/book.png .
#COPY images/holding_book.jpeg .

COPY . .

COPY feature-matching.py .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "./feature-matching.py"]


