# Use an official Python runtime as the base image
FROM python:3.11.4-slim

# Set the working directory in the container
WORKDIR /code

# Copy only the dependency files to the working directory
COPY pyproject.toml poetry.lock /code/

# Install Poetry
RUN pip install poetry

# Install project dependencies
RUN poetry config virtualenvs.create false && poetry install --no-dev --no-interaction --no-ansi

# Copy the project code to the working directory
COPY . /code/

# Expose the port that the Django app will run on
EXPOSE 8000

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE=pypro.settings

# Run the Django development server
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
