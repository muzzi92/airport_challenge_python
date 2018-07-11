from weather import Weather

class Airport():
    hanger = []

    def land(self, plane):
        self.hanger.append(plane)

    def take_off(self, plane, weather = Weather().forecast()):
        if weather == 'stormy' : raise RuntimeError('Cannot take off in storm')
        self.hanger.remove(plane)
