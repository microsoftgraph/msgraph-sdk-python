from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
relation_type = lazy_import('msgraph.generated.models.term_store.relation_type')
set = lazy_import('msgraph.generated.models.term_store.set')
term = lazy_import('msgraph.generated.models.term_store.term')

class Relation(entity.Entity):
    """
    Provides operations to manage the collection of agreement entities.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new relation and sets the default values.
        """
        super().__init__()
        # The from [term] of the relation. The term from which the relationship is defined. A null value would indicate the relation is directly with the [set].
        self._from_term: Optional[term.Term] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The type of relation. Possible values are: pin, reuse.
        self._relationship: Optional[relation_type.RelationType] = None
        # The [set] in which the relation is relevant.
        self._set: Optional[set.Set] = None
        # The to [term] of the relation. The term to which the relationship is defined.
        self._to_term: Optional[term.Term] = None
    
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
    
    @property
    def from_term(self,) -> Optional[term.Term]:
        """
        Gets the fromTerm property value. The from [term] of the relation. The term from which the relationship is defined. A null value would indicate the relation is directly with the [set].
        Returns: Optional[term.Term]
        """
        return self._from_term
    
    @from_term.setter
    def from_term(self,value: Optional[term.Term] = None) -> None:
        """
        Sets the fromTerm property value. The from [term] of the relation. The term from which the relationship is defined. A null value would indicate the relation is directly with the [set].
        Args:
            value: Value to set for the fromTerm property.
        """
        self._from_term = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "from_term": lambda n : setattr(self, 'from_term', n.get_object_value(term.Term)),
            "relationship": lambda n : setattr(self, 'relationship', n.get_enum_value(relation_type.RelationType)),
            "set": lambda n : setattr(self, 'set', n.get_object_value(set.Set)),
            "to_term": lambda n : setattr(self, 'to_term', n.get_object_value(term.Term)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def relationship(self,) -> Optional[relation_type.RelationType]:
        """
        Gets the relationship property value. The type of relation. Possible values are: pin, reuse.
        Returns: Optional[relation_type.RelationType]
        """
        return self._relationship
    
    @relationship.setter
    def relationship(self,value: Optional[relation_type.RelationType] = None) -> None:
        """
        Sets the relationship property value. The type of relation. Possible values are: pin, reuse.
        Args:
            value: Value to set for the relationship property.
        """
        self._relationship = value
    
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
    
    @property
    def set(self,) -> Optional[set.Set]:
        """
        Gets the set property value. The [set] in which the relation is relevant.
        Returns: Optional[set.Set]
        """
        return self._set
    
    @set.setter
    def set(self,value: Optional[set.Set] = None) -> None:
        """
        Sets the set property value. The [set] in which the relation is relevant.
        Args:
            value: Value to set for the set property.
        """
        self._set = value
    
    @property
    def to_term(self,) -> Optional[term.Term]:
        """
        Gets the toTerm property value. The to [term] of the relation. The term to which the relationship is defined.
        Returns: Optional[term.Term]
        """
        return self._to_term
    
    @to_term.setter
    def to_term(self,value: Optional[term.Term] = None) -> None:
        """
        Sets the toTerm property value. The to [term] of the relation. The term to which the relationship is defined.
        Args:
            value: Value to set for the toTerm property.
        """
        self._to_term = value
    

