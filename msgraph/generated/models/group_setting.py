from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
setting_value = lazy_import('msgraph.generated.models.setting_value')

class GroupSetting(entity.Entity):
    """
    Provides operations to manage the collection of agreement entities.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new groupSetting and sets the default values.
        """
        super().__init__()
        # Display name of this group of settings, which comes from the associated template.
        self._display_name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Unique identifier for the tenant-level groupSettingTemplates object that's been customized for this group-level settings object. Read-only.
        self._template_id: Optional[str] = None
        # Collection of name-value pairs corresponding to the name and defaultValue properties in the referenced groupSettingTemplates object.
        self._values: Optional[List[setting_value.SettingValue]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> GroupSetting:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: GroupSetting
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return GroupSetting()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Display name of this group of settings, which comes from the associated template.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Display name of this group of settings, which comes from the associated template.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "template_id": lambda n : setattr(self, 'template_id', n.get_str_value()),
            "values": lambda n : setattr(self, 'values', n.get_collection_of_object_values(setting_value.SettingValue)),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("templateId", self.template_id)
        writer.write_collection_of_object_values("values", self.values)
    
    @property
    def template_id(self,) -> Optional[str]:
        """
        Gets the templateId property value. Unique identifier for the tenant-level groupSettingTemplates object that's been customized for this group-level settings object. Read-only.
        Returns: Optional[str]
        """
        return self._template_id
    
    @template_id.setter
    def template_id(self,value: Optional[str] = None) -> None:
        """
        Sets the templateId property value. Unique identifier for the tenant-level groupSettingTemplates object that's been customized for this group-level settings object. Read-only.
        Args:
            value: Value to set for the templateId property.
        """
        self._template_id = value
    
    @property
    def values(self,) -> Optional[List[setting_value.SettingValue]]:
        """
        Gets the values property value. Collection of name-value pairs corresponding to the name and defaultValue properties in the referenced groupSettingTemplates object.
        Returns: Optional[List[setting_value.SettingValue]]
        """
        return self._values
    
    @values.setter
    def values(self,value: Optional[List[setting_value.SettingValue]] = None) -> None:
        """
        Sets the values property value. Collection of name-value pairs corresponding to the name and defaultValue properties in the referenced groupSettingTemplates object.
        Args:
            value: Value to set for the values property.
        """
        self._values = value
    

