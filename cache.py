import json
import atexit

class Cacher(object):
    def __init__(self):
        atexit.register(self.save)
        self.data = {}
        self.load()

    def __call__(self, fn):
        def wrapper(*args, **kwargs):
            key = hash(str(args))
            if key in self.data:
                return self.data[key]

            output = fn(*args, **kwargs)
            self.data[key] = output
            return output
        return wrapper

    def save(self):
        try:
            with open(".cache.db", "w") as f:
                json.dump(self.data, f)
        except:
            pass

    def load(self):
        try:
            with open(".cache.db") as f:
                self.data = json.load(f)
        except:
            pass
