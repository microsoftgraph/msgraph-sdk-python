from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .subject_set import SubjectSet

from .subject_set import SubjectSet

@dataclass
class ConnectedOrganizationMembers(SubjectSet, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.connectedOrganizationMembers"
    # The ID of the connected organization in entitlement management.
    connected_organization_id: Optional[str] = None
    # The name of the connected organization.
    description: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ConnectedOrganizationMembers:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ConnectedOrganizationMembers
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ConnectedOrganizationMembers()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .subject_set import SubjectSet

        from .subject_set import SubjectSet

        fields: dict[str, Callable[[Any], None]] = {
            "connectedOrganizationId": lambda n : setattr(self, 'connected_organization_id', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("connectedOrganizationId", self.connected_organization_id)
        writer.write_str_value("description", self.description)
    

