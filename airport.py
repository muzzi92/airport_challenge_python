class Airport():
    hanger = []

    def land(self, plane):
        self.hanger.append(plane)

    def take_off(self, plane):
        self.hanger.remove(plane)
