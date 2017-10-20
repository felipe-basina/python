# Desafio
Objetivo: verificar cpf confrontando com uma blacklist <br />
Referência: https://github.com/idwall/python-test

## Versão Python
 - `>= 3

## Procedimentos
 - Criar virtual environment <br /> virtualenv venv

 - Ativar virtual environment <br /> venv\Scripts\activate
 
 - Instalar dependência <br /> pip install flask

## Testes de unidade
 Executar <br /> test_cpf_blacklist.py
 
## Aplicação
 Executar <br /> cpf_blacklist.py
 
 - Exemplos de chamadas: <br />

 curl localhost:5000/00000000000
 >> "BLOCK"
 
 curl localhost:5000/
 >> "RUNNING"
 
 curl localhost:5000/26347271940
 >> "FREE"