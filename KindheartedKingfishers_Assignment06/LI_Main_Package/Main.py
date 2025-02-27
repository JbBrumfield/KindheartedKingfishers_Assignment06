# File Name : Main.py
# Student Name: Lucas Iceman
# email:  icemanlc@mail.uc.edu
# Assignment Number: Assignment 06
# Due Date:   2/27/2025
# Course #/Section:   IS4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:
# Brief Description of what this module does: 
# Citations: 
# Anything else that's relevant:

from JB_Package.team import *
from LV_Package.stadium import *

if __name__ == "__main__":
 
    stadium = Stadium("Grand Arena", 50000, "New York")

    print(stadium)
    
    stadium.host_event("Championship Match")
    print(stadium)  
    
    team = Team("Warriors", "Coach Smith")
    
    print(team)
    
    team.add_player("John Doe")
    team.add_player("Jane Smith")
    
    print(f"Roster: {team.display_roster()}")

    team.remove_player("John Doe")
    
    print(f"Updated Roster: {team.display_roster()}")