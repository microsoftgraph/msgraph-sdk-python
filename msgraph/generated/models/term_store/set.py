from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from ..key_value import KeyValue
    from .group import Group
    from .localized_name import LocalizedName
    from .relation import Relation
    from .term import Term

from ..entity import Entity

@dataclass
class Set(Entity, Parsable):
    # Children terms of set in term [store].
    children: Optional[list[Term]] = None
    # Date and time of set creation. Read-only.
    created_date_time: Optional[datetime.datetime] = None
    # Description that gives details on the term usage.
    description: Optional[str] = None
    # Name of the set for each languageTag.
    localized_names: Optional[list[LocalizedName]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The parentGroup property
    parent_group: Optional[Group] = None
    # Custom properties for the set.
    properties: Optional[list[KeyValue]] = None
    # Indicates which terms have been pinned or reused directly under the set.
    relations: Optional[list[Relation]] = None
    # All the terms under the set.
    terms: Optional[list[Term]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Set:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Set
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Set()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from ..key_value import KeyValue
        from .group import Group
        from .localized_name import LocalizedName
        from .relation import Relation
        from .term import Term

        from ..entity import Entity
        from ..key_value import KeyValue
        from .group import Group
        from .localized_name import LocalizedName
        from .relation import Relation
        from .term import Term

        fields: dict[str, Callable[[Any], None]] = {
            "children": lambda n : setattr(self, 'children', n.get_collection_of_object_values(Term)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "localizedNames": lambda n : setattr(self, 'localized_names', n.get_collection_of_object_values(LocalizedName)),
            "parentGroup": lambda n : setattr(self, 'parent_group', n.get_object_value(Group)),
            "properties": lambda n : setattr(self, 'properties', n.get_collection_of_object_values(KeyValue)),
            "relations": lambda n : setattr(self, 'relations', n.get_collection_of_object_values(Relation)),
            "terms": lambda n : setattr(self, 'terms', n.get_collection_of_object_values(Term)),
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
        writer.write_collection_of_object_values("children", self.children)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_collection_of_object_values("localizedNames", self.localized_names)
        writer.write_object_value("parentGroup", self.parent_group)
        writer.write_collection_of_object_values("properties", self.properties)
        writer.write_collection_of_object_values("relations", self.relations)
        writer.write_collection_of_object_values("terms", self.terms)
    

