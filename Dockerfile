FROM python:3.12-slim

WORKDIR /app 

COPY requirements.txt .

COPY analyse_turbines.py .

COPY telemetry_data(in).csv .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "analyse_turbines.py"]

