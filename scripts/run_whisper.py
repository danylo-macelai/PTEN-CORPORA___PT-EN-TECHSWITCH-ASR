import whisper
import pandas as pd
import os

os.makedirs("transcripts", exist_ok=True)

model = whisper.load_model("base")  # ou medium / large
df = pd.read_csv("csv/corpus_pt_en.csv")

results = []
for idx, row in df.iterrows():
    audio_path = f"audio/{str(row['id']).zfill(3)}.wav"
    result = model.transcribe(audio_path)
    transcript = result["text"]
    results.append({
        "id": row["id"],
        "reference": row["frase"],
        "hypothesis": transcript
    })

df_results = pd.DataFrame(results)
df_results.to_csv("transcripts/transcriptions_whisper.csv", index=False)
