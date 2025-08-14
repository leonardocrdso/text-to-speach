from pathlib import Path
from openai import OpenAI

# 👇 Adicione sua chave da OpenAI aqui
api_key = "API_KEY"
client = OpenAI(api_key=api_key)

# Caminho onde o áudio será salvo
speech_file_path = Path(__file__).parent / "speech.mp3"

# Solicita a geração do áudio
response = client.audio.speech.create(
    model="tts-1",
    voice="nova",  # ou shimmer, fable, onyx, etc.
    input="""TEXT"""
)

# Salva o conteúdo da resposta como MP3
with open(speech_file_path, "wb") as f:
    f.write(response.content)

print(f"Narração salva em: {speech_file_path}")
