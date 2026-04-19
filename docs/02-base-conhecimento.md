# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores, já entendendo o que o cliente busca e continuar com a ajuda |
| `perfil_investidor.json` | JSON | Personalizar recomendações de acordo com a renda e objetivos |
| `produtos_financeiros.json` | JSON | Sugerir produtos adequados ao perfil do usuário |
| `transacoes.csv` | CSV | Analisar padrão de gastos do cliente, sugerindo melhora para conseguir investir mais e melhor |


## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Não modifiquei.

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Os JSON/CSV são carregados ao iniciar a seção, no decorrer dela e com base no contexto fornecido pelo usuário 

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

Os dados são utilizados de forma dinâmica, sendo incorporados ao contexto da conversa conforme a necessidade da interação.

O agente consulta os arquivos JSON e CSV para obter informações relevantes sobre o usuário, como perfil de investidor, histórico de transações e interações anteriores. Esses dados são então estruturados e inseridos no contexto da mensagem enviada ao modelo, permitindo respostas mais personalizadas e coerentes.

O system prompt define o comportamento do agente (como um assistente financeiro), enquanto os dados da base de conhecimento são adicionados como contexto adicional nas mensagens do usuário.
---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
Dados do Cliente:
- Nome: Maria Santos
- Perfil: Iniciante
- Renda mensal: R$ 1.500
- Saldo disponível: R$ 200

Objetivo:
- Começar a investir mesmo com pouco dinheiro
- Criar uma reserva de emergência

Produtos recomendados:
- Tesouro Selic
- CDB com liquidez diária
- Conta remunerada

Últimas transações:
- 02/11: Supermercado - R$ 320
- 05/11: Conta de luz - R$ 120
- 08/11: Transporte - R$ 90
- 10/11: Lanche - R$ 45
