"""
File: main.py
Description: All classes test code running here. Simulating battles, upgrades,
             encryption, trace management, and etc.
Author: Sakshi Ambekar
ID: <student_id>
Username: ambss001
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Asset import Asset
from rigRedo import Rig
from hackerRedo import Hacker

print("PHASE 1. Testing base class creations")
# creating assets
crypto = Asset("CryptoToken", "A digital currency that acquires or repairs rig")
data_spike = Asset("Data Spike", "Hacking tool used in battles")
print(f"Successfully Created Assets \n    {crypto} \n    {data_spike}")

# test rig class creation with starting assets
print("\n1.1 Testing Rig Class:")
rig = Rig("testerRig1")
print(f"Successfully Created Rig: {rig.name}")
print(f"Starter Assets: {[asset.name for asset in rig.storage]}")
print(f"Condition: {rig.rig_condition()}")

# hacker creation and rig acquisition
print("\n1.2 Hacker Class and Rig Acquisition:")
hacker = Hacker("Cyberhacker")
print(f"Hacker: {hacker.name}")
print(f"Starter Inventory: {[asset.name for asset in hacker.inventory]}")

acquisition_res = hacker.acquire_rig()
print(f"\n      Rig Acquisition Success: {acquisition_res}")
if hacker.rig:
    print(f"      Rig Name: {hacker.rig.name}")
    print(f"      Inventory after Acquisition:"
          f" {[asset.name for asset in hacker.inventory]}")

print("\nPHASE 1 TESTS COMPLETED: Testing base class creations")



