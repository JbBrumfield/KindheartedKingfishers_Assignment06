# File Name : stadium.py
# Student Name: Liam Vasey
# email:  vaseylh@mail.uc.edu
# Assignment Number: Assignment 06
# Due Date:   02/27/2025
# Course #/Section:   IS4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  This assingment requires each group member to create a class representing a real world thing to model, which we chose a football game.

# Brief Description of what this module does. This module shows us how to create classes using init, str, and repr methods, while also using getters and setters
# Citations: https://www.geeksforgeeks.org/__init__-in-python/  , https://stackoverflow.com/questions/36267794/meaning-of-a-function-str


class Stadium:
    def __init__(self, name: str, capacity: int, location: str):
        """
        Initializes a Stadium object with a name, capacity, and location.
        
        @param name: Name of the stadium
        @param capacity: Seating capacity of the stadium
        @param location: Location of the stadium
        """
        self._name = name
        self._capacity = capacity
        self._location = location
        self._current_event = None  # Tracks the event currently being hosted

    def __str__(self):
        """
        Returns a user string representation of the stadium.
        """
        return f"Stadium(name={self._name}, capacity={self._capacity}, location={self._location}, current event={self._current_event})"

    def __repr__(self):
        """
        Returns a formal string representation of the stadium.
        """
        return f"Stadium('{self._name}', {self._capacity}, '{self._location}')"

    
    def capacity(self):
        """Getter for stadium capacity."""
        return self._capacity

    
    def capacity(self, new_capacity):
        """Setter for stadium capacity."""
        if new_capacity > 0:
            self._capacity = new_capacity
        else:
            raise ValueError("Capacity must be greater than zero.")

    def host_event(self, event_name: str):
        """
        Simulates hosting an event at the stadium.
        
        :param event_name: Name of the event to be hosted
        """
        self._current_event = event_name
        print(f"{self._name} is now hosting {event_name}.")



