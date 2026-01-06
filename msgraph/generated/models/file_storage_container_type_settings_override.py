from enum import Enum

class FileStorageContainerTypeSettingsOverride(str, Enum):
    UrlTemplate = "urlTemplate",
    IsDiscoverabilityEnabled = "isDiscoverabilityEnabled",
    IsSearchEnabled = "isSearchEnabled",
    IsItemVersioningEnabled = "isItemVersioningEnabled",
    ItemMajorVersionLimit = "itemMajorVersionLimit",
    MaxStoragePerContainerInBytes = "maxStoragePerContainerInBytes",
    UnknownFutureValue = "unknownFutureValue",

