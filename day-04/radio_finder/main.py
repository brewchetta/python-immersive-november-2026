from api import APIConnector

# jazz_stations = APIConnector(station_type="jazz")

# FEATURE LIST

# menu - 1, 2, 3, etc.

# search by station type

# search by country code

# automatic retry on api failure

# users may favorite stations

# users may see their favorited stations

# sort stations by name / type / whatever

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
        while self.running == True:
            self.main_menu_display()
            user_input = input(">>> ")
            if user_input == "1":
                self.search_by_type()
            elif user_input == "2":
                self.search_by_country()
            elif user_input == "3":
                self.view_favorites
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

    def search_by_type(self):
        pass
        # search by user input / chosen station type

    def search_by_country(self):
        pass

    def view_favorites(self):
        pass


# initialize the app
app = App()