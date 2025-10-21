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

        if not crypto_token:
            print(f"In order to acquire a rig, {self.name} needs a CryptoToken.")
            return False

        self.inventory.remove(crypto_token)

        if rig:
            self.rig = rig

        else:
            self.rig = Rig(f"Rig belongs to {self.name}.")

        print(f"{self.name} has successfully acquired {self.rig.name}!")
        return True


    # launch data spikes on another rig, increasing its trace level and consuming one spike.
    def launch_attack(self, target):

        # checking prior to attack - no rig found, broken rig, or if trace level is at max
        if not self.rig:
            print(f"{self.name} has no rig for launching an attack!")
            return False

        if self.rig.broken:
            print(f"Can't attack a broken rig {self.rig.name}!!")
            return False

        if self.trace_level >= self.trace_threshold:
            print(f"Can't attack, trace level is too high!!!")
            return False

        # find data spike from rig storage
        data_spike = None
        for asset in self.rig.storage:
            if asset.name == "Data Spike" and not asset.encrypted:
                data_spike = asset

        # data spike found if not returns false
        if not data_spike:
            print(f"{self.rig.name} has no available Data Spikes.")
            return False

        # remove data spike from storage to execute attack
        self.rig.storage.remove(data_spike)
        self.trace_level += 1 # increasing trace level

        print(f"{self.name} launched Data Spike attack at {target.name}.\n"
              f"New Trace Level: {self.trace_level}")
        target.take_hit()
        return True


    # method to extract unsecured assets from a broken rig
    def extract_asset(self, target):

        # since extraction action can only be performed on a broken system
        # checking if the target has been comprimised
        if not target.broken:
            print(f"{target.name} can't be extracted, rig is not broken.")
            return False

        # searching for removable drive in rig storage
        # conditions: drive must exist and not be encrypted
        removable_drive = None
        for asset in self.rig.storage:
            if asset.name == "Removable Drive" and not asset.encrypted:
                removable_drive = asset

        # removable drive found if not returns false
        if not removable_drive:
            print(f"Could not find Removable Drive in storage!\n"
                  f"Can't perform extraction.")
            return False

        # begin extraction of unencrypted assets
        self.rig.storage.remove(removable_drive)

        # tracks number of successful extractions
        extract_count = 0

        # iterate through original list using [:]
        # only extracts assets that are not encrypted and removes them from the storage
        for asset in target.storage[:]:
            if not asset.encrypted:
                target.storage.remove(asset)

                # transfers assets to the hacker's rig storage
                self.rig.store_asset(asset)
                extract_count += 1

        print(f"{extract_count} unencrypted assets successfully extracted from {target.name}")
        return extract_count > 0

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
