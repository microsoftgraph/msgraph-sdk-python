from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .comms_operation import CommsOperation
    from .send_dtmf_completion_reason import SendDtmfCompletionReason

from .comms_operation import CommsOperation

@dataclass
class SendDtmfTonesOperation(CommsOperation, Parsable):
    # The results of the action. Possible values are: unknown, completedSuccessfully, mediaOperationCanceled, unknownfutureValue.
    completion_reason: Optional[SendDtmfCompletionReason] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SendDtmfTonesOperation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SendDtmfTonesOperation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SendDtmfTonesOperation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .comms_operation import CommsOperation
        from .send_dtmf_completion_reason import SendDtmfCompletionReason

        from .comms_operation import CommsOperation
        from .send_dtmf_completion_reason import SendDtmfCompletionReason

        fields: Dict[str, Callable[[Any], None]] = {
            "completionReason": lambda n : setattr(self, 'completion_reason', n.get_enum_value(SendDtmfCompletionReason)),
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
        from .comms_operation import CommsOperation
        from .send_dtmf_completion_reason import SendDtmfCompletionReason

        writer.write_enum_value("completionReason", self.completion_reason)
    

