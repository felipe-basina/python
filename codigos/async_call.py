from multiprocessing.pool import ThreadPool
import time

pool = ThreadPool(processes=1)

def teste_thread():
  for k in range(5):
    print('Executando Thread...\n')
    time.sleep(1)
  return 'Thread Executada com sucesso!'

def exec():
    async_call = pool.apply_async(teste_thread)
    print('Processando....')
    time.sleep(10)
    return async_call.get()
  
if __name__ == '__main__':
    print(exec())
