from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from ..key_value import KeyValue
    from .localized_description import LocalizedDescription
    from .localized_label import LocalizedLabel
    from .relation import Relation
    from .set import Set

from ..entity import Entity

@dataclass
class Term(Entity, Parsable):
    # Children of current term.
    children: Optional[list[Term]] = None
    # Date and time of term creation. Read-only.
    created_date_time: Optional[datetime.datetime] = None
    # Description about term that is dependent on the languageTag.
    descriptions: Optional[list[LocalizedDescription]] = None
    # Label metadata for a term.
    labels: Optional[list[LocalizedLabel]] = None
    # Last date and time of term modification. Read-only.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Collection of properties on the term.
    properties: Optional[list[KeyValue]] = None
    # To indicate which terms are related to the current term as either pinned or reused.
    relations: Optional[list[Relation]] = None
    # The [set] in which the term is created.
    set: Optional[Set] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Term:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Term
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Term()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from ..key_value import KeyValue
        from .localized_description import LocalizedDescription
        from .localized_label import LocalizedLabel
        from .relation import Relation
        from .set import Set

        from ..entity import Entity
        from ..key_value import KeyValue
        from .localized_description import LocalizedDescription
        from .localized_label import LocalizedLabel
        from .relation import Relation
        from .set import Set

        fields: dict[str, Callable[[Any], None]] = {
            "children": lambda n : setattr(self, 'children', n.get_collection_of_object_values(Term)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "descriptions": lambda n : setattr(self, 'descriptions', n.get_collection_of_object_values(LocalizedDescription)),
            "labels": lambda n : setattr(self, 'labels', n.get_collection_of_object_values(LocalizedLabel)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "properties": lambda n : setattr(self, 'properties', n.get_collection_of_object_values(KeyValue)),
            "relations": lambda n : setattr(self, 'relations', n.get_collection_of_object_values(Relation)),
            "set": lambda n : setattr(self, 'set', n.get_object_value(Set)),
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
        writer.write_collection_of_object_values("descriptions", self.descriptions)
        writer.write_collection_of_object_values("labels", self.labels)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_collection_of_object_values("properties", self.properties)
        writer.write_collection_of_object_values("relations", self.relations)
        writer.write_object_value("set", self.set)
    

