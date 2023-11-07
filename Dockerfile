#Pull Image Python
FROM python:3.8
#make Dir
RUN mkdir App
#set Working dir
WORKDIR /App
#Instal dependencies
RUN apt-get update -y
RUN pip install tensorflow && pip install joblib && pip install flask && pip install Pillow && pip install waitress
#Copy dependencies file
COPY ./App .
# Expose the Docker container for the application to run on port 1000
EXPOSE 1000
#CMD runinning
CMD python app.py