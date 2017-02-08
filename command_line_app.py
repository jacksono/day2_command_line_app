import requests #the requests library needs to be installed first, use pip install requests
import json
import sys
import pprint

def curren_city_weather(city_id, key):
    """
    Retrieves current weather data for a city from the openweathermap API
    Args:
        city_id: the city id as set in the openweathermap city ID list
        key: the API key
        examples: for Nairobi, city_id = 184742
                  my personal key is 69e7171295188958144216fbaef8f988

    Returns:
        Returns a json format of current weather data for the city with city_id

    """
    try:
        api_url = "http://api.openweathermap.org/data/2.5/weather?id=%s&appid=%s" %(city_id,key)
                    
        response = requests.get(api_url)
        if response.status_code == 401:#Check for valid key
        	print("Invalid API key")       	
        elif response.status_code == 200:#converting response to json
        	weather_data = json.loads(response.text)
        return weather_data

    except(UnboundLocalError):
        return "Please check the API key and/or city id entered"

    
def main(city_id, key):
    '''
        Prints out the output form the public_api function in a pretty print format
    '''
    pprint.pprint(curren_city_weather(city_id, key))


if __name__ == '__main__':
    '''
        Runs the main() function from the command line with and passes to it 2 command line
        arguments:
        sys.argv[1] corresponds to city_id argument of main()
        sys.argv[2] corresponds to key argument of main()
    '''
    try:
        main(sys.argv[1], sys.argv[2])
    except(IndexError):
        print('Please enter the city id and API key as command line arguments after the script file name')

