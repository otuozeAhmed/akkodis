# Base image
FROM python:3.9-slim-buster AS base

# Install necessary packages
RUN apt-get update && apt-get install -y \
    procps \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


# Builder stage
FROM base AS builder

# Install packages necessary to capture parent OS executable and processes
RUN apt-get update && apt-get install -y \
    procps \
    lsof \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy the code to the container
COPY . /app

# Set the working directory
WORKDIR /app

# Final stage
FROM base AS final

# Copy the Python dependencies
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages

# Copy the code
COPY . /app

# Set the working directory
WORKDIR /app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
