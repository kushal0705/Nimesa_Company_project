import get_presure
import get_weather_data
import get_weather
import get_windspeed

def main():
    weather_data = get_weather_data.get_weather_data()
    if not weather_data:
        print("Exiting program.")
        return

    while True:
        print("\n1. Get weather\n2. Get Wind Speed\n3. Get Pressure\n0. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            date = input("Enter the date (e.g., 2019-03-31): ")
            temp = get_weather.get_weather_by_date(weather_data, date)
            if temp is not None:
                print(f"Temperature on {date}: {temp} K")
            else:
                print("Weather data not found for the given date.")
        elif choice == 2:
            date = input("Enter the date (e.g., 2019-03-31): ")
            wind_speed = get_windspeed.get_wind_speed_by_date(weather_data, date)
            if wind_speed is not None:
                print(f"Wind Speed on {date}: {wind_speed} m/s")
            else:
                print("Weather data not found for the given date.")
        elif choice == 3:
            date = input("Enter the date (e.g., 2019-03-31): ")
            pressure = get_presure.get_pressure_by_date(weather_data, date)
            if pressure is not None:
                print(f"Pressure on {date}: {pressure} hPa")
            else:
                print("Weather data not found for the given date.")
        elif choice == 0:
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

main()
