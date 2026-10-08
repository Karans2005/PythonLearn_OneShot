import datetime
import requests


class WeatherApp:

    def __init__(self):
        # OpenWeatherMap ki free demo API URL
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"
        # Demo API Key (Professional use ke liye apni openweathermap.org se le sakte hain)
        self.api_key = "b6907d289e10d714a6e88b30761fae22"

    def get_weather(self, city_name):
        """API se weather data fetch karne ke liye (API + JSON + Error Handling)"""
        params = {
            "q": city_name,
            "appid": self.api_key,
            "units": "metric",  # Temperature Celsius me lene ke liye
        }

        try:
            response = requests.get(self.base_url, params=params)

            # Agar city nahi mili ya koi aur HTTP error aaya
            if response.status_code == 404:
                print(
                    f"\n❌ Error: '{city_name}' naam ki city nahi mili! Name check karein."
                )
                return None
            elif response.status_code != 200:
                print(
                    f"\n❌ API Error: Something went wrong (Status Code: {response.status_code})"
                )
                return None

            # JSON response parse karna
            data = response.json()
            return data

        except requests.exceptions.ConnectionError:
            print("\n❌ Internet Error: Internet connection check karein!")
            return None
        except Exception as e:
            print(f"\n❌ Unexpected Error: {e}")
            return None

    def save_to_history(self, city, temp, condition):
        """Search history ko text file me save karna (File Handling)"""
        try:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open("weather_history.txt", "a") as file:
                file.write(
                    f"[{timestamp}] City: {city} | Temp: {temp}°C | Condition: {condition}\n"
                )
        except Exception as e:
            print(f"History save karne me error aaya: {e}")

    def display_weather(self, data):
        """Fetched data ko clean format me print karna"""
        city = data["name"]
        country = data["sys"]["country"]
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"].title()

        print("\n" + "=" * 35)
        print(f"🌍 WEATHER REPORT: {city.upper()}, {country}")
        print("=" * 35)
        print(f"🌡️  Temperature : {temp}°C (Feels like: {feels_like}°C)")
        print(f"☁️  Condition   : {condition}")
        print(f"💧 Humidity    : {humidity}%")
        print("=" * 35)

        # History file me save karna
        self.save_to_history(city, temp, condition)
        print("✅ Search History me save ho gaya!")


# --- MAIN EXECUTION ---
if __name__ == "__main__":
    app = WeatherApp()

    print("🌤️ WELCOME TO PYTHON WEATHER APP")

    while True:
        city_input = input(
            "\nCity ka naam likhein (ya 'exit' karke bahar aayein): "
        ).strip()

        if city_input.lower() == "exit":
            print("\nDhanyawad! App band ho raha hai... 👋")
            break

        if not city_input:
            print("Pehle city ka naam toh enter kijiye!")
            continue

        # Weather fetch karo aur display karo
        weather_data = app.get_weather(city_input)
        if weather_data:
            app.display_weather(weather_data)