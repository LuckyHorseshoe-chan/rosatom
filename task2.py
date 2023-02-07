class CapturedStep:
    def __init__(self, callback, step):
        self.callback = callback
        self.step = step

    def __call__(self):
        return self.callback(self.step)


def create_handlers(callback):
    return [CapturedStep(callback, step) for step in range(5)]


def execute_handlers(handlers):
    for handler in handlers:
        handler()


execute_handlers(create_handlers(lambda a : print(a*2)))