from enum import Enum

class DefenderThreatAction(Enum):
    # Apply action based on the update definition.
    DeviceDefault = "deviceDefault",
    # Clean the detected threat.
    Clean = "clean",
    # Quarantine the detected threat.
    Quarantine = "quarantine",
    # Remove the detected threat.
    Remove = "remove",
    # Allow the detected threat.
    Allow = "allow",
    # Allow the user to determine the action to take with the detected threat.
    UserDefined = "userDefined",
    # Block the detected threat.
    Block = "block",

