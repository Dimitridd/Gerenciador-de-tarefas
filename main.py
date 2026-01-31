import requests
import json
import time
from datetime import datetime

url = "https://economia.awesomeapi.com.br/last/USD-BRL"

def main():
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
    print(f"O valor do dólar é : {valor_atual}")
    print(f"O valor antigo do dólar é : {valor_referencia}")
    print(__name__)
    if valor_referencia == 0:
        print("Este é a primeira análise")
    elif valor_atual > valor_referencia:
        print("O dólar subiu ^")
    elif valor_atual == valor_referencia:
        print("O dólar está estável =")
    else:
        print("O dólar caiu =")

    salvar_preco(valor_atual)

while True:
    main()
    print("Aguardando 30 segundos...")
    time.sleep(30)