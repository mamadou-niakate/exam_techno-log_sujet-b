FROM python:3.10-alpine

RUN pip install fastapi

RUN pip install pymongo

RUN pip install uvicorn

WORKDIR /exam_api

COPY . .

EXPOSE 4800

CMD ["uvicorn", "app_api:app", "--reload", "--host", "0.0.0.0", "--port", "4800"]