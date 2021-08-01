from mk1.bmp280 import bmp_data
from mk1.bh1750 import bh1750_data
from mk1.gps_data import GPSData
import logging
import subprocess
import threading
import time
from datetime import datetime
log = logging.getLogger('main')
hdlr = logging.FileHandler(
    '/home/pi/strato/logs/main_log' + str(datetime.today()) + '.log')
formatter = logging.Formatter('%(asctime)s - %(message)s')
hdlr.setFormatter(formatter)
log.addHandler(hdlr)
log.setLevel(logging.INFO)


class StratoData:
    def __init__(self):
        self.main_logger = logging.getLogger('main.main')
        self.main_hdlr = logging.FileHandler(
            f'/home/pi/strato/main/main-{datetime.today()}.log', mode="w")
        self.main_logger.addHandler(self.main_hdlr)
        self.main_logger.setLevel(logging.INFO)
        self.bmpa = {'temperature': 11, 'pressure': 1, 'altitude': 0}
        self.gpsdata = {'latitude': 0, 'longitude': 0, 'speed': 0, 'gps_time': 0, 'gps_date': 0,
                        'horizontal_dil': 0, 'fix_quality': 0, 'num_sats': 0, 'altitude': 0}
        self.lux = {'lux': 0}

    def getBMPData(self):
        bmpdata = bmp_data()
        bmpdata.getAltitude()
        bmpdata.getPressure()
        bmpdata.getTemperature()
        self.bmpa = bmpdata.return_data()
        self.main_logger.info(
            f'Temperature: {self.bmpa["temperature"]}°C  Pressure: {self.bmpa["pressure"]}hPa Altitude: {self.bmpa["altitude"]}meters')

    def getGPSData(self):
        gpsdata = GPSData()
        gpsdata.get_gps_data()
        self.gpsdata = gpsdata.return_data()
        print(self.gpsdata)
        if self.gpsdata['type'] == 'NONE':
            pass
        else:
            self.main_logger.info(
                f"Type: {self.gpsdata['type']} Latitude: {self.gpsdata['latitude']} Longtitude: {self.gpsdata['longitude']} GPS Time: {self.gpsdata['gps_time']} GPS Date: {self.gpsdata['gps_date']} Speed: {self.gpsdata['speed']} GPS Altitude: {self.gpsdata['altitude']}")

    def getBH1750Data(self):
        bhp175 = bh1750_data()
        bhp175.get_luminosity()
        self.lux = bhp175.return_data()
        self.main_logger.info(f"Lux: {self.lux['lux']}")


def getWeatherData():
    strato = StratoData()
    while True:
        strato.getBMPData()
        time.sleep(3)


def getGPSData():
    strato = StratoData()
    while True:
        strato.getGPSData()
        time.sleep(3)


def getLuminousData():
    strato = StratoData()
    while True:
        strato.getBH1750Data()
        time.sleep(3)


if __name__ == "__main__":
    log.warning("=====Program has started=====")
    weather_thread = threading.Thread(target=getWeatherData)
    gps_thread = threading.Thread(target=getGPSData)
    luminous_thread = threading.Thread(target=getLuminousData)
    weather_thread.start()
    gps_thread.start()
    luminous_thread.start()
    weather_thread.join()
    gps_thread.join()
    luminous_thread.join()
