from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .sharing_capabilities import SharingCapabilities

@dataclass
class FileStorageContainerTypeRegistrationSettings(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Indicates whether items from containers are surfaced in experiences such as My Activity or Microsoft 365.
    is_discoverability_enabled: Optional[bool] = None
    # Indicates whether item versioning is enabled.
    is_item_versioning_enabled: Optional[bool] = None
    # Indicates whether search is enabled.
    is_search_enabled: Optional[bool] = None
    # Only the manager and owner can share files in the container if restricted sharing is enabled.
    is_sharing_restricted: Optional[bool] = None
    # Maximum number of versions. Versioning must be enabled ('isItemVersioningEnabled'=true).
    item_major_version_limit: Optional[int] = None
    # Controls maximum storage in bytes.
    max_storage_per_container_in_bytes: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Sharing capabilities permitted for containers. The possible values are: disabled, externalUserSharingOnly, externalUserAndGuestSharing, existingExternalUserSharingOnly, unknownFutureValue. Can always be updated.
    sharing_capability: Optional[SharingCapabilities] = None
    # Pattern used to redirect files.
    url_template: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FileStorageContainerTypeRegistrationSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FileStorageContainerTypeRegistrationSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return FileStorageContainerTypeRegistrationSettings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .sharing_capabilities import SharingCapabilities

        from .sharing_capabilities import SharingCapabilities

        fields: dict[str, Callable[[Any], None]] = {
            "isDiscoverabilityEnabled": lambda n : setattr(self, 'is_discoverability_enabled', n.get_bool_value()),
            "isItemVersioningEnabled": lambda n : setattr(self, 'is_item_versioning_enabled', n.get_bool_value()),
            "isSearchEnabled": lambda n : setattr(self, 'is_search_enabled', n.get_bool_value()),
            "isSharingRestricted": lambda n : setattr(self, 'is_sharing_restricted', n.get_bool_value()),
            "itemMajorVersionLimit": lambda n : setattr(self, 'item_major_version_limit', n.get_int_value()),
            "maxStoragePerContainerInBytes": lambda n : setattr(self, 'max_storage_per_container_in_bytes', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "sharingCapability": lambda n : setattr(self, 'sharing_capability', n.get_enum_value(SharingCapabilities)),
            "urlTemplate": lambda n : setattr(self, 'url_template', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_bool_value("isDiscoverabilityEnabled", self.is_discoverability_enabled)
        writer.write_bool_value("isItemVersioningEnabled", self.is_item_versioning_enabled)
        writer.write_bool_value("isSearchEnabled", self.is_search_enabled)
        writer.write_bool_value("isSharingRestricted", self.is_sharing_restricted)
        writer.write_int_value("itemMajorVersionLimit", self.item_major_version_limit)
        writer.write_int_value("maxStoragePerContainerInBytes", self.max_storage_per_container_in_bytes)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("sharingCapability", self.sharing_capability)
        writer.write_str_value("urlTemplate", self.url_template)
        writer.write_additional_data_value(self.additional_data)
    

