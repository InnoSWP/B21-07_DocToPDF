#!/bin/sh
http_code=$(curl -s -o $2 -w '%{http_code}' -F file=@$1 http://127.0.0.1:5000/api/convertDocx\?apiKey\=ur38r839u2f8ioejfnndh3wifh3892fyh389f;)

if [[ $http_code -eq 200 ]]; then
    open $2 
	exit 0
fi

## decide which status you want to return for 404 or 500
cat $2
