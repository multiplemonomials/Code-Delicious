# Code Delicious, an Open-Source Vegan Cookbook

## Setup Instructions

Create a venv and install pelican into it:
```shell
python3 -m venv venv # on Windows use python instead of python3
source venv/bin/activate.sh # on Windows with Powershell, run 'venv\Scripts\activate.ps1'
pip install -r requirements.txt
```

## Building the Site Locally

In one terminal, run `pelican -r`. This will generate the site and regenerate if changes are made.

In another terminal, run `pelican -l`. This will serve the generated files.