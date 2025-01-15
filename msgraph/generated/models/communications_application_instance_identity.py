from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .identity import Identity

from .identity import Identity

@dataclass
class CommunicationsApplicationInstanceIdentity(Identity, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.communicationsApplicationInstanceIdentity"
    # True if the participant shouldn't be shown in other participants' rosters.
    hidden: Optional[bool] = None
    # The tenant ID of the application.
    tenant_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CommunicationsApplicationInstanceIdentity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CommunicationsApplicationInstanceIdentity
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CommunicationsApplicationInstanceIdentity()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .identity import Identity

        from .identity import Identity

        fields: dict[str, Callable[[Any], None]] = {
            "hidden": lambda n : setattr(self, 'hidden', n.get_bool_value()),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
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
        writer.write_bool_value("hidden", self.hidden)
        writer.write_str_value("tenantId", self.tenant_id)
    

