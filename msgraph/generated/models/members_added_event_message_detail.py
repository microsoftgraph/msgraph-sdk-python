from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

event_message_detail = lazy_import('msgraph.generated.models.event_message_detail')
identity_set = lazy_import('msgraph.generated.models.identity_set')
teamwork_user_identity = lazy_import('msgraph.generated.models.teamwork_user_identity')

class MembersAddedEventMessageDetail(event_message_detail.EventMessageDetail):
    def __init__(self,) -> None:
        """
        Instantiates a new MembersAddedEventMessageDetail and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.membersAddedEventMessageDetail"
        # Initiator of the event.
        self._initiator: Optional[identity_set.IdentitySet] = None
        # List of members added.
        self._members: Optional[List[teamwork_user_identity.TeamworkUserIdentity]] = None
        # The timestamp that denotes how far back a conversation's history is shared with the conversation members.
        self._visible_history_start_date_time: Optional[datetime] = None
    
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
        fields = {
            "initiator": lambda n : setattr(self, 'initiator', n.get_object_value(identity_set.IdentitySet)),
            "members": lambda n : setattr(self, 'members', n.get_collection_of_object_values(teamwork_user_identity.TeamworkUserIdentity)),
            "visible_history_start_date_time": lambda n : setattr(self, 'visible_history_start_date_time', n.get_datetime_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def initiator(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the initiator property value. Initiator of the event.
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._initiator
    
    @initiator.setter
    def initiator(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the initiator property value. Initiator of the event.
        Args:
            value: Value to set for the initiator property.
        """
        self._initiator = value
    
    @property
    def members(self,) -> Optional[List[teamwork_user_identity.TeamworkUserIdentity]]:
        """
        Gets the members property value. List of members added.
        Returns: Optional[List[teamwork_user_identity.TeamworkUserIdentity]]
        """
        return self._members
    
    @members.setter
    def members(self,value: Optional[List[teamwork_user_identity.TeamworkUserIdentity]] = None) -> None:
        """
        Sets the members property value. List of members added.
        Args:
            value: Value to set for the members property.
        """
        self._members = value
    
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
    
    @property
    def visible_history_start_date_time(self,) -> Optional[datetime]:
        """
        Gets the visibleHistoryStartDateTime property value. The timestamp that denotes how far back a conversation's history is shared with the conversation members.
        Returns: Optional[datetime]
        """
        return self._visible_history_start_date_time
    
    @visible_history_start_date_time.setter
    def visible_history_start_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the visibleHistoryStartDateTime property value. The timestamp that denotes how far back a conversation's history is shared with the conversation members.
        Args:
            value: Value to set for the visibleHistoryStartDateTime property.
        """
        self._visible_history_start_date_time = value
    

