# Orient

Orient is a text messaging service that texts Lauren Goemaat a choice photo every hour at the top of the hour

## Getting Started

1. Create a virtual environment: `virtualenv venv`
2. Install all dependencies: `pip install -r requirements.txt`
3. Load local environment variables: `source local.env`
4. Execute the service: `python lambda.py`

## Hosting and Deployment

1. Install the serverless framework globally: `npm i -g serverless`
2. Install the Python requirements plugin for serverless: `npm i`
3. Set environment variables in `prod.env.yml`
4. Deploy: `serverless deploy`
