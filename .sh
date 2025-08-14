curl https://api.openai.com/v1/audio/speech \
  -H "Authorization: Bearer API_KEY
" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "tts-1",
    "voice": "nova",
    "input": "TEXT"
  }' --output example_name.mp3
