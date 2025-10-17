"""
File: Rig.py
Description: The rig class represents the computer system of a hacker.
Handling capabilities of storage, upgrades, damage, and generating assets.
Author: Sakshi Ambekar
ID: <student_id>
Username: ambss001
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Rig:
    def __init__(self, name):
        self.name = name
        self.damage_count = 0 # current damage level
        self.broken_state = False # is the rig functioning?
        self.storage = [] # storage for assets
        self.upgrade_level = 0
