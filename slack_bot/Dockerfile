FROM python:3.11-slim-bullseye

RUN cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime
RUN pip install \
    slack-bolt \
    boto3

RUN mkdir /app
WORKDIR /app
COPY bot bot

CMD python -m bot.slack_bot
