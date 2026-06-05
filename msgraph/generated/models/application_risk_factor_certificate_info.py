from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class ApplicationRiskFactorCertificateInfo(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Indicates whether the certificate's common name doesn't match the expected domain name.
    has_bad_common_name: Optional[bool] = None
    # Indicates whether the certificate uses a weak or insecure signature algorithm (for example, MD5 or SHA-1).
    has_insecure_signature: Optional[bool] = None
    # Indicates whether the certificate chain of trust is incomplete or invalid.
    has_no_chain_of_trust: Optional[bool] = None
    # Indicates whether the certificate is on a known denylist or associated with compromised issuers.
    is_denylisted: Optional[bool] = None
    # Indicates whether the certificate's hostname doesn't match the domain it was issued for.
    is_hostname_mismatch: Optional[bool] = None
    # Indicates whether the certificate is expired and no longer valid.
    is_not_after: Optional[bool] = None
    # Indicates whether the certificate isn't yet valid based on its activation date.
    is_not_before: Optional[bool] = None
    # Indicates whether the issuing certificate authority revoked the certificate.
    is_revoked: Optional[bool] = None
    # Indicates whether the certificate is self-signed rather than issued by a trusted certificate authority.
    is_self_signed: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ApplicationRiskFactorCertificateInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ApplicationRiskFactorCertificateInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ApplicationRiskFactorCertificateInfo()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "hasBadCommonName": lambda n : setattr(self, 'has_bad_common_name', n.get_bool_value()),
            "hasInsecureSignature": lambda n : setattr(self, 'has_insecure_signature', n.get_bool_value()),
            "hasNoChainOfTrust": lambda n : setattr(self, 'has_no_chain_of_trust', n.get_bool_value()),
            "isDenylisted": lambda n : setattr(self, 'is_denylisted', n.get_bool_value()),
            "isHostnameMismatch": lambda n : setattr(self, 'is_hostname_mismatch', n.get_bool_value()),
            "isNotAfter": lambda n : setattr(self, 'is_not_after', n.get_bool_value()),
            "isNotBefore": lambda n : setattr(self, 'is_not_before', n.get_bool_value()),
            "isRevoked": lambda n : setattr(self, 'is_revoked', n.get_bool_value()),
            "isSelfSigned": lambda n : setattr(self, 'is_self_signed', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_bool_value("hasBadCommonName", self.has_bad_common_name)
        writer.write_bool_value("hasInsecureSignature", self.has_insecure_signature)
        writer.write_bool_value("hasNoChainOfTrust", self.has_no_chain_of_trust)
        writer.write_bool_value("isDenylisted", self.is_denylisted)
        writer.write_bool_value("isHostnameMismatch", self.is_hostname_mismatch)
        writer.write_bool_value("isNotAfter", self.is_not_after)
        writer.write_bool_value("isNotBefore", self.is_not_before)
        writer.write_bool_value("isRevoked", self.is_revoked)
        writer.write_bool_value("isSelfSigned", self.is_self_signed)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

