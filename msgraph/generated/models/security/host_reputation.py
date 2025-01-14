from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .host_reputation_classification import HostReputationClassification
    from .host_reputation_rule import HostReputationRule

from ..entity import Entity

@dataclass
class HostReputation(Entity, Parsable):
    # The classification property
    classification: Optional[HostReputationClassification] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # A collection of rules that have been used to calculate the classification and score.
    rules: Optional[list[HostReputationRule]] = None
    # The calculated score (0-100) of the requested host. A higher value indicates that this host is more likely to be suspicious or malicious.
    score: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> HostReputation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: HostReputation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return HostReputation()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .host_reputation_classification import HostReputationClassification
        from .host_reputation_rule import HostReputationRule

        from ..entity import Entity
        from .host_reputation_classification import HostReputationClassification
        from .host_reputation_rule import HostReputationRule

        fields: dict[str, Callable[[Any], None]] = {
            "classification": lambda n : setattr(self, 'classification', n.get_enum_value(HostReputationClassification)),
            "rules": lambda n : setattr(self, 'rules', n.get_collection_of_object_values(HostReputationRule)),
            "score": lambda n : setattr(self, 'score', n.get_int_value()),
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
        writer.write_enum_value("classification", self.classification)
        writer.write_collection_of_object_values("rules", self.rules)
        writer.write_int_value("score", self.score)
    

