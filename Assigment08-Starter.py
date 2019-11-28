# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# QKuang,11.27.2019,Created started script
# QKuang,11.27.2019,Added pseudo-code to start assignment 8
# QKuang,11.27.2019,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

import os
# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []
dicRow = {}


class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        QKuang,11.27.2019,Created Class
        QKuang,11.27.2019,Modified code to complete assignment 8
    """

    # -- Constructor --
    def __init__(self, products_name, products_price):
        # - - Attributes - -
        self.__product_name = products_name
        self.__product_price = products_price

    # -- Properties --
    @property
    def product_name(self):
        return str(self.__product_name)

    @product_name.setter
    def product_name(self, value):
        if not str(value).isnumeric():
            self.__product_name = value
        else:
            raise Exception("Names cannot be numbers!")

    @property
    def product_price(self):
        return float(self.__product_price)

    @product_price.setter
    def product_price(self, value):
        if type(value) == float:
            self.__product_price = value
        else:
            raise Exception("Price must be float numbers!")
# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects): save data from a list of product objects to a file

        read_data_from_file(file_name): read data from a file to a list of product objects


    changelog: (When,Who,What)
        QKuang,11.27.2019,Created Class
        QKuang,11.27.2019,Modified code to complete assignment 8
    """

    @staticmethod
    def save_data_to_file(file_name, list_of_product_objects):
        """
        Desc - Write a list of data into a file

        :param file_name: (string) with name of file:
        :param list_of_product_objects: (list) you want filled with file data:
        """
        objfile = open(file_name, 'w')
        for row in list_of_product_objects:
            objfile.write(row.product_name + "," + str(row.product_price) + "\n")
        objfile.close()

    @staticmethod
    def read_data_from_file(file_name):
        """
        Desc - Reads data from a file into a list of product objects

        :param file_name: (string) with name of file:
        :param lstOfProductObjects: (list) you want filled with file data:
        :return: (list) of product objects
        """
        file = open(file_name, 'r')
        for line in file:
            data = line.split(",")
            newProduct = Product(data[0].strip(), data[1].strip())
            lstOfProductObjects.append(newProduct)
        file.close()
        return lstOfProductObjects

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:

    """perform Input and Output

    methods:
        static: OutputMenuItems() -> Show the menu choice to the user

                InputMenuChoice() -> Get the menu choice from the user

                ShowCurrentItemsInList() -> Show the current data from the file to the user

                InputNewTaskAndPriority() -> Get the product data from the user

    changelog: (When,Who,What)
        QKuang,11.27.2019,Created Class
        QKuang,11.27.2019,Modified code to complete assignment 8

    """

    @staticmethod
    def OutputMenuItems():
        """  Display a menu of choices to the user
        :return: nothing
        """
        print('''
        Menu of Options
        1) Show current data
        2) Add a new item.
        3) Save Data to File
        4) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def InputMenuChoice():
        """ Gets the menu choice from a user
        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def ShowCurrentItemsInList(list_of_rows):
        """ Shows the current items in the list of product objects

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current items ToDo are: *******")
        for row in list_of_rows:
            print(row.product_name + " (" + str(row.product_price) + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def InputNewTaskAndPriority():
        """  Ask the user to input new task and it's priority
         :return: strings
         """
        product_name = input("What is the product's name? - ").strip()  # Get product's name from user
        product_price = input("How much is the product? - ").strip()  # Get product's price from user
        print()  # Add an extra line for looks
        return product_name, product_price
# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
# Load data from file into a list of product objects when script starts
if os.path.exists(strFileName):
    FileProcessor.read_data_from_file(strFileName)  # read file data
# Show user a menu of options
while(True):
    IO.OutputMenuItems()
# Get user's menu option choice
    strChoice = IO.InputMenuChoice()
    # Show user current data in the list of product objects
    if (strChoice.strip() == '1'):
        IO.ShowCurrentItemsInList(lstOfProductObjects)  # Show current data in the list
        continue  # to show the menu
    # Let user add data to the list of product objects
    elif (strChoice.strip() == '2'):
        product_name, product_price = IO.InputNewTaskAndPriority()
        lstOfProductObjects.append(Product(product_name, product_price))
        IO.ShowCurrentItemsInList(lstOfProductObjects)  # Show current data in the list
        continue  # to show the menu

    # let user save current data to file and exit program
    elif (strChoice == '3'):

        # Step 3.4.a - Show the current items in the table
        IO.ShowCurrentItemsInList(lstOfProductObjects)  # Show current data in the list

        # Step 3.4.b - Ask if user if they want save that data
        if ("y" == str(input("Save this data to file? (y/n) - ")).strip().lower()):  # Double-check with user

            FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)

            input("Data saved to file! Press the [Enter] key to return to menu.")
        else:  # Let the user know the data was not saved
            input("New data was NOT Saved, but previous data still exists! Press the [Enter] key to return to menu.")
        continue  # to show the menu
    elif (strChoice == '4'):
        break   # and Exit

# Main Body of Script  ---------------------------------------------------- #

