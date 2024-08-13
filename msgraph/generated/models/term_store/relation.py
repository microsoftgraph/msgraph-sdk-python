from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .relation_type import RelationType
    from .set import Set
    from .term import Term

from ..entity import Entity

@dataclass
class Relation(Entity):
    # The from [term] of the relation. The term from which the relationship is defined. A null value would indicate the relation is directly with the [set].
    from_term: Optional[Term] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The type of relation. Possible values are: pin, reuse.
    relationship: Optional[RelationType] = None
    # The [set] in which the relation is relevant.
    set: Optional[Set] = None
    # The to [term] of the relation. The term to which the relationship is defined.
    to_term: Optional[Term] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Relation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Relation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Relation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .relation_type import RelationType
        from .set import Set
        from .term import Term

        from ..entity import Entity
        from .relation_type import RelationType
        from .set import Set
        from .term import Term

        fields: Dict[str, Callable[[Any], None]] = {
            "fromTerm": lambda n : setattr(self, 'from_term', n.get_object_value(Term)),
            "relationship": lambda n : setattr(self, 'relationship', n.get_enum_value(RelationType)),
            "set": lambda n : setattr(self, 'set', n.get_object_value(Set)),
            "toTerm": lambda n : setattr(self, 'to_term', n.get_object_value(Term)),
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
        writer.write_object_value("fromTerm", self.from_term)
        writer.write_enum_value("relationship", self.relationship)
        writer.write_object_value("set", self.set)
        writer.write_object_value("toTerm", self.to_term)
    

