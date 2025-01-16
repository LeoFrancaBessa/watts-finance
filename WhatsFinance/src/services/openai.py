from openai import OpenAI
import json
from dotenv import load_dotenv
import os

load_dotenv()

def get_intent_message(message):

    client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
    )

    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    store=True,
    messages=[
        {"role": "user", "content": "Registre um gasto de R$ 50 em alimentação hoje."},
        {"role": "assistant", "content": '{"intent": "Registrar gasto", "parameters": {"amount": 50, "category": "alimentação", "date": "hoje"}}'},

        {"role": "user", "content": "Eu gastei 300 reais no aluguel."},
        {"role": "assistant", "content": '{"intent": "Registrar gasto", "parameters": {"amount": 300, "category": "aluguel"}}'},

        {"role": "user", "content": "Adicione um gasto de R$ 120 com transporte na terça-feira passada."},
        {"role": "assistant", "content": '{"intent": "Registrar gasto", "parameters": {"amount": 120, "category": "transporte", "date": "terça-feira passada"}}'},

        {"role": "user", "content": "Vou gastar 250 reais em lazer este mês."},
        {"role": "assistant", "content": '{"intent": "Registrar gasto", "parameters": {"amount": 250, "category": "lazer", "date": "este mês"}}'},

        {"role": "user", "content": "Quero adicionar mais 500 reais ao meu orçamento mensal."},
        {"role": "assistant", "content": '{"intent": "Adicionar orçamento", "parameters": {"amount": 500}}'},

        {"role": "user", "content": "Coloque mais 2000 reais no meu orçamento."},
        {"role": "assistant", "content": '{"intent": "Adicionar orçamento", "parameters": {"amount": 2000}}'},

        {"role": "user", "content": "Registre que gastei R$ 80 em roupas."},
        {"role": "assistant", "content": '{"intent": "Registrar gasto", "parameters": {"amount": 80, "category": "roupas"}}'},

        {"role": "user", "content": "Quero ajustar meu orçamento para 4000 reais."},
        {"role": "assistant", "content": '{"intent": "Atualizar orçamento", "parameters": {"amount": 4000}}'},

        {"role": "user", "content": "Meu orçamento no mes é de 2200 reais."},
        {"role": "assistant", "content": '{"intent": "Atualizar orçamento", "parameters": {"amount": 2200}}'},

        {"role": "user", "content": "Pode registrar um gasto de 150 reais em educação na semana passada?"},
        {"role": "assistant", "content": '{"intent": "Registrar gasto", "parameters": {"amount": 150, "category": "educação", "date": "semana passada"}}'},

        {"role": "user", "content": "Atualize meu orçamento para 3500 reais."},
        {"role": "assistant", "content": '{"intent": "Atualizar orçamento", "parameters": {"amount": 3500}}'},

        {"role": "user", "content": "Adicione um gasto de R$ 100 em saúde ontem."},
        {"role": "assistant", "content": '{"intent": "Registrar gasto", "parameters": {"amount": 100, "category": "saúde", "date": "ontem"}}'},

        {"role": "user", "content": "Gastei 500 reais no cartão de crédito hoje."},
        {"role": "assistant", "content": '{"intent": "Registrar gasto", "parameters": {"amount": 500, "category": "cartão de crédito", "date": "hoje"}}'},

        {"role": "user", "content": "Quero gastar 900 reais esse mês"},
        {"role": "assistant", "content": '{"intent": "Atualizar orçamento", "parameters": {"amount": 900}}'},

        # Mensagem do usuário atual
        {"role": "user", "content": message},
    ]
    )

    response_message = completion.choices[0].message.content
    if 'intent' not in response_message:
        return None
    else:
        return json.loads(response_message)