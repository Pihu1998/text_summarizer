# Base image for flask application
FROM python:3.10-alpine
# Work directory for Flask application
WORKDIR /Summarizer_langchain
# Copy the contents of flask app including requirements.txt
COPY . .

RUN apk add --no-cache --update \
    python3 python3-dev gcc \
    gfortran musl-dev

RUN pip install --upgrade pip
# Install requirements
RUN pip install -r requirements.txt
# Run app
CMD python app.py