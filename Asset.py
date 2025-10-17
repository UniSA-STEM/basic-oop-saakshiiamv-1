"""
File: Asset.py
Description: The asset class is the base class for all items in the simulation.
It represents which digital assests can be encrypted and transferred.
Author: Sakshi Ambekar
ID: <student_id>
Username: ambss001
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Asset:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.is_encrypted =  # assests default start: unencrypted - boolean

    def __str__(self):
        if self.is_encrypted is True:
            return f"{self.name} : {self.description} [encrypted]"
        else:
            return f"{self.name} : {self.description}"
