from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import audit_property

@dataclass
class AuditResource(AdditionalDataHolder, Parsable):
    """
    A class containing the properties for Audit Resource.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Audit resource's type.
    audit_resource_type: Optional[str] = None
    # Display name.
    display_name: Optional[str] = None
    # List of modified properties.
    modified_properties: Optional[List[audit_property.AuditProperty]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Audit resource's Id.
    resource_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AuditResource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AuditResource
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AuditResource()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import audit_property

        fields: Dict[str, Callable[[Any], None]] = {
            "auditResourceType": lambda n : setattr(self, 'audit_resource_type', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "modifiedProperties": lambda n : setattr(self, 'modified_properties', n.get_collection_of_object_values(audit_property.AuditProperty)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "resourceId": lambda n : setattr(self, 'resource_id', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("auditResourceType", self.audit_resource_type)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("modifiedProperties", self.modified_properties)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("resourceId", self.resource_id)
        writer.write_additional_data_value(self.additional_data)
    

