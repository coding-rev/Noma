import random


class BaseStation:
    def __init__(self, station_id):
        self.station_id = station_id
        self.connected_devices = set()

    def connect_device(self, device):
        self.connected_devices.add(device)

    def send_data_to_devices(self, data):
        for device in self.connected_devices:
            device.send_data(data)


class FiveGNetwork:
    def __init__(self):
        self.base_stations = {}

    def add_base_station(self, station_id):
        self.base_stations[station_id] = BaseStation(station_id)

    def add_device(self, device):
        # Randomly assign a base station to the device
        station_id = random.choice(list(self.base_stations.keys()))
        base_station = self.base_stations[station_id]
        base_station.connect_device(device)