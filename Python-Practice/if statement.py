weather_condition = input('How is the weather today? ').strip().lower()

cold_weather = ['cold']
hot_weather = ['hot']
normal_response = ["normal"]

if weather_condition in cold_weather:
    print('Wear walm clothes')
    print('Have a nice day')

elif weather_condition in hot_weather:
    print('Drink plenty of water')
    print('Have a nice day')

else:
 print("It's is a lovely day")
 print('Have a nice day')