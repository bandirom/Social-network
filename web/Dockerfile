# pull official base image
FROM python:3.8.2-alpine

# set work directory
WORKDIR /usr/src/web

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV TZ Europe/Kyiv
ENV DEBUG 1
ENV SECRET_KEY  '22+sg%5+##a=^-$o58(1q9(^r@cjl-p0r3m^x9@-#i=1qcs2y2'
ENV DJANGO_ALLOWED_HOSTS localhost 127.0.0.1 [::1]

# install dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev openssl libffi-dev openssl-dev

# install Pillow dependencies
RUN apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev harfbuzz-dev fribidi-dev


# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/web/requirements.txt
RUN pip install -r requirements.txt

# EXPOSE 8000
# copy project
COPY . /usr/src/web/

# CMD python manage.py runserver 0.0.0.0:8000
# CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000"]
