FROM python:3.7-alpine
ADD monitoring_container.py /
RUN pip install requests
CMD ["python", "monitoring_container.py"]