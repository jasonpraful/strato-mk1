# get gps data from neo 6m raspberry pi
import pynmea2
import serial
import time
import logging
from datetime import datetime
serial_port = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=0.5)
log = logging.getLogger('main.gpsdata')
gps_hdlr = logging.FileHandler(
    f'/home/pi/strato/gps/gps_data{datetime.today()}.log', mode="w")
log.addHandler(gps_hdlr)
log.setLevel(logging.DEBUG)


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
        self.lat_dir = 'NA'
        self.lon_dir = 'NA' 
        self.type = "NONE"

    def get_gps_data(self):
        dataout = pynmea2.NMEAStreamReader()
        newdata = serial_port.readline().decode('ascii', errors='replace')
        if newdata[0:6] == '$GPRMC':
            newmsg = pynmea2.parse(newdata)
            self.type = "GPRMC"
            self.lat = newmsg.latitude
            self.lon = newmsg.longitude
            self.speed = newmsg.spd_over_grnd
            self.gps_time = newmsg.timestamp
            self.lat_dir = newmsg.lat_dir
            self.lon_dir = newmsg.lon_dir
            #self.altitude = newmsg.altitude
            #self.satellites = newmsg.num_sats
            #self.hdop = newmsg.horizontal_dil
            self.gps_date = newmsg.datestamp
            #self.fix_quality = newmsg.gps_qual
        if newdata[0:6] == "$GPGGA":
            print(newdata)
            newmsg = pynmea2.parse(newdata)
            self.type = "GPGGA"
            self.lat = newmsg.latitude
            self.lon = newmsg.longitude
            self.lat_dir = newmsg.lat_dir
            self.lon_dir = newmsg.lon_dir
            self.gps_time = newmsg.timestamp
            self.altitude = newmsg.altitude
            self.satellites = newmsg.num_sats
            self.hdop = newmsg.horizontal_dil
            self.fix_quality = newmsg.gps_qual

    def return_data(self):
        log.debug({
            'latitude': self.lat if self.lat != 0 else "NA",
            'longitude': self.lon if self.lon != 0 else "NA",
            'speed': self.speed if self.speed != 0 else "NA",
            'altitude': self.altitude if self.altitude != 0 else "NA",
            'horizontal_dil': self.hdop if self.hdop != 0 else "NA",
            'fix_quality': self.fix_quality if self.fix_quality != 0 else "NA",
            'num_sats': self.num_sats if self.num_sats != 0 else "NA",
            'gps_time': self.gps_time if self.gps_time != 0 else "NA",
            'gps_date': self.gps_date if self.gps_date != 0 else "NA",
            'lat_dir': self.lat_dir,
            'lon_dir': self.lon_dir,
            'type': self.type,
        })
        return {
            'latitude': self.lat if self.lat != 0 else "NA",
            'longitude': self.lon if self.lon != 0 else "NA",
            'speed': self.speed if self.speed != 0 else "NA",
            'altitude': self.altitude if self.altitude != 0 else "NA",
            'horizontal_dil': self.hdop if self.hdop != 0 else "NA",
            'fix_quality': self.fix_quality if self.fix_quality != 0 else "NA",
            'num_sats': self.num_sats if self.num_sats != 0 else "NA",
            'gps_time': self.gps_time if self.gps_time != 0 else "NA",
            'gps_date': self.gps_date if self.gps_date != 0 else "NA",
            'lat_dir': self.lat_dir,
            'lon_dir': self.lon_dir,
            'type': self.type,
        }
