from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .communications_user_identity import CommunicationsUserIdentity
    from .identity import Identity
    from .meeting_audience import MeetingAudience
    from .virtual_event import VirtualEvent

from .virtual_event import VirtualEvent

@dataclass
class VirtualEventTownhall(VirtualEvent, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.virtualEventTownhall"
    # The audience to whom the town hall is visible. The possible values are: everyone, organization, and unknownFutureValue.
    audience: Optional[MeetingAudience] = None
    # Identity information of the coorganizers of the town hall.
    co_organizers: Optional[list[CommunicationsUserIdentity]] = None
    # The attendees invited to the town hall. The supported identities are: communicationsUserIdentity and communicationsGuestIdentity.
    invited_attendees: Optional[list[Identity]] = None
    # Indicates whether the town hall is only open to invited people and groups within your organization. The isInviteOnly property can only be true if the value of the audience property is set to organization.
    is_invite_only: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> VirtualEventTownhall:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: VirtualEventTownhall
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return VirtualEventTownhall()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .communications_user_identity import CommunicationsUserIdentity
        from .identity import Identity
        from .meeting_audience import MeetingAudience
        from .virtual_event import VirtualEvent

        from .communications_user_identity import CommunicationsUserIdentity
        from .identity import Identity
        from .meeting_audience import MeetingAudience
        from .virtual_event import VirtualEvent

        fields: dict[str, Callable[[Any], None]] = {
            "audience": lambda n : setattr(self, 'audience', n.get_enum_value(MeetingAudience)),
            "coOrganizers": lambda n : setattr(self, 'co_organizers', n.get_collection_of_object_values(CommunicationsUserIdentity)),
            "invitedAttendees": lambda n : setattr(self, 'invited_attendees', n.get_collection_of_object_values(Identity)),
            "isInviteOnly": lambda n : setattr(self, 'is_invite_only', n.get_bool_value()),
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
        writer.write_collection_of_object_values("invitedAttendees", self.invited_attendees)
        writer.write_bool_value("isInviteOnly", self.is_invite_only)
    

