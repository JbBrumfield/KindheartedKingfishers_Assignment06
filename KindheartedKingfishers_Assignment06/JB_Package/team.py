# File Name : team.py
# Student Name: Jacob Brumfield
# email:  brumfijb@mail.uc.edu
# Assignment Number: Assignment 06
# Due Date:   2/27/2025
# Course #/Section:   IS4010 001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  Work together with 3 classmates to produce a model of something that has meaning to all of us. Include init, str, and repr methods in each class.

# Brief Description of what this module does: The Team class allows you to manage a teams roster, coach, and add/remove players from a roster.
# Citations: https://stackoverflow.com/questions/45153422/how-to-properly-implement-both-str-and-repr

# Anything else that's relevant:

class Team:
    def __init__(self,name,coach):
        """
        Initializes the Team object with the given name and coach
        @param str the name of the team
        @param coach str name of the coach
        """
        self.name = name
        self.coach = coach
        self.roster = []
    def name(self):
        """
        Shows name of the team
        @param
        returns name of the team
        """
        return self._name
    def name(self, value):
        """
        Sets the name
        @param
        """
        self._name = value
    def coach(self):
        """
        Shows the name of the coach's team
        @param
        """
        return self._coach
    def coach(self, value):
        """
        Sets the name of the teams coach
        @param
        """
        self._coach = value
    def roster(self):
        """
        Shows the current roster
        @param
        Returns roster
        """
        return self._roster
    def roster(self, value):
        """
        Sets the lsit of players
        @param
        """
        self._roster = value
    def __str__(self):
        """
        returns a readable string
        """
        return f"Team: {self.name}, Coach: {self.coach}, Roster size: {len(self.roster)}"
    def __repr__(self):
        """
        Returns a detailed string rep of the team object
        """
        return f"Team(name={self.name}, coach={self.coach}, roster={self.roster})"
    def add_player(self, player):
        """
        Adds a player to the team's roster
        @param player is added
        """
        self.roster.append(player)
        print(f"{player.name} added to {self.name}.")
    def remove_player(self, player):
        """
        Removes a player from the team's roster
        @param player is removed
        """
        self.roster.remove(player)
        print(f"{player.name} removed from {self.name}.")
    def display_roster(self):
        """
        Displays the list of players currently on the active roster
        @param
        returns: list of players
        """
        return [player.name for player in self.roster]