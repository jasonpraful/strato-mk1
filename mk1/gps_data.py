# get gps data from neo 6m raspberry pi
import pynmea2
import serial
import time
import logging
# log to file
logging.basicConfig(filename='/home/pi/strato/gps_data.log',
                    format='%(asctime)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)
# initialize serial port
serial_port = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=0.5)


class GPSData:
    def __init__(self):
        self.lat = 0
        self.lon = 0
        self.speed = 0
        self.altitude = 0
        self.hdop = 0
        self.fix_quality = 0
        self.num_sats = 0
        self.gps_time = 0
        self.gps_date = 0

    def get_gps_data(self):
        dataout = pynmea2.NMEAStreamReader()
        newdata = serial_port.readline()
        if newdata[0:6] == '$GPGGA':
            newmsg = pynmea2.parse(newdata)
            self.lat = newmsg.latitude
            self.lon = newmsg.longitude
            self.speed = newmsg.speed
            self.gps_time = newmsg.timestamp
            self.altitude = newmsg.altitude
            self.satellites = newmsg.num_sats
            self.hdop = newmsg.horizontal_dil
            self.gps_date = newmsg.datestamp
            self.fix_quality = newmsg.gps_qual

    def return_data(self):
        logging.info(self)
        return {
            'latitude': self.lat,
            'longitude': self.lon,
            'speed': self.speed,
            'altitude': self.altitude,
            'horizontal_dil': self.hdop,
            'fix_quality': self.fix_quality,
            'num_sats': self.num_sats,
            'gps_time': self.gps_time,
            'gps_date': self.gps_date,
        }
