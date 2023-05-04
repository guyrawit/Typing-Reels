from django.core.files.storage import default_storage
from google.cloud import speech_v1p1beta1 as speech

def generate_transcript_ai(movie_scene):
    
    # initialize google cloud speech client
    client = speech.SpeechClient()
    
    # get path mp3 file of movie in google cloud storage
    path = movie_scene.audio_file.name
    
    # read audio file to bytes
    with default_storage.open(path, 'rb') as f:
        content = f.read()
        # Set the speech recognition configuration
    
    audio = speech.RecognitionAudio(content=content)
    
    # config speech recognition model to fit with my mp3 file    
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.MP3,
        sample_rate_hertz=44000,
        language_code="en-US",
        model="video"
    )

    # run model
    operation = client.long_running_recognize(config=config, audio=audio)
    response = operation.result(timeout=90)
    transcript = ''
    for result in response.results:
        transcript += result.alternatives[0].transcript + "."
        # The first alternative is the most likely one for this portion.
        print("Transcript: {}".format(result.alternatives[0].transcript))
        print("Confidence: {}".format(result.alternatives[0].confidence))
        
    # Update the transcript_ai field in the model
    movie_scene.transcript_ai = transcript
    movie_scene.save()
