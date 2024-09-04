from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authentication_combination_configuration import AuthenticationCombinationConfiguration

from .authentication_combination_configuration import AuthenticationCombinationConfiguration

@dataclass
class X509CertificateCombinationConfiguration(AuthenticationCombinationConfiguration):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.x509CertificateCombinationConfiguration"
    # A list of allowed subject key identifier values.
    allowed_issuer_skis: Optional[List[str]] = None
    # A list of allowed policy OIDs.
    allowed_policy_o_i_ds: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> X509CertificateCombinationConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: X509CertificateCombinationConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return X509CertificateCombinationConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .authentication_combination_configuration import AuthenticationCombinationConfiguration

        from .authentication_combination_configuration import AuthenticationCombinationConfiguration

        fields: Dict[str, Callable[[Any], None]] = {
            "allowedIssuerSkis": lambda n : setattr(self, 'allowed_issuer_skis', n.get_collection_of_primitive_values(str)),
            "allowedPolicyOIDs": lambda n : setattr(self, 'allowed_policy_o_i_ds', n.get_collection_of_primitive_values(str)),
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
        writer.write_collection_of_primitive_values("allowedIssuerSkis", self.allowed_issuer_skis)
        writer.write_collection_of_primitive_values("allowedPolicyOIDs", self.allowed_policy_o_i_ds)
    

