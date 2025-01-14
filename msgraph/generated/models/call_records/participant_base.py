from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..communications_identity_set import CommunicationsIdentitySet
    from ..entity import Entity
    from .administrative_unit_info import AdministrativeUnitInfo
    from .organizer import Organizer
    from .participant import Participant

from ..entity import Entity

@dataclass
class ParticipantBase(Entity, Parsable):
    # List of administrativeUnitInfo objects for the call participant.
    administrative_unit_infos: Optional[list[AdministrativeUnitInfo]] = None
    # The identity of the call participant.
    identity: Optional[CommunicationsIdentitySet] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ParticipantBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ParticipantBase
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.callRecords.organizer".casefold():
            from .organizer import Organizer

            return Organizer()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.callRecords.participant".casefold():
            from .participant import Participant

            return Participant()
        return ParticipantBase()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..communications_identity_set import CommunicationsIdentitySet
        from ..entity import Entity
        from .administrative_unit_info import AdministrativeUnitInfo
        from .organizer import Organizer
        from .participant import Participant

        from ..communications_identity_set import CommunicationsIdentitySet
        from ..entity import Entity
        from .administrative_unit_info import AdministrativeUnitInfo
        from .organizer import Organizer
        from .participant import Participant

        fields: dict[str, Callable[[Any], None]] = {
            "administrativeUnitInfos": lambda n : setattr(self, 'administrative_unit_infos', n.get_collection_of_object_values(AdministrativeUnitInfo)),
            "identity": lambda n : setattr(self, 'identity', n.get_object_value(CommunicationsIdentitySet)),
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
        writer.write_collection_of_object_values("administrativeUnitInfos", self.administrative_unit_infos)
        writer.write_object_value("identity", self.identity)
    

