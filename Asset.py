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
        self.__name = name
        self.__description = description
        self.__is_encrypted =  # assests default start: unencrypted - boolean


