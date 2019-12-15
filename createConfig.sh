#/bin/bash

source .env

SECRET_KEY=`< /dev/urandom tr -dc _A-Z-a-z-0-9 | head -c${1:-32};echo;`

sed "
  s/%SECRET_KEY%/${SECRET_KEY}/;

  s/%DB_NAME%/${DB_NAME}/;
  s/%DB_USERNAME%/${DB_USERNAME}/;
  s/%DB_PASSWORD%/${DB_PASSWORD}/;

  s/%MAIL_HOST%/${MAIL_HOST}/;
  s/%MAIL_FROM%/${MAIL_FROM}/;
  s/%MAIL_PASSWORD%/${MAIL_PASSWORD}/;
  s/%MAIL_USERNAME%/${MAIL_USERNAME}/;
" config.py.template > config.py
