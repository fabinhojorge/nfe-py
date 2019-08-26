# nfe-py
This projects consumes the Arquivei's API to fetch a list of NFEs



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

Sync valid first request (New)
![Database Empty](assets/sync_valid_new.png)

Sync valid any other request (No change)
![Database Empty](assets/sync_valid_no_change.png)

Sync error 500
![Sync error 500](assets/request_error500.png)

Find but when there are no data synchronized 
![Find Database empty](assets/database_empty.png)

Valid request for Find
![Find valid request](assets/find_valid_request.png)

Access Key was not find
![Find invalid request](assets/find_wrong_access_key.png)
