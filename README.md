# Monitor de Câmbio em Tempo Real (USD → BRL)

Este projeto é um script em **Python** que monitora o valor do dólar em tempo real utilizando uma **API financeira pública**, registra o histórico localmente e pode **enviar alertas automáticos por e-mail** quando o dólar atingir um valor definido pelo usuário.

---

## Funcionalidades

- Conexão com uma API financeira real para obter o valor atual do dólar (USD → BRL)
- Persistência de dados utilizando um arquivo `historico.json`
- Análise automática da variação do dólar (subiu, caiu ou permaneceu estável)
- Execução contínua com atualização a cada 30 segundos
- Envio de alertas por e-mail quando o dólar atinge um valor desejado
- Sistema anti-spam: o e-mail só é enviado uma vez por queda

- - ===============================================
-
- d/m/ano h:m:s
- O valor do dólar é : x.x
- O valor antigo do dólar é : x.x
- O dólar subiu/está estável/caiu x.x
- Aguardando 30 segundos...
