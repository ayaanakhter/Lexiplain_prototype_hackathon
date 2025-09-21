# 1. Start with an official Python base image
FROM python:3.11-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy the file that lists the dependencies
COPY requirements.txt .

# 4. Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy your application's code and model files into the container
COPY . .

# 6. Tell Docker that the container listens on port 5000
EXPOSE 5000

# 7. Define the command to run your application
CMD ["python", "app.py"]