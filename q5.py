
weather_data = [
    {"date": "2024-08-01", "max_temp": 33, "min_temp": 20, "humidity": 65},
    {"date": "2024-08-02", "max_temp": 32, "min_temp": 22, "humidity": 62},
    {"date": "2024-08-03", "max_temp": 34, "min_temp": 23, "humidity": 56},
    {"date": "2024-08-04", "max_temp": 28, "min_temp": 24, "humidity": 53},
    {"date": "2024-08-05", "max_temp": 34, "min_temp": 21, "humidity": 49},
    {"date": "2024-08-06", "max_temp": 37, "min_temp": 23, "humidity": 47},
    {"date": "2024-08-07", "max_temp": 26, "min_temp": 19, "humidity": 73},
    {"date": "2024-08-08", "max_temp": 31, "min_temp": 18, "humidity": 72},
    {"date": "2024-08-09", "max_temp": 28, "min_temp": 15, "humidity": 86},
    {"date": "2024-08-10", "max_temp": 30, "min_temp": 24, "humidity": 61}
]

def find_extreme_temperatures(data):
    max_temp = max(data, key=lambda x: x['max_temp'])['max_temp']
    min_temp = min(data, key=lambda x: x['min_temp'])['min_temp']
    return max_temp, min_temp

def count_days_above_30(data):
    count = sum(1 for day in data if day['max_temp'] > 30)
    return count

def average_humidity(data):
    total_humidity = sum(day['humidity'] for day in data)
    return total_humidity / len(data)

def main():
    max_temp, min_temp = find_extreme_temperatures(weather_data)
    print(f"Highest Temperature: {max_temp}°C")
    print(f"Lowest Temperature: {min_temp}°C")

    days_above_30 = count_days_above_30(weather_data)
    print(f"Number of days with temperatures above 30°C: {days_above_30}")

    avg_humidity = average_humidity(weather_data)
    print(f"Average Humidity: {avg_humidity}%")

if __name__ == "__main__":
    main()