# Areogrid-Engineering-Project
This repo detects failing wind turbine using anomaly detection from telemetry data

## Problem

Aerogrid manages wind turbines with sensors,their servers struggle to keep up with the volume allowing for warning signs to be missed

## What this repo contains

- 'analyse_turbines.py' which reads telemetry data and flags turbines exceeding safety thresholds

- 'Dockerfile' Contains a script so it runs on any machine

- 'requirements.txt' Python dependency

- 'Telemetry_data(in).csv' 24 hour sample of turbine sensor readings

- 'architecture-diagram.png' Picture of the diagram

- ' Engineering Report.odt'

## Requirements

- Python 3.10+
- pandas

## How to run

1. Clone this repository:

git clone https://github.com/JRBM-png/Areogrid-Engineering-Project.git

Alternatively if you don't have git download the folder and extract it

2. Navigate into the project folder in the terminal:

cd Areogrid-Engineering-Project

3. Install dependencies:

*NOTE* On some systems (modern debian/ubuntu) an "externally-managed-environment" error. If so create a virtual environment

python3 -m venv venv
source venv/bin/activate

Then re-run:

pip install -r requirements.txt

4. Run the script

python analyse_turbines.py

### Running with docker instead

docker build -t areogrid-analysis .

docker run areogrid-analysis
