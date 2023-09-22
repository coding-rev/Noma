import matplotlib.pyplot as plt

def plot_signal_strength(users):
    user_ids = [user.device_id for user in users]
    signal_strengths = [user.signal_strength for user in users]

    plt.figure(figsize=(10, 6))
    plt.bar(user_ids, signal_strengths, color='skyblue')
    plt.xlabel('User Devices')
    plt.ylabel('Signal Strength (dB)')
    plt.title('Signal Strength of Connected Users')
    plt.ylim(0, 100)  # Set the y-axis range from 0 to 100 dB
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_transmitted_power(users):
    user_ids = [user.device_id for user in users]
    transmitted_powers = [user.transmitted_power for user in users]

    plt.figure(figsize=(10, 6))
    plt.bar(user_ids, transmitted_powers, color='lightcoral')
    plt.xlabel('User Devices')
    plt.ylabel('Transmitted Power (dBm)')
    plt.title('Transmitted Power Distribution Among Connected Users')
    plt.ylim(0, 30)  # Set the y-axis range from 0 to 30 dBm (max power)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

