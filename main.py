from FiveGNetwork import FiveGNetwork
from plot import plot_signal_strength, plot_transmitted_power
from user_device import UserDevice


# Create a 5G network
network = FiveGNetwork()

# Add base stations
network.add_base_station("BS1")

# Create user devices with distances and connect them to the network
device1 = UserDevice("Device1", distance=1)
device1.connect_to_network(network)
device1.measure_signal_strength()

device2 = UserDevice("Device2", distance=50)
device2.connect_to_network(network)
device2.measure_signal_strength()

device3 = UserDevice("Device3", distance=100)
device3.connect_to_network(network)
device3.measure_signal_strength()

device4 = UserDevice("Device4", distance=200)
device4.connect_to_network(network)
device4.measure_signal_strength()

device5 = UserDevice("Device5", distance=300)
device5.connect_to_network(network)
device5.measure_signal_strength()

# Set the total transmitted power limit
total_transmitted_power_limit = 100  # dBm

# Adjust transmitted power for all connected devices (including the new one)
total_connected_devices = [device1, device2, device3, device4, device5]

device1.regulate_transmitted_power(total_transmitted_power_limit, total_connected_devices)
device2.regulate_transmitted_power(total_transmitted_power_limit, total_connected_devices)
device3.regulate_transmitted_power(total_transmitted_power_limit, total_connected_devices)
device4.regulate_transmitted_power(total_transmitted_power_limit, total_connected_devices)
device5.regulate_transmitted_power(total_transmitted_power_limit, total_connected_devices)
# Plot signal strength and transmitted power for all connected users
plot_signal_strength(total_connected_devices)
plot_transmitted_power(total_connected_devices)