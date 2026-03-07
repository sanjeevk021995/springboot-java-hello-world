import requests
import threading
import time

URL = "http://springboot.127.0.0.1.nip.io:9090/hello"
RPS = 5000

def send():
    try:
        r = requests.get(URL)
        print(r.status_code)
    except:
        pass

while True:
    threads = []

    for i in range(RPS):
        t = threading.Thread(target=send)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    time.sleep(1)