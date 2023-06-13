from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import localized_description, localized_label, relation, set
    from .. import entity, key_value

from .. import entity

@dataclass
class Term(entity.Entity):
    # Children of current term.
    children: Optional[List[Term]] = None
    # Date and time of term creation. Read-only.
    created_date_time: Optional[datetime] = None
    # Description about term that is dependent on the languageTag.
    descriptions: Optional[List[localized_description.LocalizedDescription]] = None
    # Label metadata for a term.
    labels: Optional[List[localized_label.LocalizedLabel]] = None
    # Last date and time of term modification. Read-only.
    last_modified_date_time: Optional[datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Collection of properties on the term.
    properties: Optional[List[key_value.KeyValue]] = None
    # To indicate which terms are related to the current term as either pinned or reused.
    relations: Optional[List[relation.Relation]] = None
    # The [set] in which the term is created.
    set: Optional[set.Set] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Term:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Term
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Term()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import localized_description, localized_label, relation, set
        from .. import entity, key_value

        fields: Dict[str, Callable[[Any], None]] = {
            "children": lambda n : setattr(self, 'children', n.get_collection_of_object_values(Term)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "descriptions": lambda n : setattr(self, 'descriptions', n.get_collection_of_object_values(localized_description.LocalizedDescription)),
            "labels": lambda n : setattr(self, 'labels', n.get_collection_of_object_values(localized_label.LocalizedLabel)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "properties": lambda n : setattr(self, 'properties', n.get_collection_of_object_values(key_value.KeyValue)),
            "relations": lambda n : setattr(self, 'relations', n.get_collection_of_object_values(relation.Relation)),
            "set": lambda n : setattr(self, 'set', n.get_object_value(set.Set)),
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
        writer.write_collection_of_object_values("children", self.children)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_collection_of_object_values("descriptions", self.descriptions)
        writer.write_collection_of_object_values("labels", self.labels)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_collection_of_object_values("properties", self.properties)
        writer.write_collection_of_object_values("relations", self.relations)
        writer.write_object_value("set", self.set)
    

