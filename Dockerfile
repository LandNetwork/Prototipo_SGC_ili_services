FROM python:3.12-slim

# Update repository OS and install necessary packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    curl \
    vim \
    default-jdk \
    && rm -rf /var/lib/apt/lists/*

# Fix certificate issues
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    ca-certificates-java \
    && rm -rf /var/lib/apt/lists/* && \
    update-ca-certificates -f;

# Settings env
ENV PYTHONUNBUFFERED 1

# Set the working directory inside the container
WORKDIR /app

# Copy the project files into the container
COPY . /app/

# Copy the requirements file and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir -r /app/ili_svc_app/submodules/requirements.txt

# Start the Django development server
#CMD ["/bin/sh", "-c", "python3 manage.py migrate && python3 create_super_user.py && python3 manage.py runserver 0.0.0.0:8000"]

# Start the Django production server with SSL
# CMD ["/bin/sh", "-c", "python3 manage.py collectstatic --no-input && python3 manage.py migrate && python3 create_super_user.py && gunicorn -w 2 -b 0.0.0.0:443 --certfile /certs/live/ceicol.com/fullchain.pem --keyfile /certs/live/ceicol.com/privkey.pem terrainfo_project.wsgi"]

# Start the Django production server
CMD ["sh", "-c", "python manage.py collectstatic --no-input && python manage.py migrate && gunicorn -w 2 -b 0.0.0.0:8000 ili_svc_project.wsgi"]
