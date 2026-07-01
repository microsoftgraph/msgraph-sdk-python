from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .directory_object import DirectoryObject
    from .validating_domains import ValidatingDomains

from .directory_object import DirectoryObject

@dataclass
class FederatedTokenValidationPolicy(DirectoryObject, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.federatedTokenValidationPolicy"
    # The validatingDomains property
    validating_domains: Optional[ValidatingDomains] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FederatedTokenValidationPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FederatedTokenValidationPolicy
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return FederatedTokenValidationPolicy()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .directory_object import DirectoryObject
        from .validating_domains import ValidatingDomains

        from .directory_object import DirectoryObject
        from .validating_domains import ValidatingDomains

        fields: dict[str, Callable[[Any], None]] = {
            "validatingDomains": lambda n : setattr(self, 'validating_domains', n.get_object_value(ValidatingDomains)),
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
        writer.write_object_value("validatingDomains", self.validating_domains)
    

