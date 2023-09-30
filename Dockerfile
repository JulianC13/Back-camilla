# start by pulling the python image
FROM --platform=linux/amd64 python:3.8-alpine

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# copy every content from the local file to the image
COPY . /app

# #Expose the required port
EXPOSE 8282

# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

CMD ["camilla.py"]