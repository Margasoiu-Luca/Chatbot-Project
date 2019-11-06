import requests

def chatbot():
    print("Hello i am ChatBot. I can forecast the weather, tell the time")
    print(" anywhere in the world and give you sports fixtures and news.")
    command = input("What would you like? ").lower()
    location = input("Enter Location ")
    webadd = "http://api.openweathermap.org/data/2.5/weather?appid=9777aeb5531c2d51d999a49783fb454d&q="
    url = webadd+location
    data = requests.get(url).json()
    description = data["weather"][0]["description"]
    temperature = data["main"]["temp"]
    temperature2 = round((temperature-273.15) ,2)

    wordlist = command.split() 
    for command in wordlist:
        if command == "weather":
            print("In" ,location, ", the weather is", description, "with temperatures of" ,temperature2,"degrees Celcius")

    def play_again():
        choice = input("Would you like anything else? ('y' or 'n') ")
        if choice == 'y':
            chatbot()
        elif choice == 'n':
            print("Okay, Goodbye!")
        else:
            print("Your input is not recognised. Please enter 'y' or 'n'.")
            play_again()
    play_again()
chatbot()
