from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity

from . import entity

class ResourceOperation(entity.Entity):
    """
    Describes the resourceOperation resource (entity) of the Microsoft Graph API (REST), which supports Intune workflows related to role-based access control (RBAC).
    """
    def __init__(self,) -> None:
        """
        Instantiates a new resourceOperation and sets the default values.
        """
        super().__init__()
        # Type of action this operation is going to perform. The actionName should be concise and limited to as few words as possible.
        self._action_name: Optional[str] = None
        # Description of the resource operation. The description is used in mouse-over text for the operation when shown in the Azure Portal.
        self._description: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Name of the Resource this operation is performed on.
        self._resource_name: Optional[str] = None
    
    @property
    def action_name(self,) -> Optional[str]:
        """
        Gets the actionName property value. Type of action this operation is going to perform. The actionName should be concise and limited to as few words as possible.
        Returns: Optional[str]
        """
        return self._action_name
    
    @action_name.setter
    def action_name(self,value: Optional[str] = None) -> None:
        """
        Sets the actionName property value. Type of action this operation is going to perform. The actionName should be concise and limited to as few words as possible.
        Args:
            value: Value to set for the action_name property.
        """
        self._action_name = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ResourceOperation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ResourceOperation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ResourceOperation()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Description of the resource operation. The description is used in mouse-over text for the operation when shown in the Azure Portal.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Description of the resource operation. The description is used in mouse-over text for the operation when shown in the Azure Portal.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "actionName": lambda n : setattr(self, 'action_name', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "resourceName": lambda n : setattr(self, 'resource_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def resource_name(self,) -> Optional[str]:
        """
        Gets the resourceName property value. Name of the Resource this operation is performed on.
        Returns: Optional[str]
        """
        return self._resource_name
    
    @resource_name.setter
    def resource_name(self,value: Optional[str] = None) -> None:
        """
        Sets the resourceName property value. Name of the Resource this operation is performed on.
        Args:
            value: Value to set for the resource_name property.
        """
        self._resource_name = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("actionName", self.action_name)
        writer.write_str_value("description", self.description)
        writer.write_str_value("resourceName", self.resource_name)
    

