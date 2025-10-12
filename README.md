# PTEN-CORPORA___-PT-EN-TECHSWITCH-ASR



# Como usar o projeto

### Passos para rodar o projeto:

<blockquote>
    <p><strong>⚠️ Atenção:</strong></p>
    <p>
        <strong>ffmpeg</strong> O projeto utiliza <strong>ffmpeg</strong> para converter arquivos de áudio de <strong>MP3</strong> para <strong>WAV</strong>.
    </p>
    <p>
        Certifique-se de ter o <strong>ffmpeg</strong> instalado no seu sistema.
    </p>
</blockquote>


1. **Instalar as dependências:**

```bash
pip install -r requirements.txt
```

2. **Gerar áudios (TTS):**

```bash
python scripts/generate_audio.py
```

Arquivo gerado: audio/*.wav

Explicação: Este script gera arquivos de áudio a partir das frases do corpus_pt_en.csv usando a biblioteca gTTS. O áudio é salvo como arquivos .wav na pasta audio/. O processo também converte os arquivos de .mp3 para .wav com ffmpeg.

3. **Rodar o modelo Whisper para transcrição:**

```bash
python scripts/run_whisper.py
```

Arquivo gerado: whisper_output/transcripts/transcriptions_whisper.csv

Explicação: O Whisper transcreve os áudios gerados e salva as transcrições no arquivo transcriptions_whisper.csv dentro da pasta whisper_output/transcripts/. Esse arquivo contém duas colunas principais: reference (frase original) e hypothesis (transcrição do Whisper).

4. **Avaliar transcrições (WER e CER):**

```bash
python scripts/evaluate.py
```

Arquivo gerado: whisper_output/metrics/transcriptions_whisper_eval.csv

Explicação: Esse script calcula as métricas de WER (Word Error Rate) e CER (Character Error Rate) comparando as transcrições do Whisper com as frases originais. O resultado é salvo no arquivo transcriptions_whisper_eval.csv na pasta whisper_output/metrics/. Esse arquivo contém as métricas para cada transcrição.
