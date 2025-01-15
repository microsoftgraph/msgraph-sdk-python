from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .setting_value import SettingValue

from .entity import Entity

@dataclass
class GroupSetting(Entity, Parsable):
    # Display name of this group of settings, which comes from the associated template.
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Unique identifier for the tenant-level groupSettingTemplates object that's been customized for this group-level settings object. Read-only.
    template_id: Optional[str] = None
    # Collection of name-value pairs corresponding to the name and defaultValue properties in the referenced groupSettingTemplates object.
    values: Optional[list[SettingValue]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> GroupSetting:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GroupSetting
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return GroupSetting()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .setting_value import SettingValue

        from .entity import Entity
        from .setting_value import SettingValue

        fields: dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "templateId": lambda n : setattr(self, 'template_id', n.get_str_value()),
            "values": lambda n : setattr(self, 'values', n.get_collection_of_object_values(SettingValue)),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("templateId", self.template_id)
        writer.write_collection_of_object_values("values", self.values)
    

