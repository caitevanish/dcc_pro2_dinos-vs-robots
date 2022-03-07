#Specify a base image
FROM python:3.11-rc-slim-buster

#Environment: keep python from generating .pyc files
ENV PYTHONDONTWRITEBYTECODE=1 
#turn off buffering for easier container logging
ENV PYTHONBUFFERED=1

# Dependencies: set up empty requirements .txt so pip intall works
COPY requirements.txt ./

#Dependency install using pip install command
RUN pip install -r requirements.txt

#Set up the working directory
WORKDIR /usr/app

#Non-root user
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app

USER appuser

#Starting command: Python and the initial .py file 
CMD ["python, "./main.py"]

#Build an image








