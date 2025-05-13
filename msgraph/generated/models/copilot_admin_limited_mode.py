from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class CopilotAdminLimitedMode(Entity, Parsable):
    # The ID of a Microsoft Entra group, for which the value of isEnabledForGroup is applied. The default value is null. If isEnabledForGroup is set to true, the groupId value must be provided for the Copilot limited mode in Teams meetings to be enabled for the members of the group. Optional.
    group_id: Optional[str] = None
    # Enables the user to be in limited mode for Copilot in Teams meetings. When copilotAdminLimitedMode=true, users in this mode can ask any questions, but Copilot doesn't respond to certain questions related to inferring emotions, behavior, or judgments. When copilotAdminLimitedMode=false, it responds to all types of questions grounded to the meeting conversation. The default value is false.
    is_enabled_for_group: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CopilotAdminLimitedMode:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CopilotAdminLimitedMode
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CopilotAdminLimitedMode()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "groupId": lambda n : setattr(self, 'group_id', n.get_str_value()),
            "isEnabledForGroup": lambda n : setattr(self, 'is_enabled_for_group', n.get_bool_value()),
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
        writer.write_str_value("groupId", self.group_id)
        writer.write_bool_value("isEnabledForGroup", self.is_enabled_for_group)
    

