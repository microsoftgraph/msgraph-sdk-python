from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .group import Group
    from .set import Set

from ..entity import Entity

@dataclass
class Store(Entity, Parsable):
    # Default language of the term store.
    default_language_tag: Optional[str] = None
    # Collection of all groups available in the term store.
    groups: Optional[list[Group]] = None
    # List of languages for the term store.
    language_tags: Optional[list[str]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Collection of all sets available in the term store. This relationship can only be used to load a specific term set.
    sets: Optional[list[Set]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Store:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Store
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Store()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .group import Group
        from .set import Set

        from ..entity import Entity
        from .group import Group
        from .set import Set

        fields: dict[str, Callable[[Any], None]] = {
            "defaultLanguageTag": lambda n : setattr(self, 'default_language_tag', n.get_str_value()),
            "groups": lambda n : setattr(self, 'groups', n.get_collection_of_object_values(Group)),
            "languageTags": lambda n : setattr(self, 'language_tags', n.get_collection_of_primitive_values(str)),
            "sets": lambda n : setattr(self, 'sets', n.get_collection_of_object_values(Set)),
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
        writer.write_str_value("defaultLanguageTag", self.default_language_tag)
        writer.write_collection_of_object_values("groups", self.groups)
        writer.write_collection_of_primitive_values("languageTags", self.language_tags)
        writer.write_collection_of_object_values("sets", self.sets)
    

