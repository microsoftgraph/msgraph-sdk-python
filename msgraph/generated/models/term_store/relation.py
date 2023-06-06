from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import relation_type, set, term
    from .. import entity

from .. import entity

@dataclass
class Relation(entity.Entity):
    # The from [term] of the relation. The term from which the relationship is defined. A null value would indicate the relation is directly with the [set].
    from_term: Optional[term.Term] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The type of relation. Possible values are: pin, reuse.
    relationship: Optional[relation_type.RelationType] = None
    # The [set] in which the relation is relevant.
    set: Optional[set.Set] = None
    # The to [term] of the relation. The term to which the relationship is defined.
    to_term: Optional[term.Term] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Relation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Relation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Relation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import relation_type, set, term
        from .. import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "fromTerm": lambda n : setattr(self, 'from_term', n.get_object_value(term.Term)),
            "relationship": lambda n : setattr(self, 'relationship', n.get_enum_value(relation_type.RelationType)),
            "set": lambda n : setattr(self, 'set', n.get_object_value(set.Set)),
            "toTerm": lambda n : setattr(self, 'to_term', n.get_object_value(term.Term)),
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
        writer.write_object_value("fromTerm", self.from_term)
        writer.write_enum_value("relationship", self.relationship)
        writer.write_object_value("set", self.set)
        writer.write_object_value("toTerm", self.to_term)
    

