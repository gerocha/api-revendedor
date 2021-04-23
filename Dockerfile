FROM python:3.9.2-buster
RUN mkdir /code
WORKDIR /code
COPY . /code
RUN python -m pip install pipenv
RUN pipenv install
RUN pipenv install mysqlclient
RUN pipenv install -e .
EXPOSE 5000
CMD ["pipenv", "run", "python", "api/app.py"]
