<h1 align="center">InnoConvert project 
<img src="https://github.com/blackcater/blackcater/raw/main/images/Hi.gif" height="32"/></h1>
<h1 align="center">Innopolis Summer 2022</h1> 

___
## ๐ Project description 
Customer started to do electronic documents management. Therefore, they needed to have some programs for this. One of the wishes was to put an electronic signature in the documents. For the correct visualization of the signature into the document, they needed to convert the document from doc or xls to pdf. What is more, PDF is the guarantee that the original file is not edited. However, customer could not use third party services due to information security.

## ๐ฟ Demo 

![Teaser](https://i.imgur.com/RKDEVjB.gif)


## ๐งท How to use
This is an API for converting files and to use it you need firstly install the project and then run. steps for installation and running are following โก๏ธ 
### ๐ Setup project

1. Clone the repository

2. Open the directory of the project

2. Give executable ability to execute the setup and start script
``` bash
chmod +x setup.sh start.sh
```

3. Install the required packages, libraries, add fonts, and configure the virtual environment for python
```bash 
./setup.sh
```

### ๐คพโโ๏ธ Run the project
Just use the start.sh script
```bash 
./start.sh
```
### ๐ Using docker 
You can build and run our project with docker:
```bash
git clone https://github.com/InnoSWP/B21-07_DocToPDF
docker build -t doc2pdf .
docker run -p 5000:5000 doc2pdf
```

## โ๏ธ Features

| Feature                                      | Supported | 
|----------------------------------------------|:---------:|
| converting .doc files                        |     โ     |
| converting .xls files                        |     โ     |
| converting with different languages texts    |     โ     |
| converting of files with different encodings |     โ     |
| returning status codes                       |     โ     |
| 100 converted files per minute               |     โ     |
| sending multiple files in zip archive        |     โ     |


## ๐ฑ Interface 
it is a local application, then the interface is through the command line.
Also it have a version of a web application, then the interface is a REST API.


### ๐ต๐ป Team

![GitHub Contributors Image](https://contrib.rocks/image?repo=InnoSWP/B21-07_DocToPDF)

Anton Nekhaev - Back-end developer

[<img src="https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white">](https://t.me/anekhaev)

Elina Akimchenkova - Teamlead

[<img src="https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white">](https://t.me/akmchnkv)

Valeriia Kharina - TechWriter

[<img src="https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white">](https://t.me/exemplerie)

Karina Denisova - Tester

[<img src="https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white">](https://t.me/karinadenisova)

Roman Voronov - Back-end developer

[<img src="https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white">](https://t.me/porludom)

Vladimir Surikov - Back-end developer, Security engineer

[<img src="https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white">](https://t.me/MasterLogick)


## ๐ง Technology
This is progect on python. To convert files we use LibreOffice.

![OS Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
[![linter sonarcloud](https://img.shields.io/badge/Sonar%20cloud-F3702A?style=for-the-badge&logo=sonarcloud&logoColor=white)](https://sonarcloud.io/summary/new_code?id=doctopdf07&branch=main)

## ๐ License

[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/InnoSWP/B21-07_DocToPDF/blob/main/LICENSE)

MIT License gives everybody rights to do any actions like using the software, copying, modifying, selling the copies etc. However, there is one restriction: any copies or substantial portions of the software must include the original copyright notice and permission notice. What is more, MIT License is free to extend (like Free Software Foundation did). Finally, software with MIT License provided without any warranties.


