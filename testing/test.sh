#!/bin/bash
http_code=$(curl -s -o out.pdf -w '%{http_code}' -F file=@./testing/1.docx http://127.0.0.1:5000/api/convertDocx\?apiKey=ur38r839u2f8ioejfnndh3wifh3892fyh389fa;)
if [[ $http_code -eq 403 ]]; then
    echo "[+] Test for API key"
else
    echo "[-] Test for API key"
    exit 1
fi

http_code=$(curl -s -o out.pdf -w '%{http_code}' -F file=@./testing/1.docx http://127.0.0.1:5000/api/convertDocx;)
if [[ $http_code -eq 403 ]]; then
    echo "[+] Test for no API key provided"
else
    echo "[-] Test for no API key provided"
    exit 1
fi


http_code=$(curl -s -o out.pdf -w '%{http_code}' -F file=@./testing/1.docx http://127.0.0.1:5000/api/convertDocx\?apiKey=ur38r839u2f8ioejfnndh3wifh3892fyh389f;)
if [[ $http_code -eq 200 ]]; then
    echo "[+] Test for sending good file"
else
    echo "[-] Test for sending good file"
    exit 1
fi


http_code=$(curl -s -o out.pdf -w '%{http_code}' -F file=@./testing/corrupted.docx http://127.0.0.1:5000/api/convertDocx\?apiKey=ur38r839u2f8ioejfnndh3wifh3892fyh389f;)
if [[ $http_code -eq 500 ]]; then
    echo "[+] Test for corrupted file"
else
    echo "[-] Test for corrupted file"
    exit 1
fi

http_code=$(curl -s -o out.pdf -w '%{http_code}' -F file=@./testing/Ludens.mp3 http://127.0.0.1:5000/api/convertDocx\?apiKey=ur38r839u2f8ioejfnndh3wifh3892fyh389f;)
if [[ $http_code -eq 500 ]]; then
    echo "[+] Test for not docx files"
else
    echo "[-] Test for not docx files"
    exit 1
fi
