# ChatApp
### This is a chat application build in python using flask and socket.io. 

This is a pretty basic application which offers a single room for all the participants to communicate. Keeping the process simple, there's no login required. Users can simply jump to the main page, add their name(username, this has to unique for all the participants in the room) and start their conversation. The chat is in real time, i.e. it is not saved. There's a list shown at the bottom of all the participants present in the room. Apart from that, there's a feature that allows users to send any sentence which they want to be broken down, i.e, users can send a message prepending '|' in the statement and the application will tell the type of word for each word in the sentence. Hope you like it. :)

## To run the application locally:
Create a virtual environment and activate it. After that install the requirements using:
```pip install -r requirements.txt
python -m nltk.downloader punkt averaged_perceptron_tagger```

After successfully installing the requirements, run:
```python app.py```


## To run the application as a container:

After successfully downloading the code,
step into the working directory:
``` cd Demo-ChatApp```
and run the command to build the image:
```docker build -t chatapp .``` 

This will create an image of name "chatapp" with all the requirements and code.

To run the container from that image:
```docker run -p 5000:5000 --name demo chatapp```

This will make a container and you will be able to access it on the port 5000 of your machine.

#### If using a virtual machine or an EC2 instance, make sure to update the address at which the socketio will run. Update it with the public IP of that machine.
