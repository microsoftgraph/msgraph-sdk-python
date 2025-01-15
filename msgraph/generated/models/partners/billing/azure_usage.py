from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ...entity import Entity
    from .billed_usage import BilledUsage
    from .unbilled_usage import UnbilledUsage

from ...entity import Entity

@dataclass
class AzureUsage(Entity, Parsable):
    # The billed property
    billed: Optional[BilledUsage] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The unbilled property
    unbilled: Optional[UnbilledUsage] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AzureUsage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AzureUsage
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AzureUsage()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ...entity import Entity
        from .billed_usage import BilledUsage
        from .unbilled_usage import UnbilledUsage

        from ...entity import Entity
        from .billed_usage import BilledUsage
        from .unbilled_usage import UnbilledUsage

        fields: dict[str, Callable[[Any], None]] = {
            "billed": lambda n : setattr(self, 'billed', n.get_object_value(BilledUsage)),
            "unbilled": lambda n : setattr(self, 'unbilled', n.get_object_value(UnbilledUsage)),
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
        writer.write_object_value("billed", self.billed)
        writer.write_object_value("unbilled", self.unbilled)
    

