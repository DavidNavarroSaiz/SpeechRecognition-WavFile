import uvicorn
from fastapi import FastAPI,UploadFile,File
import speech_recognition as sr
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.cors import CORSMiddleware
import soundfile as sf
import io




app = FastAPI()

# Specify the allowed origins for CORS
origins = [
    "http://127.0.0.1:3000",  # Replace with the correct URL of your front-end
]

# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}


# @app.post("/recognize-speech")
# async def recognize_speech(file_path: str):
#     # Load the audio file
#     r = sr.Recognizer()
#     with sr.WavFile(file_path) as wav_file:
#         audio = r.record(wav_file)

@app.post("/recognize-speech")
async def recognize_speech(audio: UploadFile = File(...)):
    # Load the audio file
    r = sr.Recognizer()
    with sr.AudioFile(audio.file) as audio_data:
        audio_data = r.record(audio_data)
    # with io.BytesIO(audio.file.read()) as audio_stream:
    #     audio_data = sr.AudioFile(audio_stream)
    # # Perform speech recognition
    # with audio_data as source:
    #     audio_data = r.record(source)
    # # Perform speech recognition
    try:
        recognized_text = r.recognize_google(audio_data,language= "es-CO")
        return {"result": recognized_text}
    except sr.UnknownValueError:
        return {"result": "Speech recognition failed: Unable to understand audio"}
    except sr.RequestError as e:
        return {"result": f"Speech recognition failed: {str(e)}"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)