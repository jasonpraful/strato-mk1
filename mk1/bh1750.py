import board
import adafruit_bh1750
i2c = board.I2C()
sensor = adafruit_bh1750.BH1750(i2c, address=0x23)


class bh1750_data:
    def __init___(self, lux):
        lux = 0

    def get_luminosity(self):
        self.lux = sensor.lux

    def return_data(self):
        return {'lux': self.lux}
