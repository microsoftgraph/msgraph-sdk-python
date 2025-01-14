from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .x509_certificate_affinity_level import X509CertificateAffinityLevel
    from .x509_certificate_authentication_mode import X509CertificateAuthenticationMode
    from .x509_certificate_rule_type import X509CertificateRuleType

@dataclass
class X509CertificateRule(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The identifier of the X.509 certificate. Required.
    identifier: Optional[str] = None
    # The issuerSubjectIdentifier property
    issuer_subject_identifier: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The policyOidIdentifier property
    policy_oid_identifier: Optional[str] = None
    # The type of strong authentication mode. The possible values are: x509CertificateSingleFactor, x509CertificateMultiFactor, unknownFutureValue. Required.
    x509_certificate_authentication_mode: Optional[X509CertificateAuthenticationMode] = None
    # The x509CertificateRequiredAffinityLevel property
    x509_certificate_required_affinity_level: Optional[X509CertificateAffinityLevel] = None
    # The type of the X.509 certificate mode configuration rule. The possible values are: issuerSubject, policyOID, unknownFutureValue. Required.
    x509_certificate_rule_type: Optional[X509CertificateRuleType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> X509CertificateRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: X509CertificateRule
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return X509CertificateRule()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .x509_certificate_affinity_level import X509CertificateAffinityLevel
        from .x509_certificate_authentication_mode import X509CertificateAuthenticationMode
        from .x509_certificate_rule_type import X509CertificateRuleType

        from .x509_certificate_affinity_level import X509CertificateAffinityLevel
        from .x509_certificate_authentication_mode import X509CertificateAuthenticationMode
        from .x509_certificate_rule_type import X509CertificateRuleType

        fields: dict[str, Callable[[Any], None]] = {
            "identifier": lambda n : setattr(self, 'identifier', n.get_str_value()),
            "issuerSubjectIdentifier": lambda n : setattr(self, 'issuer_subject_identifier', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "policyOidIdentifier": lambda n : setattr(self, 'policy_oid_identifier', n.get_str_value()),
            "x509CertificateAuthenticationMode": lambda n : setattr(self, 'x509_certificate_authentication_mode', n.get_enum_value(X509CertificateAuthenticationMode)),
            "x509CertificateRequiredAffinityLevel": lambda n : setattr(self, 'x509_certificate_required_affinity_level', n.get_enum_value(X509CertificateAffinityLevel)),
            "x509CertificateRuleType": lambda n : setattr(self, 'x509_certificate_rule_type', n.get_enum_value(X509CertificateRuleType)),
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
        writer.write_str_value("identifier", self.identifier)
        writer.write_str_value("issuerSubjectIdentifier", self.issuer_subject_identifier)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("policyOidIdentifier", self.policy_oid_identifier)
        writer.write_enum_value("x509CertificateAuthenticationMode", self.x509_certificate_authentication_mode)
        writer.write_enum_value("x509CertificateRequiredAffinityLevel", self.x509_certificate_required_affinity_level)
        writer.write_enum_value("x509CertificateRuleType", self.x509_certificate_rule_type)
        writer.write_additional_data_value(self.additional_data)
    

