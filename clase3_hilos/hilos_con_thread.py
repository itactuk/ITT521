import _thread, threading
import time
import queue

inicio = time.time()

x = queue.Queue()
for i in range(20):
    x.put(i)


def procesar():
    data = x.get()
    time.sleep(2)  # simulando trabajo
    print(f"Soy el hilo {threading.current_thread().name} "
          f"y tengo la data {data}")
    x.task_done()

for i in range(20):
    _thread.start_new_thread(procesar, ())

x.join()


print(f"Tardó {time.time()-inicio}s en ejecutarse")
