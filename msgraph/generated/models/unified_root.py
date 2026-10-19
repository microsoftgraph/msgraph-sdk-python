from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_review_instance import AccessReviewInstance
    from .access_review_instance_decision_item import AccessReviewInstanceDecisionItem
    from .access_review_schedule_definition import AccessReviewScheduleDefinition
    from .entity import Entity

from .entity import Entity

@dataclass
class UnifiedRoot(Entity, Parsable):
    # Represents the unified (vNext) access review decisions on an instance of a review.
    decisions: Optional[list[AccessReviewInstanceDecisionItem]] = None
    # Represents the unified (vNext) template and scheduling for an access review.
    definitions: Optional[list[AccessReviewScheduleDefinition]] = None
    # Represents the unified (vNext) instance of a review.
    instances: Optional[list[AccessReviewInstance]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UnifiedRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UnifiedRoot
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UnifiedRoot()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .access_review_instance import AccessReviewInstance
        from .access_review_instance_decision_item import AccessReviewInstanceDecisionItem
        from .access_review_schedule_definition import AccessReviewScheduleDefinition
        from .entity import Entity

        from .access_review_instance import AccessReviewInstance
        from .access_review_instance_decision_item import AccessReviewInstanceDecisionItem
        from .access_review_schedule_definition import AccessReviewScheduleDefinition
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "decisions": lambda n : setattr(self, 'decisions', n.get_collection_of_object_values(AccessReviewInstanceDecisionItem)),
            "definitions": lambda n : setattr(self, 'definitions', n.get_collection_of_object_values(AccessReviewScheduleDefinition)),
            "instances": lambda n : setattr(self, 'instances', n.get_collection_of_object_values(AccessReviewInstance)),
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
        writer.write_collection_of_object_values("decisions", self.decisions)
        writer.write_collection_of_object_values("definitions", self.definitions)
        writer.write_collection_of_object_values("instances", self.instances)
    

