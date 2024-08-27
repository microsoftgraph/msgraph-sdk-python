from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .identity import Identity

from .identity import Identity

@dataclass
class CommunicationsApplicationIdentity(Identity):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.communicationsApplicationIdentity"
    # First-party Microsoft application that presents this identity.
    application_type: Optional[str] = None
    # True if the participant shouldn't be shown in other participants' rosters.
    hidden: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CommunicationsApplicationIdentity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CommunicationsApplicationIdentity
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CommunicationsApplicationIdentity()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .identity import Identity

        from .identity import Identity

        fields: Dict[str, Callable[[Any], None]] = {
            "applicationType": lambda n : setattr(self, 'application_type', n.get_str_value()),
            "hidden": lambda n : setattr(self, 'hidden', n.get_bool_value()),
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
        writer.write_str_value("applicationType", self.application_type)
        writer.write_bool_value("hidden", self.hidden)
    

