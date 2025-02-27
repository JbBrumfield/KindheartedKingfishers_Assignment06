# File Name : player.py
# Student Name: Daquan Daniels 
# email:  Danieldu@mail.uc.edu
# Assignment Number: Assignment 06
# Due Date:   02/27/2025
# Course #/Section:   IS4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment: collaborate with group members to create a class that models something from the real world 

# Brief Description of what this module does: defines the player class, which represents football players with attributes like name, position, number, and age.
# Citations: https://labex.io/tutorials/python-how-to-use-init-str-and-repr-methods-in-python-415189

# Anything else that's relevant:N/A

class Player:
    def __init__(self, name, position, number, age):
        """
        Initializes a Player object with the given name, position, number, and age.
        
        @param name: str, the name of the player
        @param position: str, the position the player plays
        @param number: int, the jersey number of the player
        @param age: int, the age of the player
        """
        self._name = name
        self._position = position
        self._number = number
        self._age = age

    def get_name(self):
        """
        Returns the name of the player.
        
        @return: str, the name of the player
        """
        return self._name

    def get_position(self):
        """
        Returns the position of the player.
        
        @return: str, the position the player plays
        """
        return self._position

    def get_number(self):
        """
        Returns the jersey number of the player.
        
        @return: int, the jersey number of the player
        """
        return self._number

    def get_age(self):
        """
        Returns the age of the player.
        
        @return: int, the age of the player
        """
        return self._age

    def set_position(self, new_position):
        """
        Sets a new position for the player.
        
        @param new_position: str, the new position of the player
        """
        self._position = new_position

    def set_number(self, new_number):
        """
        Sets a new jersey number for the player.
        
        @param new_number: int, the new jersey number of the player
        """
        self._number = new_number

    def set_age(self, new_age):
        """
        Sets a new age for the player.
        
        @param new_age: int, the new age of the player
        """
        self._age = new_age

    def update_position(self, new_position):
        """
        Updates the player's position and prints a message about the change.
        
        @param new_position: str, the new position the player will play
        """
        print(f"{self._name} is now playing as {new_position}.")
        self._position = new_position

    def __str__(self):
        """
        Returns a formatted string representation of the player.
        
        @return: str, a string that shows the player's name, position, number, and age
        """
        return f"Player(Name: {self._name}, Position: {self._position}, Number: {self._number}, Age: {self._age})"

    def __repr__(self):
        """
        Returns a detailed string representation of the player, useful for debugging.
        
        @return: str, a detailed string that could be used to recreate the player object
        """
        return f"Player('{self._name}', '{self._position}', {self._number}, {self._age})"

