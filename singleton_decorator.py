from typing import Any


class SingletonDecorator:
    
    def __init__(self, cls):
        self.cls = cls
        self.instance = None
        
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        if self.instance is None:
            self.instance = self.cls(*args, **kwds)
        return self.instance
    
    def __getattr__(self, name: str) -> Any:
        return getattr(self.cls, name)
