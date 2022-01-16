Intorduction

A data engineering assignment that ingests data about Air Quality Measures on 
the National Environmental Health Tracking Network. The data is downloaded from data.gov and 
it's in Json format.

Implementation overview

The solution consists of two services. 
- A containerized Python application which reads, validates and transfers data to PostgreSQL.
- A containerized PstgreSQL as data warehouse.
Both services are designed to be run in one container and the docker-compose file can be found
  in the root directory of the project.

Prerequisits:
To install and deploy components, you need to have Docker.

Configuration steps:

Navigate into the root of the project and run the following command:
docker compose up --build -d

This will build and run two containers mentioned above.

In order to see the application logs run:
docker logs data_ingestion_assignment_app_1

Notes on how the solution is implemented

tasks list

Get the docker app "working", prints on screen -- DONE
Get the app to connect and query Postgres -- DONE
Get the app to read the meta data from Json file and make create table automatically -- DONE
Make a simple data validation to check the length of the each record -- Done
Batch insert valid data into the right table and errors into the errors tables  -- DONE
Containerize the app and Postgres using Docker-compose --Done

Development considerations
- The data is downloaded from https://catalog.data.gov/dataset/air-quality-measures-on-the-national-environmental-health-tracking-network
and storored under the /app directory. 
- In oredr to overcome the order of getting up postgres and then running the application, 
"wait-for-it.sh" is used. for more info please see:
https://docs.docker.com/compose/startup-order/
- Containerizing the app and Postgres is inspired from:
https://github.com/stefanopassador/Tutorial_DockerPythonPostgres

Next steps:
Improve data validation
