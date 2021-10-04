FROM python:3.8-slim
ADD requirements.txt /src/requirements.txt
ADD run.sh /src/run.sh
RUN chmod +x /src/run.sh
RUN pip install --upgrade -r /src/requirements.txt
ADD app.py /src/app.py
CMD ["/src/run.sh"]
