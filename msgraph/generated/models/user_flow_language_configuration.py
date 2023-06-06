from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, user_flow_language_page

from . import entity

@dataclass
class UserFlowLanguageConfiguration(entity.Entity):
    # Collection of pages with the default content to display in a user flow for a specified language. This collection does not allow any kind of modification.
    default_pages: Optional[List[user_flow_language_page.UserFlowLanguagePage]] = None
    # The language name to display. This property is read-only.
    display_name: Optional[str] = None
    # Indicates whether the language is enabled within the user flow.
    is_enabled: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Collection of pages with the overrides messages to display in a user flow for a specified language. This collection only allows to modify the content of the page, any other modification is not allowed (creation or deletion of pages).
    overrides_pages: Optional[List[user_flow_language_page.UserFlowLanguagePage]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserFlowLanguageConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserFlowLanguageConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserFlowLanguageConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, user_flow_language_page

        fields: Dict[str, Callable[[Any], None]] = {
            "defaultPages": lambda n : setattr(self, 'default_pages', n.get_collection_of_object_values(user_flow_language_page.UserFlowLanguagePage)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "isEnabled": lambda n : setattr(self, 'is_enabled', n.get_bool_value()),
            "overridesPages": lambda n : setattr(self, 'overrides_pages', n.get_collection_of_object_values(user_flow_language_page.UserFlowLanguagePage)),
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
        writer.write_collection_of_object_values("defaultPages", self.default_pages)
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("isEnabled", self.is_enabled)
        writer.write_collection_of_object_values("overridesPages", self.overrides_pages)
    

