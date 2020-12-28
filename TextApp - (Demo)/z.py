import tts.sapi
voice = tts.sapi.Sapi()
voice.set_voice('David')
voice.create_recording('output.wav', text)