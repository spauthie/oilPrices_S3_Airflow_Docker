# Brent/WTI daily prices to S3 Bucket

## Aim
The goal of this project is to retrieve oil prices from investpy API and store the data as .csv file into S3 Bucket. To do it, we run a simple dag using Apache Airflow with Docker.


## Informations

* Based on Python (3.7-slim-buster) official Image [python:3.7-slim-buster](https://hub.docker.com/_/python/) and uses the official [Postgres](https://hub.docker.com/_/postgres/)
* Install [Docker](https://www.docker.com/)
* Install [Docker Compose](https://docs.docker.com/compose/install/)
* Following the Airflow release from [Python Package Index](https://pypi.python.org/pypi/apache-airflow)


## Installation

Pull the image from the Docker repository.

    docker pull puckel/docker-airflow


## Usage

We will need to create a virtual env where will store our AWS credentials. To do it, you can run the following commandes line

On **Windows Powershell**:
```shell
    virtualenv airflow
    .\airflow\Scripts\activate.ps1 #Activation
    $env:AWS_SECRET_ACCESS_KEY='XXXXXXXXXXXXXXXXXXX'
    $env:AWS_ACCESS_KEY_ID='YYYYYYYYYYYYYYYYY'
    ```

If our are using Linux or Mac, commandes will be slightly diffent

You also need to update the bucket name will you want to use in the oil_price.py file.


After this you can the following commande to build the image and run your containers

For **LocalExecutor** :

    docker-compose -f docker-compose-LocalExecutor.yml up -d

You now go to http://localhost:8080/ where you should see the dag. Activate it and trigger your dag!