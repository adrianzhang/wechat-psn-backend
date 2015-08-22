#######################################################################################
#    This Dockerfile used to create Linux+Web+Python+WeRoBot  for DaoCloud.io user    #
#    Based on official Python 2.7 docker image                                        #
#######################################################################################

FROM daocloud.io/python:2.7.10

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . /usr/src/app

RUN pip install -r requirements.txt

EXPOSE 80

CMD [ "python","index.wsgi"]