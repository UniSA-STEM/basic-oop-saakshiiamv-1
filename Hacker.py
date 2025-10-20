"""
File: Hacker.py
Description: This class handles all hacker actions such as attacks, encryption, upgrades, and etc.
Author: Sakshi Ambekar
ID: <student_id>
Username: ambss001
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Asset import Asset
from Rig import Rig

class Hacker:
    def __init__(self, name):
        self.name = name
        self.inventory = [] # hacker's assets
        self.rig = None # as default the hacker has no computer rigs
        self.trace_level = 0 # default level
        self.trace_threshold = 5 # level at which hacker is exposed

        # begins with a basic inventory containing a single CyrptoToken
        self.inventory.append(Asset("CryptoToken", "A digital currency that acquires or repairs rig"))
        print(f"Initialise hacker {self.name} with basic inventory.")

    # acquire rig with a CryptoToken, either using an existing one or creating a new rig
    # returns a true or false boolean output
    def acquire_rig(self, rig):
        self.rig = None

        # checking if rig already has a CryptoToken
        if self.rig:
            print(f"Rig {self.rig.name} already belongs to {self.name}.")
            return False

        # now finds cryptoToken in inventory, removes it and acquires a rig successfully
        crypto_token = None
        for asset in self.inventory:
            if asset.name == "CryptoToken" and not asset.encrypted:
                crypto_token = asset

                self.inventory.remove(crypto_token)

            if rig:
                self.rig = rig

            else:
                self.rig = Rig(f"Rig belongs to {self.name}.")

            print(f"{self.name} has successfully acquired {self.rig.name}!")
            return True

        print(f"In order to acquire a rig, {self.name} needs a CryptoToken.")
        return False

    def launch_attack(self, target):


    def extract_asset(self, target):
        pass

    def encrypt_asset(self, asset, location):
        pass

    def decrypt_asset(self, asset, location):
        pass

    def upgrade_rig(self):
        pass

    def store_asset(self, asset_name):
        pass

    def retrieve_asset(self, asset_name):
        pass

    def scan_inventory(self, asset_name):
        pass
