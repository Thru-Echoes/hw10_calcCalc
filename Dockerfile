FROM python:3.5-alpine

MAINTAINER Oliver Muellerklein "omuellerklein@berkeley.edu"

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["app.py"]
