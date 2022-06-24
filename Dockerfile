FROM ubuntu

ENV DEBIAN_FRONTEND=noninteractive 

EXPOSE 5000

ADD . /doc2pdf
WORKDIR /doc2pdf
RUN apt-get update && apt-get install -y sudo
RUN ./setup.sh
ENTRYPOINT ["./start.sh"]
