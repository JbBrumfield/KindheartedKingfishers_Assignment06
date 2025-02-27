# File Name : Main.py
# Student Name: Lucas Iceman
# email:  icemanlc@mail.uc.edu
# Assignment Number: Assignment 06
# Due Date:   2/27/2025
# Course #/Section:   IS4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:collaborate with peers to develop a VS project modeling something in the real world. 
# Brief Description of what this module does: This moduale call my classmates methods
# Citations: N/A
# Anything else that's relevant:N/A

from JB_Package.team import *
from LV_Package.stadium import *
from DD_Package.player import *


if __name__ == "__main__":
 
    bengals_stadium = Stadium("Paycor Stadium", 65515, "Cincinnati, OH")
    
    print(bengals_stadium)
    print(repr(bengals_stadium))

    bengals_stadium.capacity(70000) 

    bengals_stadium.host_event("Cincinnati Bengals vs. Pittsburgh Steelers")
    print(bengals_stadium)
    
    bengals_team = Team("Cincinnati Bengals", "Zac Taylor")

    print(bengals_team)
    print(repr(bengals_team))
    
    bengals_team.add_player("Joe Burrow", "Quarterback")  
    bengals_team.add_player("Ja'Marr Chase", "Wide Receiver")
    bengals_team.add_player("Tee Higgins", "Wide Receiver")
    bengals_team.add_player("Joe Mixon", "Running Back")

    print("Bengals Roster:", bengals_team.display_roster())
 
    bengals_team.remove_player("Tee Higgins")
    print("Updated Bengals Roster:", bengals_team.display_roster())

    joe_burrow = Player("Joe Burrow", "Quarterback", 9, 27)
    jamarr_chase = Player("Ja'Marr Chase", "Wide Receiver", 1, 24)
    joe_mixon = Player("Joe Mixon", "Running Back", 28, 27)

    print(joe_burrow)
    print(jamarr_chase)
    print(joe_mixon)

    joe_mixon.update_position("Fullback") 
    print(joe_mixon)