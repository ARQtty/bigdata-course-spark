FROM python:3.9

WORKDIR /app

ADD ./requirements.txt .
RUN pip3 install -r requirements.txt

ADD ./src/ ./src/
ADD ./data/subset.csv ./data/subset.csv
