FROM python:3.7
RUN pip3 install fastapi uvicorn pandas
CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000" ]
