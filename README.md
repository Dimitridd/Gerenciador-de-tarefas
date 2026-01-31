# Monitor de Câmbio em Tempo Real:

- Conexão: O programa se conecta a uma API financeira real para buscar o preço mais recente.
- Memória: Ele lê um arquivo historico.json para saber qual era o preço da última vez que ele verificou.
- Inteligência (Lógica): Ele compara o preço novo com o antigo e decide se o dólar subiu, caiu ou estabilizou.
- Automação: Em vez de você rodar o script toda hora, ele fica rodando sozinho em um loop infinito, verificando o preço a cada 30 segundos (ou o tempo que você definir).
- Registro: Ele salva o novo preço no arquivo para a próxima comparação.
-
- ===============================================
-
- d/m/ano h:m:s
- O valor do dólar é : x.x
- O valor antigo do dólar é : x.x
- O dólar subiu/está estável/caiu
- Aguardando 30 segundos...