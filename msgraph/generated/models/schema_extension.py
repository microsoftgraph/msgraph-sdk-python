from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
extension_schema_property = lazy_import('msgraph.generated.models.extension_schema_property')

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
        # The appId of the application that is the owner of the schema extension. This property can be supplied on creation, to set the owner.  If not supplied, then the calling application's appId will be set as the owner. In either case, the signed-in user must be the owner of the application. So, for example, if creating a new schema extension definition using Graph Explorer, you must supply the owner property. Once set, this property is read-only and cannot be changed. Supports $filter (eq).
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
        fields = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "owner": lambda n : setattr(self, 'owner', n.get_str_value()),
            "properties": lambda n : setattr(self, 'properties', n.get_collection_of_object_values(extension_schema_property.ExtensionSchemaProperty)),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
            "target_types": lambda n : setattr(self, 'target_types', n.get_collection_of_primitive_values(str)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def owner(self,) -> Optional[str]:
        """
        Gets the owner property value. The appId of the application that is the owner of the schema extension. This property can be supplied on creation, to set the owner.  If not supplied, then the calling application's appId will be set as the owner. In either case, the signed-in user must be the owner of the application. So, for example, if creating a new schema extension definition using Graph Explorer, you must supply the owner property. Once set, this property is read-only and cannot be changed. Supports $filter (eq).
        Returns: Optional[str]
        """
        return self._owner
    
    @owner.setter
    def owner(self,value: Optional[str] = None) -> None:
        """
        Sets the owner property value. The appId of the application that is the owner of the schema extension. This property can be supplied on creation, to set the owner.  If not supplied, then the calling application's appId will be set as the owner. In either case, the signed-in user must be the owner of the application. So, for example, if creating a new schema extension definition using Graph Explorer, you must supply the owner property. Once set, this property is read-only and cannot be changed. Supports $filter (eq).
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
            value: Value to set for the targetTypes property.
        """
        self._target_types = value
    

