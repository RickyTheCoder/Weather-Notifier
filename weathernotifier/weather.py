import schedule 
import time

def get_weather(latitude, longitude):
    base_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m"
    response = requests.get(base_url)
    data = response.json()
    return data

def send_text_message(body):
    account_sid = "twilio_sid"
    auth_token = "twilio_token"
    from_phone_number = "from_phone_number"
    to_phone_number = "to_phone_number"

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=body,
        from_=from_phone_number,
        to=to_phone_number
    )

    print("Text message sent!")

def send_weather_update():
    latitude = 41.8781
    longitude = -87.6298

    weather_data = get_weather(latitude, longitude)
    temperature_fahrenheit = weather_data["hourly"]["temperature_2m"][0]
    relativehumidity = weather_data["hourly"]["relativehumidity_2m"]
    wind_speed = weather_data["hourly"]["windspeed_10m"][0]

    weather_info = (
        f"Good morning!\n"
        f"The current weather in Chicago:\n"
        f"Temperature: {temperature_fahrenheit:.2f}\n"
        f"Relative Humidity: {relative_humidity}%\n"
        f"Wind Speed; {wind_speed} m/s"
    )

    send_text_message(weather_info)

def main():
    schedule.every().day.at("06:00").do(send_weather_update)
    while True:
        schedule.run_pending
        time.sleep(1)

if __name__ == "__main__":
    main()