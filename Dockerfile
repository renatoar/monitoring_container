FROM python:3
WORKDIR /usr/src/app
COPY requirements.txt ./
COPY monitoring_container.py ./
RUN pip install --no-cache-dir -r requirements.txt
CMD python ./monitoring_container.py