from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .meeting_participant_info import MeetingParticipantInfo
    from .virtual_event_presenter_details import VirtualEventPresenterDetails

from .meeting_participant_info import MeetingParticipantInfo

@dataclass
class VirtualEventPresenterInfo(MeetingParticipantInfo, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.virtualEventPresenterInfo"
    # The presenterDetails property
    presenter_details: Optional[VirtualEventPresenterDetails] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> VirtualEventPresenterInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: VirtualEventPresenterInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return VirtualEventPresenterInfo()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .meeting_participant_info import MeetingParticipantInfo
        from .virtual_event_presenter_details import VirtualEventPresenterDetails

        from .meeting_participant_info import MeetingParticipantInfo
        from .virtual_event_presenter_details import VirtualEventPresenterDetails

        fields: Dict[str, Callable[[Any], None]] = {
            "presenterDetails": lambda n : setattr(self, 'presenter_details', n.get_object_value(VirtualEventPresenterDetails)),
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
        from .meeting_participant_info import MeetingParticipantInfo
        from .virtual_event_presenter_details import VirtualEventPresenterDetails

        writer.write_object_value("presenterDetails", self.presenter_details)
    

