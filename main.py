from mk1.bmp280 import bmp_data
#from mk1.gps_data import GPSData
import logging
import subprocess
import threading
import time
# log to file
logging.basicConfig(
    # filename='/home/pi/strato/logs/main_log.log',
    format='%(asctime)s - %(message)s',
    datefmt='%d-%b-%y %H:%M:%S',
    level=logging.INFO)


class StratoData:
    def __init__(self):
        self.bmpa = {'temperature': 11, 'pressure': 1, 'altitude': 0}
        self.gpsdata = {'latitude': 0, 'longitude': 0, 'speed': 0, 'gps_time': 0, 'gps_date': 0,
                        'horizontal_dil': 0, 'fix_quality': 0, 'num_sats': 0, 'altitude': 0}

    def getBMPData(self):
        bmpdata = bmp_data()
        bmpdata.getAltitude()
        bmpdata.getPressure()
        bmpdata.getTemperature()
        self.bmpa = bmpdata.return_data()
        logging.info(
            f'Temperature: {self.bmpa["temperature"]}°C  Pressure: {self.bmpa["pressure"]}hPa Altitude: {self.bmpa["altitude"]}meters')

    def getGPSData(self):
        gpsdata = GPSData()
        gpsdata.get_gps_data()
        self.gpsdata = gpsdata.return_data()
        logging.info(
            f"Latitude: {self.gpsdata['latitude']} Longtitude: {self.gpsdata['longitude']} GPS Time: {self.gpsdata['gps_time']} Speed: {self.gpsdata['speed']}")


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


if __name__ == "__main__":
    # multithreading function every 3 seconds infinite times
    logging.warning("=====Program has started=====")
    weather_thread = threading.Thread(target=getWeatherData)
    gps_thread = threading.Thread(target=getGPSData)
    weather_thread.start()
    gps_thread.start()
    weather_thread.join()
    gps_thread.join()
