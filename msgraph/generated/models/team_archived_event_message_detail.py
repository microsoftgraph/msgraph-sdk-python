from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import event_message_detail, identity_set

from . import event_message_detail

class TeamArchivedEventMessageDetail(event_message_detail.EventMessageDetail):
    def __init__(self,) -> None:
        """
        Instantiates a new TeamArchivedEventMessageDetail and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.teamArchivedEventMessageDetail"
        # Initiator of the event.
        self._initiator: Optional[identity_set.IdentitySet] = None
        # Unique identifier of the team.
        self._team_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamArchivedEventMessageDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TeamArchivedEventMessageDetail
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TeamArchivedEventMessageDetail()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import event_message_detail, identity_set

        fields: Dict[str, Callable[[Any], None]] = {
            "initiator": lambda n : setattr(self, 'initiator', n.get_object_value(identity_set.IdentitySet)),
            "teamId": lambda n : setattr(self, 'team_id', n.get_str_value()),
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
        writer.write_str_value("teamId", self.team_id)
    
    @property
    def team_id(self,) -> Optional[str]:
        """
        Gets the teamId property value. Unique identifier of the team.
        Returns: Optional[str]
        """
        return self._team_id
    
    @team_id.setter
    def team_id(self,value: Optional[str] = None) -> None:
        """
        Sets the teamId property value. Unique identifier of the team.
        Args:
            value: Value to set for the team_id property.
        """
        self._team_id = value
    

