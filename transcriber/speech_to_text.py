import openai
from dotenv import dotenv_values

def speech_to_text(filepath, title):
    audio_file = open(filepath, 'rb')
    transcript = openai.Audio.transcribe(
        'whisper-1',
        audio_file,
        dotenv_values('.env')['OPENAI_API_KEY']
    )

    if isinstance(transcript, dict) and 'text' in transcript:
        transcript_text = transcript['text']
        transcript_output_location = fr"./transcripts/{title}.txt"
        with open(transcript_output_location, 'w') as file_out:
            file_out.write(transcript_text)
