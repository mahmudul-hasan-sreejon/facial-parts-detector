FROM python:2.7.15
LABEL Sreejon="sreejon_doom@yahoo.com"

# Bundle source files
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app

# Install python app dependencies
RUN pip install -r requirements.txt

COPY . /app

# Expose port
ENTRYPOINT ["python"]
CMD ["app.py", "-p 8080"]