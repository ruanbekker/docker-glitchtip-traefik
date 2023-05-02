FROM python:3.8-slim
RUN apt update && apt install curl -y
WORKDIR /src
ADD requirements.txt /src/requirements.txt
ADD run.sh /src/run.sh
RUN chmod +x /src/run.sh
RUN pip install --upgrade -r /src/requirements.txt
WORKDIR /src
ADD app.py /src/app.py

CMD ["/src/run.sh"]
