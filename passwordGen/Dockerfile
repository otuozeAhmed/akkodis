# Use a lightweight Python image as the base image for the first stage
FROM python:3.10-slim AS base
WORKDIR /app
COPY . .


# Use an even smaller Python image as the base image for the second stage
FROM python:3.10-alpine AS final
WORKDIR /app

# Copy the script and dependencies from the previous stage
COPY --from=base /app .

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1


ENTRYPOINT ["tail", "-f", "/dev/null"]
