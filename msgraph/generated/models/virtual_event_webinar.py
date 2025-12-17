from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .communications_user_identity import CommunicationsUserIdentity
    from .meeting_audience import MeetingAudience
    from .virtual_event import VirtualEvent
    from .virtual_event_registration import VirtualEventRegistration
    from .virtual_event_webinar_registration_configuration import VirtualEventWebinarRegistrationConfiguration

from .virtual_event import VirtualEvent

@dataclass
class VirtualEventWebinar(VirtualEvent, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.virtualEventWebinar"
    # To whom the webinar is visible. The possible values are: everyone, organization, and unknownFutureValue.
    audience: Optional[MeetingAudience] = None
    # Identity information of coorganizers of the webinar.
    co_organizers: Optional[list[CommunicationsUserIdentity]] = None
    # Registration configuration of the webinar.
    registration_configuration: Optional[VirtualEventWebinarRegistrationConfiguration] = None
    # Registration records of the webinar.
    registrations: Optional[list[VirtualEventRegistration]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> VirtualEventWebinar:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: VirtualEventWebinar
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return VirtualEventWebinar()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .communications_user_identity import CommunicationsUserIdentity
        from .meeting_audience import MeetingAudience
        from .virtual_event import VirtualEvent
        from .virtual_event_registration import VirtualEventRegistration
        from .virtual_event_webinar_registration_configuration import VirtualEventWebinarRegistrationConfiguration

        from .communications_user_identity import CommunicationsUserIdentity
        from .meeting_audience import MeetingAudience
        from .virtual_event import VirtualEvent
        from .virtual_event_registration import VirtualEventRegistration
        from .virtual_event_webinar_registration_configuration import VirtualEventWebinarRegistrationConfiguration

        fields: dict[str, Callable[[Any], None]] = {
            "audience": lambda n : setattr(self, 'audience', n.get_enum_value(MeetingAudience)),
            "coOrganizers": lambda n : setattr(self, 'co_organizers', n.get_collection_of_object_values(CommunicationsUserIdentity)),
            "registrationConfiguration": lambda n : setattr(self, 'registration_configuration', n.get_object_value(VirtualEventWebinarRegistrationConfiguration)),
            "registrations": lambda n : setattr(self, 'registrations', n.get_collection_of_object_values(VirtualEventRegistration)),
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
        writer.write_enum_value("audience", self.audience)
        writer.write_collection_of_object_values("coOrganizers", self.co_organizers)
        writer.write_object_value("registrationConfiguration", self.registration_configuration)
        writer.write_collection_of_object_values("registrations", self.registrations)
    

