import concurrent.futures
from Connection import Connection
from Event_manager import Event_manager
import msvcrt
import os


class Controller:
    
    def callback(self ,event ,data):
        if event=="raktDicke_Pos":
            print(data)
   

if __name__=='__main__':
    host='192.168.0.52'
    port=2000
    con=Connection(host ,port ,1 ,5740)
    em=Event_manager()
    ctrl=Controller()
    em.subscribe("raktDicke_Pos" ,ctrl.callback)
    ex=concurrent.futures.ThreadPoolExecutor(max_workers=2)
    future1=ex.submit(con.receive)
    future2=ex.submit(em.em_loop)
    
    try:
        while True:
            if msvcrt.kbhit():
                key = msvcrt.getch()
                if key == b'q':  # Exit on 'q' key press
                    print("Exiting...")
                    ex.shutdown(wait=False)  # Shutdown the executor 
                    break        
            # ... (other code in your main thread)
    except Exception as e:
        print(f"Error during execution: {e}")
        ex.shutdown(wait=False)
    os._exit(0)
    
    
    
