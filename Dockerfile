FROM python:3

WORKDIR /home/arie/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENV CITY="Rome"

EXPOSE 5000

CMD [ "python", "app.py"]