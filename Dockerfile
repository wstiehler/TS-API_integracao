FROM python:3.9.5

COPY . /var/www
WORKDIR /var/www

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

EXPOSE 8000

ENTRYPOINT python manage.py migrate && python manage.py runserver 0.0.0.0:8000
