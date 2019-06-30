FROM python:3.7-alpine
ADD monitoring_container.py /
RUN pip install requests
RUN pip install pymongo
CMD ["python", "monitoring_container.py"]