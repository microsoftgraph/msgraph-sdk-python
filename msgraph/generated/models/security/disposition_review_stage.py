from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity

from ..entity import Entity

@dataclass
class DispositionReviewStage(Entity, Parsable):
    # Name representing each stage within a collection.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # A collection of reviewers at each stage.
    reviewers_email_addresses: Optional[list[str]] = None
    # The unique sequence number for each stage of the disposition review.
    stage_number: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DispositionReviewStage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DispositionReviewStage
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DispositionReviewStage()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity

        from ..entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "reviewersEmailAddresses": lambda n : setattr(self, 'reviewers_email_addresses', n.get_collection_of_primitive_values(str)),
            "stageNumber": lambda n : setattr(self, 'stage_number', n.get_str_value()),
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
        writer.write_str_value("name", self.name)
        writer.write_collection_of_primitive_values("reviewersEmailAddresses", self.reviewers_email_addresses)
        writer.write_str_value("stageNumber", self.stage_number)
    

