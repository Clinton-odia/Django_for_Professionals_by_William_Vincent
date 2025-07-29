FROM python:3.12

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Set work directory
WORKDIR /cho1_docker
# Install dependencies
COPY Pipfile Pipfile.lock /cho1_docker/
RUN pip install pipenv && pipenv install --system
# Copy project
COPY . /cho1_docker/

