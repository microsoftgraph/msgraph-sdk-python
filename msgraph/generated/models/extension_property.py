from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

directory_object = lazy_import('msgraph.generated.models.directory_object')

class ExtensionProperty(directory_object.DirectoryObject):
    """
    Provides operations to manage the collection of application entities.
    """
    @property
    def app_display_name(self,) -> Optional[str]:
        """
        Gets the appDisplayName property value. Display name of the application object on which this extension property is defined. Read-only.
        Returns: Optional[str]
        """
        return self._app_display_name
    
    @app_display_name.setter
    def app_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the appDisplayName property value. Display name of the application object on which this extension property is defined. Read-only.
        Args:
            value: Value to set for the appDisplayName property.
        """
        self._app_display_name = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new extensionProperty and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.extensionProperty"
        # Display name of the application object on which this extension property is defined. Read-only.
        self._app_display_name: Optional[str] = None
        # Specifies the data type of the value the extension property can hold. Following values are supported. Not nullable. Binary - 256 bytes maximumBooleanDateTime - Must be specified in ISO 8601 format. Will be stored in UTC.Integer - 32-bit value.LargeInteger - 64-bit value.String - 256 characters maximum
        self._data_type: Optional[str] = None
        # Indicates if this extension property was synced from on-premises active directory using Azure AD Connect. Read-only.
        self._is_synced_from_on_premises: Optional[bool] = None
        # Name of the extension property. Not nullable. Supports $filter (eq).
        self._name: Optional[str] = None
        # Following values are supported. Not nullable. UserGroupAdministrativeUnitApplicationDeviceOrganization
        self._target_objects: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ExtensionProperty:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ExtensionProperty
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ExtensionProperty()
    
    @property
    def data_type(self,) -> Optional[str]:
        """
        Gets the dataType property value. Specifies the data type of the value the extension property can hold. Following values are supported. Not nullable. Binary - 256 bytes maximumBooleanDateTime - Must be specified in ISO 8601 format. Will be stored in UTC.Integer - 32-bit value.LargeInteger - 64-bit value.String - 256 characters maximum
        Returns: Optional[str]
        """
        return self._data_type
    
    @data_type.setter
    def data_type(self,value: Optional[str] = None) -> None:
        """
        Sets the dataType property value. Specifies the data type of the value the extension property can hold. Following values are supported. Not nullable. Binary - 256 bytes maximumBooleanDateTime - Must be specified in ISO 8601 format. Will be stored in UTC.Integer - 32-bit value.LargeInteger - 64-bit value.String - 256 characters maximum
        Args:
            value: Value to set for the dataType property.
        """
        self._data_type = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "app_display_name": lambda n : setattr(self, 'app_display_name', n.get_str_value()),
            "data_type": lambda n : setattr(self, 'data_type', n.get_str_value()),
            "is_synced_from_on_premises": lambda n : setattr(self, 'is_synced_from_on_premises', n.get_bool_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "target_objects": lambda n : setattr(self, 'target_objects', n.get_collection_of_primitive_values(str)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_synced_from_on_premises(self,) -> Optional[bool]:
        """
        Gets the isSyncedFromOnPremises property value. Indicates if this extension property was synced from on-premises active directory using Azure AD Connect. Read-only.
        Returns: Optional[bool]
        """
        return self._is_synced_from_on_premises
    
    @is_synced_from_on_premises.setter
    def is_synced_from_on_premises(self,value: Optional[bool] = None) -> None:
        """
        Sets the isSyncedFromOnPremises property value. Indicates if this extension property was synced from on-premises active directory using Azure AD Connect. Read-only.
        Args:
            value: Value to set for the isSyncedFromOnPremises property.
        """
        self._is_synced_from_on_premises = value
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. Name of the extension property. Not nullable. Supports $filter (eq).
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. Name of the extension property. Not nullable. Supports $filter (eq).
        Args:
            value: Value to set for the name property.
        """
        self._name = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("appDisplayName", self.app_display_name)
        writer.write_str_value("dataType", self.data_type)
        writer.write_bool_value("isSyncedFromOnPremises", self.is_synced_from_on_premises)
        writer.write_str_value("name", self.name)
        writer.write_collection_of_primitive_values("targetObjects", self.target_objects)
    
    @property
    def target_objects(self,) -> Optional[List[str]]:
        """
        Gets the targetObjects property value. Following values are supported. Not nullable. UserGroupAdministrativeUnitApplicationDeviceOrganization
        Returns: Optional[List[str]]
        """
        return self._target_objects
    
    @target_objects.setter
    def target_objects(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the targetObjects property value. Following values are supported. Not nullable. UserGroupAdministrativeUnitApplicationDeviceOrganization
        Args:
            value: Value to set for the targetObjects property.
        """
        self._target_objects = value
    

