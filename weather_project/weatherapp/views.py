from django.shortcuts import render
import requests

def index(request):
    weather_data = {}
    error_message = None
    
    if request.method == 'POST':
        city = request.POST.get('city')  # Get the city from the form input
        api_key = '5e8f288e6b356528c801e1d60767dc58'  # Your API key
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        
        try:
            response = requests.get(url)
            data = response.json()

            if data.get('cod') == 200:  # Check if API returned success
                weather_data = {
                    'city': data['name'],
                    'temperature': data['main']['temp'],
                    'description': data['weather'][0]['description'],
                    'icon': data['weather'][0]['icon']
                }
            else:
                error_message = "City not found or API error. Please try again."
        except requests.exceptions.RequestException as e:
            error_message = f"An error occurred: {e}"

    return render(request, 'weatherapp/index.html', {'weather_data': weather_data, 'error_message': error_message})
