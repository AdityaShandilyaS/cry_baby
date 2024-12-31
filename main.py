import pyaudio
import wave

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 8000

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print('Starting recording')

frames = []
seconds = 7
for i in range(0, int(RATE/ CHUNK * seconds)):
    data = stream.read(CHUNK)
    frames.append(data)

print('Stopping recording')

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open('test.wav', 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()