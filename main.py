from pathlib import Path
from openai import OpenAI

# 👇 Adicione sua chave da OpenAI aqui
api_key = "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"
client = OpenAI(api_key=api_key)

# Caminho onde o áudio será salvo
speech_file_path = Path(__file__).parent / "speech.mp3"

# Solicita a geração do áudio
response = client.audio.speech.create(
    model="tts-1",
    voice="nova",  # ou shimmer, fable, onyx, etc.
    input="""Olá! Nos últimos meses, nosso time modernizou processos essenciais para entregar soluções com mais velocidade e segurança. 
Precisávamos de um ambiente estável, fácil de gerenciar e de ferramentas que unissem automação, inteligência artificial e colaboração em um só lugar. 
Para isso, montamos uma base sólida com Docker Swarm, Traefik e Portainer, garantindo servidores sempre disponíveis, tráfego inteligente e um painel visual que facilita o dia a dia de toda a equipe. 
Implementamos o Open WebUI com a imagem mais recente, permitindo que qualquer pessoa acesse modelos de IA por meio de uma interface intuitiva, sem dominar comandos complexos. 
Com o n8n, automatizamos tarefas repetitivas e integramos sistemas sem escrever código, liberando horas de trabalho e reduzindo erros. 
Apresentamos o lezGPT, nosso chat inteligente para treinamento de franqueados: suporte 24/7, respostas padronizadas, acesso instantâneo a informações-chave e menos dúvidas recorrentes, acelerando a curva de aprendizado e aliviando a carga do time de atendimento. 
Graças a essas iniciativas, aceleramos deploys, diminuímos o tempo de resolução de incidentes e liberamos a equipe para focar em inovação, não em tarefas operacionais. 
E isso é só o começo! Vamos continuar evoluindo nossa infraestrutura e nossas ferramentas para entregar cada vez mais valor. Muito obrigado pela atenção!"""
)

# Salva o conteúdo da resposta como MP3
with open(speech_file_path, "wb") as f:
    f.write(response.content)

print(f"Narração salva em: {speech_file_path}")
