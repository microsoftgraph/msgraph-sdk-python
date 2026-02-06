from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity

from ..entity import Entity

@dataclass
class TeamsPolicyUserAssignment(Entity, Parsable):
    # The OdataType property
    odata_type: Optional[str] = None
    # The unique identifier (GUID) of the policy within the specified policy type.
    policy_id: Optional[str] = None
    # The type of Teams policy assigned or unassigned, such as teamsMeetingBroadcastPolicy.
    policy_type: Optional[str] = None
    # The unique identifier (GUID) of the user.
    user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TeamsPolicyUserAssignment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TeamsPolicyUserAssignment
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TeamsPolicyUserAssignment()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity

        from ..entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "policyId": lambda n : setattr(self, 'policy_id', n.get_str_value()),
            "policyType": lambda n : setattr(self, 'policy_type', n.get_str_value()),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
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
        writer.write_str_value("policyId", self.policy_id)
        writer.write_str_value("policyType", self.policy_type)
        writer.write_str_value("userId", self.user_id)
    

