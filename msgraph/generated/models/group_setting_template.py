from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

directory_object = lazy_import('msgraph.generated.models.directory_object')
setting_template_value = lazy_import('msgraph.generated.models.setting_template_value')

class GroupSettingTemplate(directory_object.DirectoryObject):
    def __init__(self,) -> None:
        """
        Instantiates a new GroupSettingTemplate and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.groupSettingTemplate"
        # Description of the template.
        self._description: Optional[str] = None
        # Display name of the template. The template named Group.Unified can be used to configure tenant-wide Microsoft 365 group settings, while the template named Group.Unified.Guest can be used to configure group-specific settings.
        self._display_name: Optional[str] = None
        # Collection of settingTemplateValues that list the set of available settings, defaults and types that make up this template.
        self._values: Optional[List[setting_template_value.SettingTemplateValue]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> GroupSettingTemplate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: GroupSettingTemplate
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return GroupSettingTemplate()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Description of the template.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Description of the template.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Display name of the template. The template named Group.Unified can be used to configure tenant-wide Microsoft 365 group settings, while the template named Group.Unified.Guest can be used to configure group-specific settings.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Display name of the template. The template named Group.Unified can be used to configure tenant-wide Microsoft 365 group settings, while the template named Group.Unified.Guest can be used to configure group-specific settings.
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
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "values": lambda n : setattr(self, 'values', n.get_collection_of_object_values(setting_template_value.SettingTemplateValue)),
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
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("values", self.values)
    
    @property
    def values(self,) -> Optional[List[setting_template_value.SettingTemplateValue]]:
        """
        Gets the values property value. Collection of settingTemplateValues that list the set of available settings, defaults and types that make up this template.
        Returns: Optional[List[setting_template_value.SettingTemplateValue]]
        """
        return self._values
    
    @values.setter
    def values(self,value: Optional[List[setting_template_value.SettingTemplateValue]] = None) -> None:
        """
        Sets the values property value. Collection of settingTemplateValues that list the set of available settings, defaults and types that make up this template.
        Args:
            value: Value to set for the values property.
        """
        self._values = value
    

