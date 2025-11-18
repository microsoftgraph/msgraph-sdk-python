from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .fraud_protection_provider import FraudProtectionProvider

from .fraud_protection_provider import FraudProtectionProvider

@dataclass
class ArkoseFraudProtectionProvider(FraudProtectionProvider, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.arkoseFraudProtectionProvider"
    # Used to invoke the Arkose service from the client application. Request from your Arkose Customer Success Manager or use the default client-api value.
    client_sub_domain: Optional[str] = None
    # The private key available on the Arkose Portal. Contact your Arkose Customer Success Manager for assistance with your keys.
    private_key: Optional[str] = None
    # The public key available on the Arkose Portal. Contact your Arkose Customer Success Manager for assistance with your keys.
    public_key: Optional[str] = None
    # Used to invoke the Arkose service from the Microsoft authentication server. Request from your Arkose Customer Success Manager or use the default verify-api value.
    verify_sub_domain: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ArkoseFraudProtectionProvider:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ArkoseFraudProtectionProvider
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ArkoseFraudProtectionProvider()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .fraud_protection_provider import FraudProtectionProvider

        from .fraud_protection_provider import FraudProtectionProvider

        fields: dict[str, Callable[[Any], None]] = {
            "clientSubDomain": lambda n : setattr(self, 'client_sub_domain', n.get_str_value()),
            "privateKey": lambda n : setattr(self, 'private_key', n.get_str_value()),
            "publicKey": lambda n : setattr(self, 'public_key', n.get_str_value()),
            "verifySubDomain": lambda n : setattr(self, 'verify_sub_domain', n.get_str_value()),
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
        writer.write_str_value("clientSubDomain", self.client_sub_domain)
        writer.write_str_value("privateKey", self.private_key)
        writer.write_str_value("publicKey", self.public_key)
        writer.write_str_value("verifySubDomain", self.verify_sub_domain)
    

