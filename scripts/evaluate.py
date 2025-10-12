import pandas as pd
from jiwer import wer, cer

df_results = pd.read_csv("transcripts/transcriptions_whisper.csv")

df_results['WER'] = df_results.apply(lambda x: wer(x['reference'], x['hypothesis']), axis=1)
df_results['CER'] = df_results.apply(lambda x: cer(x['reference'], x['hypothesis']), axis=1)

df_results.to_csv("metrics/transcriptions_whisper_eval.csv", index=False)
print(df_results[['id','WER','CER']])
