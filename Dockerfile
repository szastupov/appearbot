FROM python

ADD requirements.txt /bot/
ADD bot.py /bot/
ADD config.json /bot/
WORKDIR /bot

RUN pip install -r ./requirements.txt

CMD ["python", "./bot.py"]
