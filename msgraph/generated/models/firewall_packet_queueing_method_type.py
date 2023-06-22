from enum import Enum

class FirewallPacketQueueingMethodType(str, Enum):
    # No value configured by Intune, do not override the user-configured device default value
    DeviceDefault = "deviceDefault",
    # Disable packet queuing
    Disabled = "disabled",
    # Queue inbound encrypted packets
    QueueInbound = "queueInbound",
    # Queue decrypted outbound packets for forwarding
    QueueOutbound = "queueOutbound",
    # Queue both inbound and outbound packets
    QueueBoth = "queueBoth",

