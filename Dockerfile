FROM python:3.8-bullseye

ENV DEBIAN_FRONTEND noninteractive
RUN apt update && apt install libmariadb3 libmariadb-dev

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 4443
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=4443"]
