FROM python:3
ENV PYTHONUNBUFFERED=1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt

RUN pip install -r requirements.txt

# RUN apt-get update

# RUN apt-get upgrade -y

# RUN apt-get install redis-server -y

# CMD ['redis-server']

# CMD ['celery -A fampay beat -l info']

EXPOSE 8000

COPY . /code/
# Run the specified command within the container.
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000"]
