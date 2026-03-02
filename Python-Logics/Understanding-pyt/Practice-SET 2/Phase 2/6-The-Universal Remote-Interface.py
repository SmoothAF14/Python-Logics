from abc import ABC, abstractmethod
class device(ABC):
    @abstractmethod
    def turn_on(ABC):
        pass
class TV(device):
    def turn_on(self):
        print("TV is turned on")
class AC(device):
    def turn_on(self):
        print("AC is turned on")
class RemoteControl:
    def activate(self, device):
        device.turn_on()
remote = RemoteControl()
remote.activate(TV())
remote.activate(AC())
