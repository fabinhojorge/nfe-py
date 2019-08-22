# nfe-py
This projects consumes the Arquivei's API to fetch a list of NFE



## Introduction


## Requirements


## Steps

    > docker-compose build
    > docker-compose up 

Access the localhost

    > Run web migration

## Links

## STEPS
Possible problem with the Endpoint: /v1/nfe/received

When it reaches the last page.next, it still prints a page.next that is the same for the current address. 
The problem is that it is supposed to be the last, so the next should be empty indicating that there are no next.

All the requests to https://sandbox-api.arquivei.com.br/v1/nfe/received?cursor=291&limit=50 returns the same address in page.next

## Screen Shots