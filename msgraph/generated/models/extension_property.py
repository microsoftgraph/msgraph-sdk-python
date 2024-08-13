from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .directory_object import DirectoryObject

from .directory_object import DirectoryObject

@dataclass
class ExtensionProperty(DirectoryObject):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.extensionProperty"
    # Display name of the application object on which this extension property is defined. Read-only.
    app_display_name: Optional[str] = None
    # Specifies the data type of the value the extension property can hold. Following values are supported. Binary - 256 bytes maximumBooleanDateTime - Must be specified in ISO 8601 format. Will be stored in UTC.Integer - 32-bit value.LargeInteger - 64-bit value.String - 256 characters maximumNot nullable. For multivalued directory extensions, these limits apply per value in the collection.
    data_type: Optional[str] = None
    # Defines the directory extension as a multi-valued property. When true, the directory extension property can store a collection of objects of the dataType; for example, a collection of string types such as 'extensionb7b1c57b532f40b8b5ed4b7a7ba67401jobGroupTracker': ['String 1', 'String 2']. The default value is false. Supports $filter (eq).
    is_multi_valued: Optional[bool] = None
    # Indicates if this extension property was synced from on-premises active directory using Microsoft Entra Connect. Read-only.
    is_synced_from_on_premises: Optional[bool] = None
    # Name of the extension property. Not nullable. Supports $filter (eq).
    name: Optional[str] = None
    # Following values are supported. Not nullable. UserGroupAdministrativeUnitApplicationDeviceOrganization
    target_objects: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ExtensionProperty:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ExtensionProperty
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ExtensionProperty()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .directory_object import DirectoryObject

        from .directory_object import DirectoryObject

        fields: Dict[str, Callable[[Any], None]] = {
            "appDisplayName": lambda n : setattr(self, 'app_display_name', n.get_str_value()),
            "dataType": lambda n : setattr(self, 'data_type', n.get_str_value()),
            "isMultiValued": lambda n : setattr(self, 'is_multi_valued', n.get_bool_value()),
            "isSyncedFromOnPremises": lambda n : setattr(self, 'is_synced_from_on_premises', n.get_bool_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "targetObjects": lambda n : setattr(self, 'target_objects', n.get_collection_of_primitive_values(str)),
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
        writer.write_str_value("appDisplayName", self.app_display_name)
        writer.write_str_value("dataType", self.data_type)
        writer.write_bool_value("isMultiValued", self.is_multi_valued)
        writer.write_bool_value("isSyncedFromOnPremises", self.is_synced_from_on_premises)
        writer.write_str_value("name", self.name)
        writer.write_collection_of_primitive_values("targetObjects", self.target_objects)
    

