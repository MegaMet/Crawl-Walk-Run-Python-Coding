#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import os
from datetime import datetime as dt
from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager


data_manager = DataManager()
flight_data = FlightData()
flight_search = FlightSearch()
notification_manager = NotificationManager()

flight_search.find_flight()