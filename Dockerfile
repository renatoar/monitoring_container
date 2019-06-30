FROM python:3.7-alpine
ADD monitoring_container.py /
CMD ["python", "monitoring_container.py"]