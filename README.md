# Docker Zermatt Reservation Installation on ARM

## Install from scratch

1. Clone the git repo
    ```bash
    git clone https://github.com/patklaey/docker-zermatt-reservation
    cd docker-zermatt-reservation
    ```
1. Modify the ```.env``` file to change passwords and other settings
    ```bash
    vi .env
    ```
1. Create your configuration file for the API
    ```bash
    ./createConfig.sh
    ```
1. Adapt the configuration for the frontend. Remember: As the angular app does not run in the container, but serves the
application to be run on the client machine, the ```API_ENDPOINT``` needs to point to the public API endpoint (e.g. 
```https://zermatt-api.patklaey.ch```)
    ```bash
    vi config.js
    ```
1. Start up the containers
    ```bash
    docker-compose up -d
    ```
1. Initialize the database
    ```bash
    docker exec zermatt-api sh -c "export FLASK_APP=cli && flask initdb"
    ```
1. Add an admin user
    ```bash
    docker exec zermatt-api sh -c "export FLASK_APP=cli && flask addadminuser"
    ```
1. Point your browser to your zermatt reservation page, login as admin and change the password :)


## Install from existing Zermatt Reservation installation

1. Clone the git repo
    ```bash
    git clone https://github.com/patklaey/docker-zermatt-reservation
    cd docker-zermatt-reservation
    ```
1. Modify the ```.env``` file to change passwords and other settings to match current setup 
    ```bash
    vi .env
    ```
1. Copy the current config.py (from backup or live server) to the current directory
    ```bash
    cp /path/to/backup/config.py .
    ```
1. Make sure the ```SQLALCHEMY_DATABASE_URI``` points to ```database``` as host, so for example: 
```'mysql+pymysql://%DB_USERNAME%:%DB_PASSWORD%@database/%DB_NAME%'```
1. lication to be run on the client machine, the ```API_ENDPOINT``` needs to point to the public API endpoint (e.g. 
```https://zermatt-api.patklaey.ch```)
    ```bash
    vi config.js
    ```
1. Start up the containers
    ```bash
    docker-compose up -d
    ```
1. Copy the database backup into the db container
    ```bash
    docker cp /path/to/backup/zermatt-utf.sql zermatt-db:/root/zermatt-utf.sql
    ```
1. Import the database backup
    ```bash
    source .env
    docker exec zermatt-db sh -c "mysql --default-character-set=latin1 -u ${DB_USERNAME} --password=${DB_PASSWORD} ${DB_NAME} < /root/zermatt-utf.sql"  
    ```
    
## Troubleshooting

1. Should you have an issues with accessing the DB (wrong password) make sure in ```.env``` the DB passwords are not in
quotes, that somehow does not work
1. Also if you get errors when initializing the DB, a error like 
```pymysql.err.InternalError: Packet sequence number wrong - got 1 expected 0``` can be related to the DB passwords.
Simply change the passwords in ```.env``` to a very simple one (such that no quotes are needed), and try again. If it
works now, it's password related, otherwise there is another issue. 