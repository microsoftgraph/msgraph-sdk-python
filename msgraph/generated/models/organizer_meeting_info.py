from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

identity_set = lazy_import('msgraph.generated.models.identity_set')
meeting_info = lazy_import('msgraph.generated.models.meeting_info')

class OrganizerMeetingInfo(meeting_info.MeetingInfo):
    def __init__(self,) -> None:
        """
        Instantiates a new OrganizerMeetingInfo and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.organizerMeetingInfo"
        # The organizer property
        self._organizer: Optional[identity_set.IdentitySet] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OrganizerMeetingInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OrganizerMeetingInfo
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return OrganizerMeetingInfo()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "organizer": lambda n : setattr(self, 'organizer', n.get_object_value(identity_set.IdentitySet)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def organizer(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the organizer property value. The organizer property
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._organizer
    
    @organizer.setter
    def organizer(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the organizer property value. The organizer property
        Args:
            value: Value to set for the organizer property.
        """
        self._organizer = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("organizer", self.organizer)
    

