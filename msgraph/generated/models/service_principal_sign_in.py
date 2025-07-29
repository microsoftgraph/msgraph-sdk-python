from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .sign_in_identity import SignInIdentity

from .sign_in_identity import SignInIdentity

@dataclass
class ServicePrincipalSignIn(SignInIdentity, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.servicePrincipalSignIn"
    # appId of the service principal that is signing in.
    service_principal_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ServicePrincipalSignIn:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ServicePrincipalSignIn
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ServicePrincipalSignIn()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .sign_in_identity import SignInIdentity

        from .sign_in_identity import SignInIdentity

        fields: dict[str, Callable[[Any], None]] = {
            "servicePrincipalId": lambda n : setattr(self, 'service_principal_id', n.get_str_value()),
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
        writer.write_str_value("servicePrincipalId", self.service_principal_id)
    

