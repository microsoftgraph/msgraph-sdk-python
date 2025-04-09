from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .x509_certificate_c_r_l_validation_configuration_state import X509CertificateCRLValidationConfigurationState

@dataclass
class X509CertificateCRLValidationConfiguration(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Represents the SKIs of CAs that should be excluded from the valid CRL distribution point check. SKI is represented as a hexadecimal string.
    exempted_certificate_authorities_subject_key_identifiers: Optional[list[str]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The state property
    state: Optional[X509CertificateCRLValidationConfigurationState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> X509CertificateCRLValidationConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: X509CertificateCRLValidationConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return X509CertificateCRLValidationConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .x509_certificate_c_r_l_validation_configuration_state import X509CertificateCRLValidationConfigurationState

        from .x509_certificate_c_r_l_validation_configuration_state import X509CertificateCRLValidationConfigurationState

        fields: dict[str, Callable[[Any], None]] = {
            "exemptedCertificateAuthoritiesSubjectKeyIdentifiers": lambda n : setattr(self, 'exempted_certificate_authorities_subject_key_identifiers', n.get_collection_of_primitive_values(str)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(X509CertificateCRLValidationConfigurationState)),
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
        writer.write_collection_of_primitive_values("exemptedCertificateAuthoritiesSubjectKeyIdentifiers", self.exempted_certificate_authorities_subject_key_identifiers)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("state", self.state)
        writer.write_additional_data_value(self.additional_data)
    

