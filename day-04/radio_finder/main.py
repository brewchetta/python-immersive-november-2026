#!/usr/bin/env python
# shebang - can run with the python interpreter without typing `python main.py` in the terminal

from api import APIConnector

class App:

    favorites = []
    running = True

    def __init__(self):
        # welcome message and go to the main menu
        print("Welcome to Radio Finder!")
        print("Your go to app for finding radio stations...")
        self.main_menu()

    def main_menu(self):
        # input a number and go to a submenu
        # while running is True, else the main menu / program will end
        while self.running == True:
            self.main_menu_display()
            user_input = input(">>> ")
            if user_input == "1":
                self.search_by(station_type=True)
            elif user_input == "2":
                self.search_by(countrycode=True)
            elif user_input == "3":
                self.view_favorites()
            elif user_input == "4":
                print("See ya later alligator")
                self.running = False
            else:
                print("Invalid input, please try again!")


    def main_menu_display(self):
        # show the menu options
        print("-----Main Menu-----")
        print("1. Search by station type")
        print("2. Search by country code")
        print("3. See your favorites")
        print("4. Exit")

    def search_by(self, station_type=None, countrycode=None):
        # search by user input / chosen station type
        user_input = input(f"What { "type of station" if station_type else "country" } are you searching for?\n>>> ").strip().lower()

        if not user_input:
            return None

        api_result = None
        if station_type:
            api_result = APIConnector(station_type=user_input)
        elif countrycode:
            api_result = APIConnector(countrycode=user_input)

        # retry if invalid response
        while not api_result.response and api_result.attempts < 5:
            print("Retrying the API...")
            api_result.retry()

        # if valid response, show stations and give favoriting option
        if api_result.response:
            stations = api_result.response.json()
            self.print_radio_stations( stations )
            user_input = input("Choose a station to favorite\n>>> ")
            valid_inputs = ["1", "2", "3", "4", "5"]
            if user_input in valid_inputs:
                index = int(user_input) - 1
                chosen_station = stations[index]
                self.favorites.append( chosen_station )
                print(f"{chosen_station['name']} has been added as a favorite!")
            else:
                print("No choice made, sending you back to the menu...")
        else:
            print("Unable to connect to the API...")

    def print_radio_stations(self, stations):
        counter = 1
        for s in stations:
            print("-------------------------------")
            print(f"#{counter}")
            print(f"Station Name: {s['name']}")
            print(f"Country: {s['country']}")
            print(f"Homepage: {s['homepage']}")
            print(f"Most recently available: {s['lastchecktime']}")
            print("-------------------------------")
            counter += 1

    def view_favorites(self):
        print("-----Favorites-----")
        # move on if no favorites
        if not self.favorites:
            print("You haven't found any favorites yet, get out there and start searching!")
        else:
            # print the favorited stations and get user input
            self.print_radio_stations( self.favorites )
            user_input = input("Which station would you like to remove?\nType 'exit' to go back to main menu\n>>> ")
            try:
                # try to parse the input into an integer and remove it if we can
                index = int(user_input) - 1
                if 0 <= index < len( self.favorites ):
                    self.favorites.pop( index )
                else:
                    print("Invalid choice, please try again")
            except:
                # if not an integer, check to see if the user input is exit
                if user_input.lower() == "exit":
                    return None
                else:
                    print("Invalid choice, please try again")



# initialize the app
app = App()