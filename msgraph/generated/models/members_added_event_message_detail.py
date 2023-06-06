from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import event_message_detail, identity_set, teamwork_user_identity

from . import event_message_detail

@dataclass
class MembersAddedEventMessageDetail(event_message_detail.EventMessageDetail):
    odata_type = "#microsoft.graph.membersAddedEventMessageDetail"
    # Initiator of the event.
    initiator: Optional[identity_set.IdentitySet] = None
    # List of members added.
    members: Optional[List[teamwork_user_identity.TeamworkUserIdentity]] = None
    # The timestamp that denotes how far back a conversation's history is shared with the conversation members.
    visible_history_start_date_time: Optional[datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MembersAddedEventMessageDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MembersAddedEventMessageDetail
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MembersAddedEventMessageDetail()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import event_message_detail, identity_set, teamwork_user_identity

        fields: Dict[str, Callable[[Any], None]] = {
            "initiator": lambda n : setattr(self, 'initiator', n.get_object_value(identity_set.IdentitySet)),
            "members": lambda n : setattr(self, 'members', n.get_collection_of_object_values(teamwork_user_identity.TeamworkUserIdentity)),
            "visibleHistoryStartDateTime": lambda n : setattr(self, 'visible_history_start_date_time', n.get_datetime_value()),
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
        writer.write_object_value("initiator", self.initiator)
        writer.write_collection_of_object_values("members", self.members)
        writer.write_datetime_value("visibleHistoryStartDateTime", self.visible_history_start_date_time)
    

