import threading
from Shared_data import Shared_data


class Event_manager:
    _instance=None
    _lock=threading.Lock()
    _publish_all=True
    _lock_sub=threading.Lock()
    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance=super().__new__(cls)
            return cls._instance
    
    def __init__(self):
        self.event_callbacks={} #key=event ,value =list of callbacks
        #self.coreEngine= Data_class.getInstance()
        self.sd=Shared_data.getInstance()
        

    
    def subscribe(self ,event ,callback):
        with self._lock_sub:
            if event not in self.event_callbacks:
                self.event_callbacks[event]=[]
            self.event_callbacks[event].append(callback)
    
    def unsubscribe(self ,event ,callback):
        if event in self.event_callbacks:
            self.event_callbacks[event].remove(callback)
            print(f"callback removed")
        if not self.event_callbacks[event]:
            del self.event_callbacks[event]
            print(f"event : {event} deleted")
    
    def publish(self ,event ,data):
        if event in self.event_callbacks:
            for callback in self.event_callbacks[event]:
                callback(event ,data)
        else :
            print(f"cannot publish ,create event :{event} for the data ")
            
    def em_loop(self):
        while True:
            data_map=self.sd.get_data()
            array_pos=data_map["raktDicke_Pos"]
            print(len(array_pos))
            self.publish("raktDicke_Pos" ,array_pos)