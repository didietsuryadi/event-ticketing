# Project Title

## Event Ticketing API

## Description

#### API for provide ticketing event services

## Getting Started

> docker-compose build
> docker-compose run web python manage.py migrate
> docker-compose up

# Routes

|Route| Method|
|-----|-------|
|Transacttion|
|/api/v1/transaction/get_info/:id|GET|
|/api/v1/transaction/purchase|POST|
|Event|
|/api/v1/event/get_info/:id|GET|
|/api/v1/event/create|POST|
|/api/v1/event/ticket/create|POST|
|Location|
|/api/v1/transaction/purchase|POST|

### for postman request sample available on folder example
