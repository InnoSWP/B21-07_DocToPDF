<h1 align="center">InnoConvert project 
<img src="https://github.com/blackcater/blackcater/raw/main/images/Hi.gif" height="32"/></h1>
<h1 align="center">Innopolis Summer 2022</h1> 

___
## Project description
Customer started to do electronic documents management. Therefore, they needed to have some programs for this. One of the wishes was to put an electronic signature in the documents. For the correct visualization of the signature into the document, they needed to convert the document from doc or xls to pdf. What is more, PDF is the guarantee that the original file is not edited. However, customer could not use third party services due to information security.

## Demo


## How to use
This is an API for converting files and to use it you need firstly install the project and then run. steps for installation and running are following ➡️ 
### Setup project

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

### Run the project
Just use the start.sh script
```bash 
./start.sh
```
### Using docker
You can build and run our project with docker:
```bash
git clone https://github.com/InnoSWP/B21-07_DocToPDF
docker build -t doc2pdf .
docker run -p 5000:5000 doc2pdf
```

## Features

| Feature                                      | Suppirted | 
|----------------------------------------------|:---------:|
| converting .doc files                        |     ✅     |
| converting .xls files                        |     ✅     |
| sending multiple files                       |     ❌     |
| converting with different languages texts    |     ✅     |
| converting of files with different encodings |     ✅     |
| returning status codes                       |     ✅     |


## Interface
it is a local application, then the interface is through the command line.
Also it have a version of a web application, then the interface is a REST API.

## Support the team

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com)

### Team
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
