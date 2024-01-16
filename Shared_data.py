import queue
import threading


class Shared_data:
    _instance=None
    _lock=threading.Lock()
    
    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance=super().__new__(cls)
            return cls._instance
    
    def __init__(self):
        self.shared_queue=queue.Queue(maxsize=5)
        
    @classmethod
    def getInstance(cls):
        return cls()
    
    def put_data(self ,data):
        print("put 1: ", self.shared_queue.qsize())
        self.shared_queue.put(data ,block=True)
        print("put 2: ", self.shared_queue.qsize())
    
    def get_data(self):
        print("get 1: ", self.shared_queue.qsize())
        data = self.shared_queue.get(block=True)
        print("get 2: ", self.shared_queue.qsize())
        return data