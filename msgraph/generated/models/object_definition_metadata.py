from enum import Enum

class ObjectDefinitionMetadata(Enum):
    PropertyNameAccountEnabled = "PropertyNameAccountEnabled",
    PropertyNameSoftDeleted = "PropertyNameSoftDeleted",
    IsSoftDeletionSupported = "IsSoftDeletionSupported",
    IsSynchronizeAllSupported = "IsSynchronizeAllSupported",
    ConnectorDataStorageRequired = "ConnectorDataStorageRequired",
    Extensions = "Extensions",
    BaseObjectName = "BaseObjectName",

