from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .user_flow_language_page import UserFlowLanguagePage

from .entity import Entity

@dataclass
class UserFlowLanguageConfiguration(Entity, Parsable):
    # Collection of pages with the default content to display in a user flow for a specified language. This collection doesn't allow any kind of modification.
    default_pages: Optional[list[UserFlowLanguagePage]] = None
    # The language name to display. This property is read-only.
    display_name: Optional[str] = None
    # Indicates whether the language is enabled within the user flow.
    is_enabled: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Collection of pages with the overrides messages to display in a user flow for a specified language. This collection only allows you to modify the content of the page, any other modification isn't allowed (creation or deletion of pages).
    overrides_pages: Optional[list[UserFlowLanguagePage]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserFlowLanguageConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserFlowLanguageConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UserFlowLanguageConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .user_flow_language_page import UserFlowLanguagePage

        from .entity import Entity
        from .user_flow_language_page import UserFlowLanguagePage

        fields: dict[str, Callable[[Any], None]] = {
            "defaultPages": lambda n : setattr(self, 'default_pages', n.get_collection_of_object_values(UserFlowLanguagePage)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "isEnabled": lambda n : setattr(self, 'is_enabled', n.get_bool_value()),
            "overridesPages": lambda n : setattr(self, 'overrides_pages', n.get_collection_of_object_values(UserFlowLanguagePage)),
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
        writer.write_collection_of_object_values("defaultPages", self.default_pages)
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("isEnabled", self.is_enabled)
        writer.write_collection_of_object_values("overridesPages", self.overrides_pages)
    

