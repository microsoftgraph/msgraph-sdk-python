from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .fraud_protection_configuration import FraudProtectionConfiguration
    from .on_fraud_protection_load_start_handler import OnFraudProtectionLoadStartHandler

from .on_fraud_protection_load_start_handler import OnFraudProtectionLoadStartHandler

@dataclass
class OnFraudProtectionLoadStartExternalUsersAuthHandler(OnFraudProtectionLoadStartHandler, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.onFraudProtectionLoadStartExternalUsersAuthHandler"
    # Specifies the fraud protection configuration for sign-up events.
    sign_up: Optional[FraudProtectionConfiguration] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OnFraudProtectionLoadStartExternalUsersAuthHandler:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OnFraudProtectionLoadStartExternalUsersAuthHandler
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OnFraudProtectionLoadStartExternalUsersAuthHandler()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .fraud_protection_configuration import FraudProtectionConfiguration
        from .on_fraud_protection_load_start_handler import OnFraudProtectionLoadStartHandler

        from .fraud_protection_configuration import FraudProtectionConfiguration
        from .on_fraud_protection_load_start_handler import OnFraudProtectionLoadStartHandler

        fields: dict[str, Callable[[Any], None]] = {
            "signUp": lambda n : setattr(self, 'sign_up', n.get_object_value(FraudProtectionConfiguration)),
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
        writer.write_object_value("signUp", self.sign_up)
    

