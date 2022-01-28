FROM python:alpine

RUN python3 -m pip install pymongo

COPY . .

EXPOSE 4080

CMD [ "python3", "seed_mongodb.py" ]