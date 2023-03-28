from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

role_assignment = lazy_import('msgraph.generated.models.role_assignment')

class DeviceAndAppManagementRoleAssignment(role_assignment.RoleAssignment):
    def __init__(self,) -> None:
        """
        Instantiates a new DeviceAndAppManagementRoleAssignment and sets the default values.
        """
        super().__init__()
        # The list of ids of role member security groups. These are IDs from Azure Active Directory.
        self._members: Optional[List[str]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceAndAppManagementRoleAssignment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceAndAppManagementRoleAssignment
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceAndAppManagementRoleAssignment()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "members": lambda n : setattr(self, 'members', n.get_collection_of_primitive_values(str)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def members(self,) -> Optional[List[str]]:
        """
        Gets the members property value. The list of ids of role member security groups. These are IDs from Azure Active Directory.
        Returns: Optional[List[str]]
        """
        return self._members
    
    @members.setter
    def members(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the members property value. The list of ids of role member security groups. These are IDs from Azure Active Directory.
        Args:
            value: Value to set for the members property.
        """
        self._members = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_primitive_values("members", self.members)
    

