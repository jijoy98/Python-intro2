
def get_weather(city, api_key):
    # OpenWeatherMap API URL
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    # Send a request to the API and get the response
    response = requests.get(url)
    
    # Check if the response was successful
    if response.status_code == 200:
        weather_data = response.json()
        # Extract the temperature from the response
        temperature = weather_data['main']['temp']
        return temperature
    else:
        print("Error fetching weather data.")
        return None

def check_tshirt_suitability(temperature):
    if temperature is None:
        print("Could not get the temperature.")
        return
    
    if temperature < 10:
        print("It's too cold for a long sleeve t-shirt. You should wear something warmer!")
    elif 10 <= temperature <= 20:
        print("A long sleeve t-shirt is just right for this weather!")
    else:
        print("It's too warm for a long sleeve t-shirt. You might want to wear something lighter!")

# Example usage
def main():
    city = input("Enter your city: ")
    api_key = "YOUR_API_KEY"  # Replace with your actual API key
    
    # Get current weather temperature
    temperature = get_weather(city, api_key)
    
    # Check if a long sleeve t-shirt is appropriate
    check_tshirt_suitability(temperature)

if __name__ == "__main__":
    main()
