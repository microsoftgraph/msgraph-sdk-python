from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ......models.evaluation_outcome import EvaluationOutcome
    from ......models.request_schedule import RequestSchedule

@dataclass
class UpdateRequestPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The evaluationId property
    evaluation_id: Optional[str] = None
    # The evaluationOutcome property
    evaluation_outcome: Optional[EvaluationOutcome] = None
    # The reason property
    reason: Optional[str] = None
    # The scheduleInfo property
    schedule_info: Optional[RequestSchedule] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UpdateRequestPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UpdateRequestPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UpdateRequestPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ......models.evaluation_outcome import EvaluationOutcome
        from ......models.request_schedule import RequestSchedule

        from ......models.evaluation_outcome import EvaluationOutcome
        from ......models.request_schedule import RequestSchedule

        fields: dict[str, Callable[[Any], None]] = {
            "evaluationId": lambda n : setattr(self, 'evaluation_id', n.get_str_value()),
            "evaluationOutcome": lambda n : setattr(self, 'evaluation_outcome', n.get_enum_value(EvaluationOutcome)),
            "reason": lambda n : setattr(self, 'reason', n.get_str_value()),
            "scheduleInfo": lambda n : setattr(self, 'schedule_info', n.get_object_value(RequestSchedule)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("evaluationId", self.evaluation_id)
        writer.write_enum_value("evaluationOutcome", self.evaluation_outcome)
        writer.write_str_value("reason", self.reason)
        writer.write_object_value("scheduleInfo", self.schedule_info)
        writer.write_additional_data_value(self.additional_data)
    

