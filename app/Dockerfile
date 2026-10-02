# ──────────────────────────────────────────────────────────────
# Dockerfile for Self-Healing DevOps Platform - Flask App
# Phase 1
#
# A Dockerfile is a recipe that tells Docker how to build
# a container image for your application.
# Each line is an "instruction" that adds a layer to the image.
# ──────────────────────────────────────────────────────────────


# ── STAGE 1: Base Image ────────────────────────────────────────
# FROM tells Docker which base image to start from.
# python:3.11-slim is a lightweight official Python image.
# "slim" means it has only the minimum needed — keeps image small.
FROM python:3.11-slim


# ── STAGE 2: Set Working Directory ────────────────────────────
# WORKDIR sets the folder inside the container where all
# subsequent commands will run. Think of it as "cd /app".
WORKDIR /app


# ── STAGE 3: Install Dependencies ─────────────────────────────
# COPY the requirements file first (before copying the rest
# of the code). This is a Docker best practice — if your
# code changes but requirements don't, Docker reuses the
# cached layer and skips re-installing packages. Saves time.
COPY requirements.txt .

# RUN executes a shell command during the image build.
# We install Python packages from requirements.txt.
# --no-cache-dir keeps the image smaller by not storing pip's cache.
RUN pip install --no-cache-dir -r requirements.txt


# ── STAGE 4: Copy Application Code ────────────────────────────
# Now copy everything else into the container.
# The first "." means "everything in the current host directory"
# The second "." means "into the WORKDIR (/app) in the container"
COPY . .


# ── STAGE 5: Expose Port ───────────────────────────────────────
# EXPOSE tells Docker that the container will listen on port 5000.
# This is documentation — it doesn't actually open the port.
# The port is opened when you run the container with -p 5000:5000.
EXPOSE 5000


# ── STAGE 6: Health Check ──────────────────────────────────────
# HEALTHCHECK tells Docker how to test if the container is healthy.
# Docker will run this command every 30 seconds.
# --interval=30s  → check every 30 seconds
# --timeout=10s   → if no response in 10 seconds, mark as unhealthy
# --start-period=5s → wait 5 seconds after startup before first check
# --retries=3     → fail 3 times in a row before marking as unhealthy
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:5000/health')" \
    || exit 1


# ── STAGE 7: Run the Application ──────────────────────────────
# CMD specifies the command to run when the container starts.
# We run app.py with Python.
# Using the list form ["python", "app.py"] is best practice —
# it runs the command directly without a shell wrapper.
CMD ["python", "app.py"]
