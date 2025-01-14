from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .x509_certificate_affinity_level import X509CertificateAffinityLevel
    from .x509_certificate_authentication_mode import X509CertificateAuthenticationMode
    from .x509_certificate_rule import X509CertificateRule

@dataclass
class X509CertificateAuthenticationModeConfiguration(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The OdataType property
    odata_type: Optional[str] = None
    # Rules are configured in addition to the authentication mode to bind a specific x509CertificateRuleType to an x509CertificateAuthenticationMode. For example, bind the policyOID with identifier 1.32.132.343 to x509CertificateMultiFactor authentication mode.
    rules: Optional[list[X509CertificateRule]] = None
    # The type of strong authentication mode. The possible values are: x509CertificateSingleFactor, x509CertificateMultiFactor, unknownFutureValue.
    x509_certificate_authentication_default_mode: Optional[X509CertificateAuthenticationMode] = None
    # The x509CertificateDefaultRequiredAffinityLevel property
    x509_certificate_default_required_affinity_level: Optional[X509CertificateAffinityLevel] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> X509CertificateAuthenticationModeConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: X509CertificateAuthenticationModeConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return X509CertificateAuthenticationModeConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .x509_certificate_affinity_level import X509CertificateAffinityLevel
        from .x509_certificate_authentication_mode import X509CertificateAuthenticationMode
        from .x509_certificate_rule import X509CertificateRule

        from .x509_certificate_affinity_level import X509CertificateAffinityLevel
        from .x509_certificate_authentication_mode import X509CertificateAuthenticationMode
        from .x509_certificate_rule import X509CertificateRule

        fields: dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "rules": lambda n : setattr(self, 'rules', n.get_collection_of_object_values(X509CertificateRule)),
            "x509CertificateAuthenticationDefaultMode": lambda n : setattr(self, 'x509_certificate_authentication_default_mode', n.get_enum_value(X509CertificateAuthenticationMode)),
            "x509CertificateDefaultRequiredAffinityLevel": lambda n : setattr(self, 'x509_certificate_default_required_affinity_level', n.get_enum_value(X509CertificateAffinityLevel)),
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("rules", self.rules)
        writer.write_enum_value("x509CertificateAuthenticationDefaultMode", self.x509_certificate_authentication_default_mode)
        writer.write_enum_value("x509CertificateDefaultRequiredAffinityLevel", self.x509_certificate_default_required_affinity_level)
        writer.write_additional_data_value(self.additional_data)
    

