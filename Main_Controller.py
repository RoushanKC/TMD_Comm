import concurrent.futures
from Connection import Connection
from Event_manager import Event_manager


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
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:
        ex.submit(con.receive)
        ex.submit(em.em_loop)