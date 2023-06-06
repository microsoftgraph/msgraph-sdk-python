from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import bitlocker_recovery_key, entity

from . import entity

@dataclass
class Bitlocker(entity.Entity):
    # The OdataType property
    odata_type: Optional[str] = None
    # The recovery keys associated with the bitlocker entity.
    recovery_keys: Optional[List[bitlocker_recovery_key.BitlockerRecoveryKey]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Bitlocker:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Bitlocker
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Bitlocker()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import bitlocker_recovery_key, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "recoveryKeys": lambda n : setattr(self, 'recovery_keys', n.get_collection_of_object_values(bitlocker_recovery_key.BitlockerRecoveryKey)),
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
        writer.write_collection_of_object_values("recoveryKeys", self.recovery_keys)
    

