from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

subject_set = lazy_import('msgraph.generated.models.subject_set')

class ConnectedOrganizationMembers(subject_set.SubjectSet):
    @property
    def connected_organization_id(self,) -> Optional[str]:
        """
        Gets the connectedOrganizationId property value. The ID of the connected organization in entitlement management.
        Returns: Optional[str]
        """
        return self._connected_organization_id
    
    @connected_organization_id.setter
    def connected_organization_id(self,value: Optional[str] = None) -> None:
        """
        Sets the connectedOrganizationId property value. The ID of the connected organization in entitlement management.
        Args:
            value: Value to set for the connectedOrganizationId property.
        """
        self._connected_organization_id = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new ConnectedOrganizationMembers and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.connectedOrganizationMembers"
        # The ID of the connected organization in entitlement management.
        self._connected_organization_id: Optional[str] = None
        # The name of the connected organization.
        self._description: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ConnectedOrganizationMembers:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ConnectedOrganizationMembers
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ConnectedOrganizationMembers()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The name of the connected organization.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The name of the connected organization.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "connected_organization_id": lambda n : setattr(self, 'connected_organization_id', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("connectedOrganizationId", self.connected_organization_id)
        writer.write_str_value("description", self.description)
    

