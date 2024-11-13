from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .comms_operation import CommsOperation

from .comms_operation import CommsOperation

@dataclass
class RecordOperation(CommsOperation, Parsable):
    # The OdataType property
    odata_type: Optional[str] = None
    # The access token required to retrieve the recording.
    recording_access_token: Optional[str] = None
    # The location where the recording is located.
    recording_location: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RecordOperation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RecordOperation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RecordOperation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .comms_operation import CommsOperation

        from .comms_operation import CommsOperation

        fields: Dict[str, Callable[[Any], None]] = {
            "recordingAccessToken": lambda n : setattr(self, 'recording_access_token', n.get_str_value()),
            "recordingLocation": lambda n : setattr(self, 'recording_location', n.get_str_value()),
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

        writer.write_str_value("recordingAccessToken", self.recording_access_token)
        writer.write_str_value("recordingLocation", self.recording_location)
    

