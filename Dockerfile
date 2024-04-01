FROM python:3.11.4-slim-buster

WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

COPY ./requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

#ENV HOME=/code
#ENV APP_HOME=/code/web
#RUN mkdir $APP_HOME
#RUN mkdir $APP_HOME/staticfiles
#WORKDIR $APP_HOME

EXPOSE 8000
RUN chmod +x /code/start.sh
ENTRYPOINT ["./start.sh"]
