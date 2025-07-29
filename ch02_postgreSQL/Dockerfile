FROM python:3.12

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /code

# Install dependencies
COPY Pipfile Pipfile.lock /code/

# Install pipenv and use it to install dependencies into the system environment
RUN pip install pipenv && pipenv install --system --deploy --ignore-pipfile

# Copy the rest of the project
COPY . /code/
