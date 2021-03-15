FROM python:3.8

WORKDIR /code

COPY /. .

RUN pip install pipreqs

RUN pipreqs . --force

RUN pip install -r requirements.txt

CMD [ "python", "./server.py" ]