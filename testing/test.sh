#!/bin/bash
http_code=$(curl -s -o out.pdf -w '%{http_code}' -F file=@./testing/1.docx http://127.0.0.1:5000/api/convertDocx\?apiKey\=ur38r839u2f8ioejfnndh3wifh3892fyh389fa;)
echo $http_code
if [[ $http_code -eq 403 ]]; then
    echo "[+] Test for API key"
    exit 0
else
    echo "[-] Test for API key"
    exit 1
fi


http_code=$(curl -s -v -o out.pdf -w '%{http_code}' -F file=@./testing/1.docx http://127.0.0.1:5000/api/convertDocx\?apiKey\=ur38r839u2f8ioejfnndh3wifh3892fyh389f;)
if [[ $http_code -eq 200 ]]; then
    echo "[+] Test for sending good file"
    exit 0
else
    echo "[-] Test for sending good file"
    exit 1
fi
