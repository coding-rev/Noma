class UserDevice:
    def __init__(self, device_id, distance):
        self.device_id = device_id
        self.connected = False
        self.distance = distance
        self.signal_strength = 0
        self.transmitted_power = 0  # Initialize transmitted power to 0 dBm

    def connect_to_network(self, network):
        if not self.connected:
            self.connected = True
            network.add_device(self)
            print(f"Device {self.device_id} connected to the 5G network at a distance of {self.distance} meters")

    def send_data(self, data):
        if self.connected:
            print(f"Device {self.device_id} sent data: {data}")
            return data
        else:
            print(f"Device {self.device_id} is not connected to the network")
            return None

    def measure_signal_strength(self):
        # Simulate measuring signal strength based on distance (inverse relationship)
        # Assuming signal strength decreases as distance increases
        self.signal_strength = max(0, 100 - self.distance // 10)  # Strength is at least 0 dB
        print(f"Device {self.device_id} signal strength: {self.signal_strength} dB")

    def regulate_transmitted_power(self, total_power, connected_users):
        # Simulate regulating transmitted power based on the total power available and connected users
        # Distribute power equally among connected users to ensure the total does not exceed the limit
        max_power = 30  # Maximum transmitted power in dBm
        min_power = 5  # Minimum transmitted power in dBm

        num_connected_users = len(connected_users)
        available_power = max_power * num_connected_users

        if available_power > total_power:
            adjustment_factor = total_power / available_power
        else:
            adjustment_factor = 1.0

        self.transmitted_power = max(min_power, max_power * adjustment_factor)
        print(f"Device {self.device_id} transmitted power: {self.transmitted_power} dBm")
