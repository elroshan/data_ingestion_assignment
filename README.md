# Intorduction

A data pipeline that ingests data about Air Quality Measures on the National Environmental
Health Tracking Network. The json format data is downloaded from data.gov.

# Implementation overview

The solution consists of two services. 
- A containerized Python application which reads, validates and transfers data to PostgreSQL.
- A containerized PstgreSQL where data is stored in relational format.

The docker-compose file in the root directory is used to define the services.

# Prerequisites
To install and deploy, you need to have Docker Desktop.

# Configuration steps

Navigate to the root of the project and run the following command:

`docker compose up --build -d`

This will build and run two containers mentioned above.

In order to see the application logs run:

`docker logs data_ingestion_assignment_app_1`

# Notes 
Here some high level notes on how the solution was implemented is shared.

## Tasks list

- Get the docker app "working", prints on screen.
- Get the app to connect and query Postgres.
- Get the app to read the metadata from json file and make 'create table' automatically.
- Make a simple data validation to check the length of each record.
- Batch insert valid data into the right table and errors into the invalid-data table.
- Containerize the app and Postgres using Docker-compose.

## Development considerations
- The data is downloaded from https://catalog.data.gov/dataset/air-quality-measures-on-the-national-environmental-health-tracking-network
and stored under the /app directory. 
- To start services in the right order, i.e. first postgres and then the application, "wait-for-it.sh" is used. for more info please see:
https://docs.docker.com/compose/startup-order/
- Containerizing the app and Postgres is inspired from:
https://github.com/stefanopassador/Tutorial_DockerPythonPostgres

## Next steps:
Improve data validation, though given the schema it's hard to imagine what more can be achieved automatically.