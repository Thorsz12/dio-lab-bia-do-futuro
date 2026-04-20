client = OpenAI(api_key="SUA_API_KEY")

def gerar_resposta(mensagem):
    resposta = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Você é um assistente financeiro para pessoas de baixa renda."},
            {"role": "user", "content": mensagem}
        ]
    )

    return resposta.choices[0].message.content
