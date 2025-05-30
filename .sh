curl https://api.openai.com/v1/audio/speech \
  -H "Authorization: Bearer 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
" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "tts-1",
    "voice": "nova",
    "input": "Olá! Nos últimos meses, nosso time modernizou processos essenciais para entregar soluções com mais velocidade e segurança. \
Precisávamos de um ambiente estável, fácil de gerenciar e de ferramentas que unissem automação, inteligência artificial e colaboração em um só lugar. \
Para isso, montamos uma base sólida com Docker Swarm, Traefik e Portainer, garantindo servidores sempre disponíveis, tráfego inteligente e um painel visual que facilita o dia a dia de toda a equipe. \
Implementamos o Open WebUI com a imagem mais recente, permitindo que qualquer pessoa acesse modelos de IA por meio de uma interface intuitiva, sem dominar comandos complexos. \
Com o n8n, automatizamos tarefas repetitivas e integramos sistemas sem escrever código, liberando horas de trabalho e reduzindo erros. \
Apresentamos o lezGPT, nosso chat inteligente para treinamento de franqueados: suporte 24/7, respostas padronizadas, acesso instantâneo a informações-chave e menos dúvidas recorrentes, acelerando a curva de aprendizado e aliviando a carga do time de atendimento. \
Graças a essas iniciativas, aceleramos deploys, diminuímos o tempo de resolução de incidentes e liberamos a equipe para focar em inovação, não em tarefas operacionais. \
E isso é só o começo! Vamos continuar evoluindo nossa infraestrutura e nossas ferramentas para entregar cada vez mais valor. Muito obrigado pela atenção!"
  }' --output narracao.mp3
