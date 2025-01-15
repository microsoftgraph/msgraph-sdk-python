from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .virtual_event_registration_configuration import VirtualEventRegistrationConfiguration

from .virtual_event_registration_configuration import VirtualEventRegistrationConfiguration

@dataclass
class VirtualEventWebinarRegistrationConfiguration(VirtualEventRegistrationConfiguration, Parsable):
    # The isManualApprovalEnabled property
    is_manual_approval_enabled: Optional[bool] = None
    # The isWaitlistEnabled property
    is_waitlist_enabled: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> VirtualEventWebinarRegistrationConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: VirtualEventWebinarRegistrationConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return VirtualEventWebinarRegistrationConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .virtual_event_registration_configuration import VirtualEventRegistrationConfiguration

        from .virtual_event_registration_configuration import VirtualEventRegistrationConfiguration

        fields: dict[str, Callable[[Any], None]] = {
            "isManualApprovalEnabled": lambda n : setattr(self, 'is_manual_approval_enabled', n.get_bool_value()),
            "isWaitlistEnabled": lambda n : setattr(self, 'is_waitlist_enabled', n.get_bool_value()),
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
        writer.write_bool_value("isManualApprovalEnabled", self.is_manual_approval_enabled)
        writer.write_bool_value("isWaitlistEnabled", self.is_waitlist_enabled)
    

