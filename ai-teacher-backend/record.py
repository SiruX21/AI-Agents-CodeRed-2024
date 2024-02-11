from dotenv import load_dotenv
import logging, verboselogs
from time import sleep
import glob, settings, json

from deepgram import (
    DeepgramClient,
    DeepgramClientOptions,
    LiveTranscriptionEvents,
    LiveOptions,
    Microphone,
    PrerecordedOptions,
    FileSource,
)

load_dotenv()

def transcribe(audio_data=''):
    try:
        # filename = input("Enter the filename for the transcription: ")
        filename = f'transcription_{len(glob.glob("*.txt")) + 1}'

        deepgram = DeepgramClient(settings.config['deepgram_key'])
        dg_connection = deepgram.listen.live.v("1")
        
        def on_message(self, result, **kwargs):
            sentence = result.channel.alternatives[0].transcript
            if len(sentence) == 0:
                return
            print(f"speaker: {sentence}")
            with open(f'transcriptions/{filename}.txt', 'a') as f:
                f.write(sentence + '\n')
        
        def on_metadata(self, metadata, **kwargs):
            print(f"\n\n{metadata}\n\n")

        def on_speech_started(self, speech_started, **kwargs):
            print(f"\n\n{speech_started}\n\n")

        def on_utterance_end(self, utterance_end, **kwargs):
            print(f"\n\n{utterance_end}\n\n")

        def on_error(self, error, **kwargs):
            print(f"\n\n{error}\n\n")

        # dg_connection.on(LiveTranscriptionEvents.Transcript, on_message)
        # dg_connection.on(LiveTranscriptionEvents.Metadata, on_metadata)
        # dg_connection.on(LiveTranscriptionEvents.SpeechStarted, on_speech_started)
        # dg_connection.on(LiveTranscriptionEvents.UtteranceEnd, on_utterance_end)
        # dg_connection.on(LiveTranscriptionEvents.Error, on_erro

        # options = LiveOptions(
        #     model="nova-2",
        #     punctuate=True,
        #     language="en-US",
        #     encoding="linear16",
        #     channels=1,
        #     sample_rate=16000,
        #     # To get UtteranceEnd, the following must be set:
        #     interim_results=True,
        #     utterance_end_ms="1000",
        #     vad_events=True,
        # )
        # dg_connection.start(options)

        # Open a microphone stream on the default input device
        # microphone = Microphone(dg_connection.send)

        # start microphone
        # microphone.start()

        # wait until finished
        # input("Press Enter to stop recording...\n\n")

        # Wait for the microphone to close
        # microphone.finish()

        # Indicate that we've finished
        # dg_connection.finish()

        # with open('audio.wav', 'rb') as audio_file:
        #      buffer_data = audio_file.read()

        buffer_data = bytes(audio_data)

        payload: FileSource = {
            "buffer": buffer_data,
        }

        options = PrerecordedOptions(
            model="nova-2",
            smart_format=True,
        )

        response = deepgram.listen.prerecorded.v("1").transcribe_file(payload, options)

        # logging purposes
        # response = response.to_json(i)

        # with open('results.json', 'w') as results_file:
        #     json.dump(
        #         response,
        #         results_file,
        #         indent = 4
        #     )
        
        response = json.loads(response.to_json())
        
        return response['results']['channels'][0]['alternatives'][0]['transcript']

        # sleep(30)  # wait 30 seconds to see if there is any additional socket activity
        # print("Really done!")

    except Exception as e:
        print(f"Could not open socket: {e}")
        return