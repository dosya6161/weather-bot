BOT_API_TOKEN = '5481444138:AAHbMsAK0irV_qyXaVGVqfu3uHAPr15gL5Y'
WEATHER_API_KEY = '3f5b6f38338af786ffb7d62efdb272c1'

CURRENT_WEATHER_API_CALL = (
        'https://api.openweathermap.org/data/2.5/weather?'
        'lat={latitude}&lon={longitude}&'
        'appid=' + WEATHER_API_KEY + '&units=metric'
)
