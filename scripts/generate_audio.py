import pandas as pd
from gtts import gTTS
import os

# Criar pasta de áudio
os.makedirs("audio", exist_ok=True)

# Ler CSV
df = pd.read_csv("csv/corpus_pt_en.csv")

for idx, row in df.iterrows():
    frase = row['frase']
    audio_path = f"audio/{str(row['id']).zfill(3)}.wav"
    
    # Gerar TTS (gTTS) - idioma português
    tts = gTTS(frase, lang='pt')
    tts.save(audio_path.replace('.wav','.mp3'))
    
    # Converter mp3 para wav com ffmpeg
    os.system(f"ffmpeg -y -i {audio_path.replace('.wav','.mp3')} -ar 16000 -ac 1 {audio_path}")
