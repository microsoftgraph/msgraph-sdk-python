from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import group, localized_name, relation, term
    from .. import entity, key_value

from .. import entity

@dataclass
class Set(entity.Entity):
    # Children terms of set in term [store].
    children: Optional[List[term.Term]] = None
    # Date and time of set creation. Read-only.
    created_date_time: Optional[datetime] = None
    # Description that gives details on the term usage.
    description: Optional[str] = None
    # Name of the set for each languageTag.
    localized_names: Optional[List[localized_name.LocalizedName]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The parentGroup property
    parent_group: Optional[group.Group] = None
    # Custom properties for the set.
    properties: Optional[List[key_value.KeyValue]] = None
    # Indicates which terms have been pinned or reused directly under the set.
    relations: Optional[List[relation.Relation]] = None
    # All the terms under the set.
    terms: Optional[List[term.Term]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Set:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Set
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Set()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import group, localized_name, relation, term
        from .. import entity, key_value

        from . import group, localized_name, relation, term
        from .. import entity, key_value

        fields: Dict[str, Callable[[Any], None]] = {
            "children": lambda n : setattr(self, 'children', n.get_collection_of_object_values(term.Term)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "localizedNames": lambda n : setattr(self, 'localized_names', n.get_collection_of_object_values(localized_name.LocalizedName)),
            "parentGroup": lambda n : setattr(self, 'parent_group', n.get_object_value(group.Group)),
            "properties": lambda n : setattr(self, 'properties', n.get_collection_of_object_values(key_value.KeyValue)),
            "relations": lambda n : setattr(self, 'relations', n.get_collection_of_object_values(relation.Relation)),
            "terms": lambda n : setattr(self, 'terms', n.get_collection_of_object_values(term.Term)),
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
        if not writer:
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
    

