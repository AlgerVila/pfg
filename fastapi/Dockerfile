FROM arm64v8/python:3.7.10-buster

# WORKDIR /app
COPY . .

RUN pip install --trusted-host pypi.python.org -r requirements.txt

ENTRYPOINT ["python"]

CMD ["main.py"]