# bmp280 i2c raspberry pi
#import board
#import adafruit_bmp280
#i2c = board.I2C()
#sensor = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)


class bmp_data:
    def __init___(self, temperature, pressure, altitude):
        temperature = 0
        pressure = 0
        altitude = 0

    def getTemperature(self):
        #self.temperature = sensor.temperature
        self.temperature = 12

    def getPressure(self):
        #self.pressure = sensor.pressure
        self.pressure = 991

    def getAltitude(self):
        #sensor.sea_level_pressure = 1013.25
        #self.altitude = sensor.altitude
        self.altitude = 121

    def return_data(self):
        return {'temperature': self.temperature, 'pressure': self.pressure, 'altitude': self.altitude}