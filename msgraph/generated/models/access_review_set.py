from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import access_review_history_definition, access_review_schedule_definition, entity

from . import entity

@dataclass
class AccessReviewSet(entity.Entity):
    # Represents the template and scheduling for an access review.
    definitions: Optional[List[access_review_schedule_definition.AccessReviewScheduleDefinition]] = None
    # Represents a collection of access review history data and the scopes used to collect that data.
    history_definitions: Optional[List[access_review_history_definition.AccessReviewHistoryDefinition]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessReviewSet:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessReviewSet
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AccessReviewSet()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import access_review_history_definition, access_review_schedule_definition, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "definitions": lambda n : setattr(self, 'definitions', n.get_collection_of_object_values(access_review_schedule_definition.AccessReviewScheduleDefinition)),
            "historyDefinitions": lambda n : setattr(self, 'history_definitions', n.get_collection_of_object_values(access_review_history_definition.AccessReviewHistoryDefinition)),
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
        writer.write_collection_of_object_values("definitions", self.definitions)
        writer.write_collection_of_object_values("historyDefinitions", self.history_definitions)
    

