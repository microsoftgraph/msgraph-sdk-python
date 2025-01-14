from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .audit_property import AuditProperty

@dataclass
class AuditResource(AdditionalDataHolder, BackedModel, Parsable):
    """
    A class containing the properties for Audit Resource.
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Audit resource's type.
    audit_resource_type: Optional[str] = None
    # Display name.
    display_name: Optional[str] = None
    # List of modified properties.
    modified_properties: Optional[list[AuditProperty]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Audit resource's Id.
    resource_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AuditResource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AuditResource
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AuditResource()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .audit_property import AuditProperty

        from .audit_property import AuditProperty

        fields: dict[str, Callable[[Any], None]] = {
            "auditResourceType": lambda n : setattr(self, 'audit_resource_type', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "modifiedProperties": lambda n : setattr(self, 'modified_properties', n.get_collection_of_object_values(AuditProperty)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "resourceId": lambda n : setattr(self, 'resource_id', n.get_str_value()),
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
        writer.write_str_value("auditResourceType", self.audit_resource_type)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("modifiedProperties", self.modified_properties)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("resourceId", self.resource_id)
        writer.write_additional_data_value(self.additional_data)
    

