from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .directory_object import DirectoryObject
    from .setting_template_value import SettingTemplateValue

from .directory_object import DirectoryObject

@dataclass
class GroupSettingTemplate(DirectoryObject, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.groupSettingTemplate"
    # Description of the template.
    description: Optional[str] = None
    # Display name of the template. The template named Group.Unified can be used to configure tenant-wide Microsoft 365 group settings, while the template named Group.Unified.Guest can be used to configure group-specific settings.
    display_name: Optional[str] = None
    # Collection of settingTemplateValues that list the set of available settings, defaults and types that make up this template.
    values: Optional[list[SettingTemplateValue]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> GroupSettingTemplate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GroupSettingTemplate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return GroupSettingTemplate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .directory_object import DirectoryObject
        from .setting_template_value import SettingTemplateValue

        from .directory_object import DirectoryObject
        from .setting_template_value import SettingTemplateValue

        fields: dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "values": lambda n : setattr(self, 'values', n.get_collection_of_object_values(SettingTemplateValue)),
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
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("values", self.values)
    

