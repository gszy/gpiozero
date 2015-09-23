from .input_devices import Button
from .output_devices import LED, Buzzer
from .devices import GPIODeviceError


class TrafficLights(object):
    def __init__(self, red=None, amber=None, green=None):
        if not all([red, amber, green]):
            raise GPIODeviceError('Red, Amber and Green pins must be provided')

        self.red = LED(red)
        self.amber = LED(amber)
        self.green = LED(green)
        self._leds = (self.red, self.amber, self.green)

    @property
    def leds(self):
        return self._leds

    def on(self):
        for led in self._leds:
            led.on()

    def off(self):
        for led in self._leds:
            led.off()

    def toggle(self):
        for led in self._leds:
            led.toggle()

    def blink(self, on_time=1, off_time=1):
        for led in self._leds:
            led.blink(on_time, off_time)


class PiTraffic(TrafficLights):
    def __init__(self):
        red, amber, green = (9, 10, 11)
        super(PiTraffic, self).__init__(red, amber, green)


class FishDish(TrafficLights):
    def __init__(self):
        red, amber, green = (9, 22, 4)
        super(FishDish, self).__init__(red, amber, green)
        self.buzzer = Buzzer(8)
        self.button = Button(pin=7, pull_up=False)
        self._all = self._leds + (self.buzzer,)

    @property
    def all(self):
        return self._all

    def on(self):
        for thing in self._all:
            thing.on()

    def off(self):
        for thing in self._all:
            thing.off()

    def toggle(self):
        for thing in self._all:
            thing.toggle()

    def lights_on(self):
        super(FishDish, self).on()

    def lights_off(self):
        super(FishDish, self).off()

    def toggle_lights(self):
        super(FishDish, self).toggle()


class TrafficHat(FishDish):
    def __init__(self):
        red, amber, green = (22, 23, 24)
        super(FishDish, self).__init__(red, amber, green)
        self.buzzer = Buzzer(5)
        self.button = Button(25)
        self._all = self._leds + (self.buzzer,)


class PiLiter(object):
    def __init__(self):
        leds = (4, 17, 27, 18, 22, 23, 24, 25)
        self._leds = tuple(LED(led) for led in leds)

    @property
    def leds(self):
        return self._leds

    def on(self):
        for led in self._leds:
            led.on()

    def off(self):
        for led in self._leds:
            led.off()

    def toggle(self):
        for led in self._leds:
            led.toggle()

    def blink(self, on_time=1, off_time=1):
        for led in self._leds:
            led.blink(on_time, off_time)