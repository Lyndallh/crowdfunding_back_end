ARG PYTHON_VERSION=3.11-slim-bullseye

FROM python:${PYTHON_VERSION}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /code

WORKDIR /code

COPY requirements.txt /tmp/requirements.txt
RUN set -ex && \
    pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    rm -rf /root/.cache/
COPY crowdfunding/ /code/

ENV SECRET_KEY "e8RklWyRNyknzZO3ebAfUEzey3ncSVfg6BrBL6zc82Ox5CsFBJ"
RUN python manage.py collectstatic --noinput
RUN chmod +x /code/run.sh

EXPOSE 8000

CMD ["/code/run.sh"]

