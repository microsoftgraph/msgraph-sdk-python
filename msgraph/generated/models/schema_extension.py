from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, extension_schema_property

from . import entity

class SchemaExtension(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new SchemaExtension and sets the default values.
        """
        super().__init__()
        # Description for the schema extension. Supports $filter (eq).
        self._description: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The appId of the application that is the owner of the schema extension. The owner of the schema definition must be explicitly specified during the Create and Update operations, or it will be implied and auto-assigned by Azure AD as follows: In delegated access: The signed-in user must be the owner of the app that calls Microsoft Graph to create the schema extension definition.  If the signed-in user isn't the owner of the calling app, they must explicitly specify the owner property, and assign it the appId of an app that they own. In app-only access:  The owner property isn't required in the request body. Instead, the calling app is assigned ownership of the schema extension. So, for example, if creating a new schema extension definition using Graph Explorer, you must supply the owner property. Once set, this property is read-only and cannot be changed. Supports $filter (eq).
        self._owner: Optional[str] = None
        # The collection of property names and types that make up the schema extension definition.
        self._properties: Optional[List[extension_schema_property.ExtensionSchemaProperty]] = None
        # The lifecycle state of the schema extension. Possible states are InDevelopment, Available, and Deprecated. Automatically set to InDevelopment on creation. For more information about the possible state transitions and behaviors, see Schema extensions lifecycle. Supports $filter (eq).
        self._status: Optional[str] = None
        # Set of Microsoft Graph types (that can support extensions) that the schema extension can be applied to. Select from administrativeUnit, contact, device, event, group, message, organization, post, todoTask, todoTaskList, or user.
        self._target_types: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SchemaExtension:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SchemaExtension
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SchemaExtension()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Description for the schema extension. Supports $filter (eq).
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Description for the schema extension. Supports $filter (eq).
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, extension_schema_property

        fields: Dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "owner": lambda n : setattr(self, 'owner', n.get_str_value()),
            "properties": lambda n : setattr(self, 'properties', n.get_collection_of_object_values(extension_schema_property.ExtensionSchemaProperty)),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
            "targetTypes": lambda n : setattr(self, 'target_types', n.get_collection_of_primitive_values(str)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def owner(self,) -> Optional[str]:
        """
        Gets the owner property value. The appId of the application that is the owner of the schema extension. The owner of the schema definition must be explicitly specified during the Create and Update operations, or it will be implied and auto-assigned by Azure AD as follows: In delegated access: The signed-in user must be the owner of the app that calls Microsoft Graph to create the schema extension definition.  If the signed-in user isn't the owner of the calling app, they must explicitly specify the owner property, and assign it the appId of an app that they own. In app-only access:  The owner property isn't required in the request body. Instead, the calling app is assigned ownership of the schema extension. So, for example, if creating a new schema extension definition using Graph Explorer, you must supply the owner property. Once set, this property is read-only and cannot be changed. Supports $filter (eq).
        Returns: Optional[str]
        """
        return self._owner
    
    @owner.setter
    def owner(self,value: Optional[str] = None) -> None:
        """
        Sets the owner property value. The appId of the application that is the owner of the schema extension. The owner of the schema definition must be explicitly specified during the Create and Update operations, or it will be implied and auto-assigned by Azure AD as follows: In delegated access: The signed-in user must be the owner of the app that calls Microsoft Graph to create the schema extension definition.  If the signed-in user isn't the owner of the calling app, they must explicitly specify the owner property, and assign it the appId of an app that they own. In app-only access:  The owner property isn't required in the request body. Instead, the calling app is assigned ownership of the schema extension. So, for example, if creating a new schema extension definition using Graph Explorer, you must supply the owner property. Once set, this property is read-only and cannot be changed. Supports $filter (eq).
        Args:
            value: Value to set for the owner property.
        """
        self._owner = value
    
    @property
    def properties(self,) -> Optional[List[extension_schema_property.ExtensionSchemaProperty]]:
        """
        Gets the properties property value. The collection of property names and types that make up the schema extension definition.
        Returns: Optional[List[extension_schema_property.ExtensionSchemaProperty]]
        """
        return self._properties
    
    @properties.setter
    def properties(self,value: Optional[List[extension_schema_property.ExtensionSchemaProperty]] = None) -> None:
        """
        Sets the properties property value. The collection of property names and types that make up the schema extension definition.
        Args:
            value: Value to set for the properties property.
        """
        self._properties = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("description", self.description)
        writer.write_str_value("owner", self.owner)
        writer.write_collection_of_object_values("properties", self.properties)
        writer.write_str_value("status", self.status)
        writer.write_collection_of_primitive_values("targetTypes", self.target_types)
    
    @property
    def status(self,) -> Optional[str]:
        """
        Gets the status property value. The lifecycle state of the schema extension. Possible states are InDevelopment, Available, and Deprecated. Automatically set to InDevelopment on creation. For more information about the possible state transitions and behaviors, see Schema extensions lifecycle. Supports $filter (eq).
        Returns: Optional[str]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[str] = None) -> None:
        """
        Sets the status property value. The lifecycle state of the schema extension. Possible states are InDevelopment, Available, and Deprecated. Automatically set to InDevelopment on creation. For more information about the possible state transitions and behaviors, see Schema extensions lifecycle. Supports $filter (eq).
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    
    @property
    def target_types(self,) -> Optional[List[str]]:
        """
        Gets the targetTypes property value. Set of Microsoft Graph types (that can support extensions) that the schema extension can be applied to. Select from administrativeUnit, contact, device, event, group, message, organization, post, todoTask, todoTaskList, or user.
        Returns: Optional[List[str]]
        """
        return self._target_types
    
    @target_types.setter
    def target_types(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the targetTypes property value. Set of Microsoft Graph types (that can support extensions) that the schema extension can be applied to. Select from administrativeUnit, contact, device, event, group, message, organization, post, todoTask, todoTaskList, or user.
        Args:
            value: Value to set for the target_types property.
        """
        self._target_types = value
    

