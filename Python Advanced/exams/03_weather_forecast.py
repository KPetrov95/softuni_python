def forecast(*args):
    weather_dict = {}
    for city, weather in args:
        weather_dict[city] = weather
    sorted_dict = sorted(weather_dict.items(), key=lambda x: x[0])
    cloudy = ''
    sunny = ''
    rainy = ''
    for city, weather in sorted_dict:
        if weather == 'Cloudy':
            cloudy += f'{city} - {weather}\n'
        elif weather == 'Sunny':
            sunny += f'{city} - {weather}\n'
        elif weather == 'Rainy':
            rainy += f'{city} - {weather}\n'
    return sunny + cloudy + rainy

print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))


