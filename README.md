<h1 align="center">InnoConvert project</a> 
<img src="https://github.com/blackcater/blackcater/raw/main/images/Hi.gif" height="32"/></h1>
<h1 align="center">Innopolis Summer 2022</a> 

___
### About:
Customer started to do electronic documents management. Therefore, they needed to have some programs for this. One of the wishes was to put an electronic signature in the documents. For the correct visualization of the signature into the document, they needed to convert the document from doc or xls to pdf. What is more, PDF is the guarantee that the original file is not edited. However, customer could not use third party services due to information security.

### Team
Anton Nekhaev - Back-end developer

Elina Akimchenkova - Teamlead

Valeriia Kharina - TechWriter

Karina Denisova - Tester

Roman Voronov - Back-end developer 

Vladimir Surikov - Back-end developer, Security engineer

### Interface
it is a local application, then the interface is through the command line. 
Also it have a version of a web application, then the interface is a REST API.

## Deployment

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
