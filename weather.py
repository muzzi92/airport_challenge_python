import random

class Weather:

    def forecast(self, num = None):
        if num is None: num = random.randint(1, 2)
        return 'stormy' if num == 1 else 'sunny'
