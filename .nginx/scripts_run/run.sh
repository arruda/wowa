#!/bin/bash

echo "waitig for app"
while ! exec 6<>/dev/tcp/${APP_PORT_8000_TCP_ADDR}/${APP_PORT_8000_TCP_PORT}; do
    echo "$(date) - still trying to connect to app at ${APP_PORT}"
    sleep 1
done

nginx