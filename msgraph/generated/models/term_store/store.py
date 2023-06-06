from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import group, set
    from .. import entity

from .. import entity

@dataclass
class Store(entity.Entity):
    # Default language of the term store.
    default_language_tag: Optional[str] = None
    # Collection of all groups available in the term store.
    groups: Optional[List[group.Group]] = None
    # List of languages for the term store.
    language_tags: Optional[List[str]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Collection of all sets available in the term store. This relationship can only be used to load a specific term set.
    sets: Optional[List[set.Set]] = None
    
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
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import group, set
        from .. import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "defaultLanguageTag": lambda n : setattr(self, 'default_language_tag', n.get_str_value()),
            "groups": lambda n : setattr(self, 'groups', n.get_collection_of_object_values(group.Group)),
            "languageTags": lambda n : setattr(self, 'language_tags', n.get_collection_of_primitive_values(str)),
            "sets": lambda n : setattr(self, 'sets', n.get_collection_of_object_values(set.Set)),
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
        writer.write_str_value("defaultLanguageTag", self.default_language_tag)
        writer.write_collection_of_object_values("groups", self.groups)
        writer.write_collection_of_primitive_values("languageTags", self.language_tags)
        writer.write_collection_of_object_values("sets", self.sets)
    

