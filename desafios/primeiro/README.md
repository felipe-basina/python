# Desafio
Objetivo: verificar cpf confrontando com uma blacklist

## Versão Python
 - >= 3

## Procedimentos
 - Criar virtual environment
 virtualenv venv

 - Ativar virtual environment
 venv\Scripts\Activate
 
 - Instalar dependência:
 pip install flask

## Testes de unidade
 Executar test_cpf_blacklist.py
 
## Aplicação
 Executar cpf_blacklist.py
 
 - Exemplos de chamadas:
 curl localhost:5000/00000000000
 >> "BLOCK"
 
 curl localhost:5000/
 >> "RUNNING"
 
 curl localhost:5000/26347271940
 >> "FREE"