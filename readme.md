### FAST API Wav File

This is a simplified version of the FAST API demonstration, where the client sends an audio file to the server for speech recognition, which then returns the recognized text.

This section includes a client-server application pair using FAST API, Python, HTML, and JavaScript. The client and server components work together to offer speech recognition and text-to-speech functionality. Various models are supported for speech recognition and text-to-speech conversion.

the key difference of this project is that it works with only audio data saved as mp3 files and it only works with google model.

For the speech recognition it is returned an string with all the results
For Texto to speech  it is returned a single audio file which is a concatenation of the results of each model.


## How to run 


### API:
go to the 'fast_api_speech_all_models/api'

Create a new environment
```
    python3.8 -m venv <env_name>
```
if you are using anaconda you just can write the following code line:

```
    conda create --name <env_name> python=3.8
```
activate the envitonrment:

```
    cd <env_name> \Scripts\activate.bat
```

<p>Anaconda:<p>

```
    conda activate <env_name>
```
```    
    conda install pip
    pip install -r requirements.txt
```


run in the terminal:
```
uvicorn main:app --reload

```
the app now is running at:

`http://127.0.0.1:8000`

to learn what are the endpoints and how to interact with the app open the following link at the explorer:

`http://127.0.0.1:8000/docs`


### Client 

to run the client as a web server use the http server of python or any similar , to do that write in the terminal

`python -m http.server 2000`
the port(2000) has to be in the main.py in the origins section:
```
origins = [
    "http://127.0.0.1:3000",  #  URL of your front-end
    "http://127.0.0.1:2000",  #  URL of your front-end
    "http://127.0.0.1:1000",  #  URL of your front-end
]

```

you have to be in the same folder as the ./client/index.html file to run that command






## What you will find:

in the `./client/script.js` you can find the petitions that are done to the API
and in the index.html you will find a very basic structure of the project.



