import python_weather
import asyncio

async def get_weather():
    # Create the client (defaults to metric units)
    async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
        # Fetch weather for a city (e.g., New York)
        weather = await client.get('New York')
        print(f"Temperature: {weather.temperature}°F")
        for daily in weather.daily_forecasts:
            print(daily)
            for hourly in daily.hourly_forecasts:
                print(f" --> {hourly!r}")

if __name__ == '__main__':
    asyncio.run(get_weather())
