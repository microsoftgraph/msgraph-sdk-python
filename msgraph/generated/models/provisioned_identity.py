from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .details_info import DetailsInfo
    from .identity import Identity

from .identity import Identity

@dataclass
class ProvisionedIdentity(Identity, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.provisionedIdentity"
    # Details of the identity.
    details: Optional[DetailsInfo] = None
    # Type of identity that has been provisioned, such as 'user' or 'group'. Supports $filter (eq, contains).
    identity_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ProvisionedIdentity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ProvisionedIdentity
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ProvisionedIdentity()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .details_info import DetailsInfo
        from .identity import Identity

        from .details_info import DetailsInfo
        from .identity import Identity

        fields: Dict[str, Callable[[Any], None]] = {
            "details": lambda n : setattr(self, 'details', n.get_object_value(DetailsInfo)),
            "identityType": lambda n : setattr(self, 'identity_type', n.get_str_value()),
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
        from .details_info import DetailsInfo
        from .identity import Identity

        writer.write_object_value("details", self.details)
        writer.write_str_value("identityType", self.identity_type)
    

