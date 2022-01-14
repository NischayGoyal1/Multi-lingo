#importingg required modules
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import os

#Converting text to speech
#Using gtts and playing it with playsound
def nischay(text,lang):
    ivu=gTTS(text=text ,lang=lang, slow= False)
    filename="voice.mp3"
    ivu.save(filename)
    song=AudioSegment.from_mp3(filename)
    play(song)
    os.remove(filename)
