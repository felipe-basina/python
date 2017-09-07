from requests import put, get

def invocar_operacoes_todo():
    print("PUT %s" % 
        put('http://localhost:5000/todo0', data={'data': 'Remember the milk'}).json())
    print("GET %s" % 
        get('http://localhost:5000/todo0').json())
    print("PUT %s" % 
        put('http://localhost:5000/todo1', data={'data': 'Change my brakepads'}).json())
    print("GET %s" % 
        get('http://localhost:5000/todo1').json())

if __name__ == '__main__':
    print("Executando endpoints Flask")
    invocar_operacoes_todo()