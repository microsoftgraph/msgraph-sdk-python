from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .details_info import DetailsInfo
    from .identity import Identity

from .identity import Identity

@dataclass
class ProvisioningSystem(Identity, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.provisioningSystem"
    # Details of the system.
    details: Optional[DetailsInfo] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ProvisioningSystem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ProvisioningSystem
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ProvisioningSystem()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .details_info import DetailsInfo
        from .identity import Identity

        from .details_info import DetailsInfo
        from .identity import Identity

        fields: dict[str, Callable[[Any], None]] = {
            "details": lambda n : setattr(self, 'details', n.get_object_value(DetailsInfo)),
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
        writer.write_object_value("details", self.details)
    

