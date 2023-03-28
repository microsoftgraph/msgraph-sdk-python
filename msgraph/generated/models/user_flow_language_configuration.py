from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, user_flow_language_page

from . import entity

class UserFlowLanguageConfiguration(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new userFlowLanguageConfiguration and sets the default values.
        """
        super().__init__()
        # Collection of pages with the default content to display in a user flow for a specified language. This collection does not allow any kind of modification.
        self._default_pages: Optional[List[user_flow_language_page.UserFlowLanguagePage]] = None
        # The language name to display. This property is read-only.
        self._display_name: Optional[str] = None
        # Indicates whether the language is enabled within the user flow.
        self._is_enabled: Optional[bool] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Collection of pages with the overrides messages to display in a user flow for a specified language. This collection only allows to modify the content of the page, any other modification is not allowed (creation or deletion of pages).
        self._overrides_pages: Optional[List[user_flow_language_page.UserFlowLanguagePage]] = None
    
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
    
    @property
    def default_pages(self,) -> Optional[List[user_flow_language_page.UserFlowLanguagePage]]:
        """
        Gets the defaultPages property value. Collection of pages with the default content to display in a user flow for a specified language. This collection does not allow any kind of modification.
        Returns: Optional[List[user_flow_language_page.UserFlowLanguagePage]]
        """
        return self._default_pages
    
    @default_pages.setter
    def default_pages(self,value: Optional[List[user_flow_language_page.UserFlowLanguagePage]] = None) -> None:
        """
        Sets the defaultPages property value. Collection of pages with the default content to display in a user flow for a specified language. This collection does not allow any kind of modification.
        Args:
            value: Value to set for the default_pages property.
        """
        self._default_pages = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The language name to display. This property is read-only.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The language name to display. This property is read-only.
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
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
    
    @property
    def is_enabled(self,) -> Optional[bool]:
        """
        Gets the isEnabled property value. Indicates whether the language is enabled within the user flow.
        Returns: Optional[bool]
        """
        return self._is_enabled
    
    @is_enabled.setter
    def is_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isEnabled property value. Indicates whether the language is enabled within the user flow.
        Args:
            value: Value to set for the is_enabled property.
        """
        self._is_enabled = value
    
    @property
    def overrides_pages(self,) -> Optional[List[user_flow_language_page.UserFlowLanguagePage]]:
        """
        Gets the overridesPages property value. Collection of pages with the overrides messages to display in a user flow for a specified language. This collection only allows to modify the content of the page, any other modification is not allowed (creation or deletion of pages).
        Returns: Optional[List[user_flow_language_page.UserFlowLanguagePage]]
        """
        return self._overrides_pages
    
    @overrides_pages.setter
    def overrides_pages(self,value: Optional[List[user_flow_language_page.UserFlowLanguagePage]] = None) -> None:
        """
        Sets the overridesPages property value. Collection of pages with the overrides messages to display in a user flow for a specified language. This collection only allows to modify the content of the page, any other modification is not allowed (creation or deletion of pages).
        Args:
            value: Value to set for the overrides_pages property.
        """
        self._overrides_pages = value
    
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
    

