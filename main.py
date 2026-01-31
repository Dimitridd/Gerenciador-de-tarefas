import requests
import json
import re
import time
from datetime import datetime
import smtplib
from email.message import EmailMessage

url = "https://economia.awesomeapi.com.br/last/USD-BRL"

print("Olá! Você gostaria de configurar um email automático de dólar barato?")
resposta1 = input("'s' para Sim / 'n' para Não")

email = ""
valor_desejado = 0.0
alerta_enviado = False

if resposta1 == "s":
    while True:
        aprovado = True
        email = input("Por favor, informe seu e-mail")
        if not re.search(r"@", email):
            print("Sua senha deve conter @")
            aprovado = False
        if not re.search(r".com", email):
            print("Sua senha deve conter .com")
            aprovado = False
        if aprovado:
            break
    while True:
        aprovado = True
        valor_desejado = input("Digite o valor desejado")
        if not re.search(r"\d", valor_desejado):
            print("Seu valor deve conter números")
            aprovado = False
        if re.search(r"[A-Z]", valor_desejado):
            print("Seu valor deve conter apenas números")
            aprovado = False
        if re.search(r"[a-z]", valor_desejado):
            print("Seu valor deve conter apenas números")
            aprovado = False
        if aprovado:
            valor_desejado = float(valor_desejado)
            break

def enviar_email(valor_atual, email):
    msg = EmailMessage()
    msg['Subject'] = "🚨 ALERTA: Oportunidade no Dólar!"
    msg['From'] = "dimitri.d.deccache@gmail.com"
    msg['To'] = email
    msg.set_content(f"O dólar atingiu R$ {valor_atual:.4f}. Hora de conferir!")

    # Configuração do Servidor (Exemplo Gmail)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login('dimitri.d.deccache@gmail.com', 'sua senha aqui')
        smtp.send_message(msg)
        print("E-mail enviado com sucesso!")

def main():
    global alerta_enviado
    resposta = requests.get(url)
    dados = resposta.json()

    def salvar_preco(preco):
        dados_para_salvar = {'ultimo_preco': preco}
        with open('historico.json', 'w') as arquivo:
            json.dump(dados_para_salvar, arquivo)

    try:
        with open('historico.json', 'r') as arquivo:
            valor_lido = json.load(arquivo)
        valor_referencia = valor_lido['ultimo_preco']
    except:
        valor_referencia = 0

    valor_atual = float(dados['USDBRL']['bid'])

    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print("\n===============================================")
    print(f"\n{agora}")
    print(f"O valor do dólar é : {valor_atual: .4f}")
    print(f"O valor antigo do dólar é : {valor_referencia: .4f}")

    diferenca = valor_atual - valor_referencia
    if valor_referencia == 0:
        print("Este é a primeira análise")
    elif valor_atual > valor_referencia:
        print(f"O dólar subiu {diferenca: .4f}")
    elif valor_atual == valor_referencia:
        print("O dólar está estável =")
    else:
        print(f"O dólar caiu {diferenca: .4f}")

    salvar_preco(valor_atual)

    if valor_atual <= valor_desejado and alerta_enviado == False:
        enviar_email(valor_atual, email)
        alerta_enviado = True
    elif valor_atual > valor_desejado:
        alerta_enviado = False

while True:
    main()
    print("Aguardando 30 segundos...")
    time.sleep(30)
