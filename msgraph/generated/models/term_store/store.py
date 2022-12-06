from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
group = lazy_import('msgraph.generated.models.term_store.group')
set = lazy_import('msgraph.generated.models.term_store.set')

class Store(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new store and sets the default values.
        """
        super().__init__()
        # Default language of the term store.
        self._default_language_tag: Optional[str] = None
        # Collection of all groups available in the term store.
        self._groups: Optional[List[group.Group]] = None
        # List of languages for the term store.
        self._language_tags: Optional[List[str]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Collection of all sets available in the term store. This relationship can only be used to load a specific term set.
        self._sets: Optional[List[set.Set]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Store:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Store
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Store()
    
    @property
    def default_language_tag(self,) -> Optional[str]:
        """
        Gets the defaultLanguageTag property value. Default language of the term store.
        Returns: Optional[str]
        """
        return self._default_language_tag
    
    @default_language_tag.setter
    def default_language_tag(self,value: Optional[str] = None) -> None:
        """
        Sets the defaultLanguageTag property value. Default language of the term store.
        Args:
            value: Value to set for the defaultLanguageTag property.
        """
        self._default_language_tag = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "default_language_tag": lambda n : setattr(self, 'default_language_tag', n.get_str_value()),
            "groups": lambda n : setattr(self, 'groups', n.get_collection_of_object_values(group.Group)),
            "language_tags": lambda n : setattr(self, 'language_tags', n.get_collection_of_primitive_values(str)),
            "sets": lambda n : setattr(self, 'sets', n.get_collection_of_object_values(set.Set)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def groups(self,) -> Optional[List[group.Group]]:
        """
        Gets the groups property value. Collection of all groups available in the term store.
        Returns: Optional[List[group.Group]]
        """
        return self._groups
    
    @groups.setter
    def groups(self,value: Optional[List[group.Group]] = None) -> None:
        """
        Sets the groups property value. Collection of all groups available in the term store.
        Args:
            value: Value to set for the groups property.
        """
        self._groups = value
    
    @property
    def language_tags(self,) -> Optional[List[str]]:
        """
        Gets the languageTags property value. List of languages for the term store.
        Returns: Optional[List[str]]
        """
        return self._language_tags
    
    @language_tags.setter
    def language_tags(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the languageTags property value. List of languages for the term store.
        Args:
            value: Value to set for the languageTags property.
        """
        self._language_tags = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("defaultLanguageTag", self.default_language_tag)
        writer.write_collection_of_object_values("groups", self.groups)
        writer.write_collection_of_primitive_values("languageTags", self.language_tags)
        writer.write_collection_of_object_values("sets", self.sets)
    
    @property
    def sets(self,) -> Optional[List[set.Set]]:
        """
        Gets the sets property value. Collection of all sets available in the term store. This relationship can only be used to load a specific term set.
        Returns: Optional[List[set.Set]]
        """
        return self._sets
    
    @sets.setter
    def sets(self,value: Optional[List[set.Set]] = None) -> None:
        """
        Sets the sets property value. Collection of all sets available in the term store. This relationship can only be used to load a specific term set.
        Args:
            value: Value to set for the sets property.
        """
        self._sets = value
    

