#Pull Image Python
FROM python:3.8
#make Dir
RUN mkdir App
#set Working dir
WORKDIR /App
#Instal dependencies
RUN apt-get update -y
RUN pip install tensorflow && pip install joblib && pip install flask && pip install Pillow && pip install waitress && pip install gunicorn && pip install flask-talisman
#Copy dependencies file
COPY ./App .
# Expose the Docker container for the application to run on port 1000
EXPOSE 1000
#CMD runinning
CMD python -m gunicorn -w 4 -b 0.0.0.0:1000 --timeout 1200 --certfile /etc/letsencrypt/live/129.213.60.252.nip.io/fullchain.pem --keyfile /etc/letsencrypt/live/129.213.60.252.nip.io/privkey.pem app:app