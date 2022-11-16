# start by pulling the python image
FROM python:3.8

ARG External_Port=22
ARG External_IP=0.0.0.0
# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt
VOLUME [ "/app/scores/"]
# copy every content from the local file to the image
COPY ./main.py /app/
COPY ./utils/ /app/utils/
COPY ./live.py /app/
#COPY ./scores/scores.txt /app/scores/
COPY ./games/ /app/games/

EXPOSE ${External_Port}

# configure the container to run in an executed manner
ENTRYPOINT [ "python","main.py"]
