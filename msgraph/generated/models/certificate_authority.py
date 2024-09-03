from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class CertificateAuthority(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Required. The base64 encoded string representing the public certificate.
    certificate: Optional[bytes] = None
    # The URL of the certificate revocation list.
    certificate_revocation_list_url: Optional[str] = None
    # The URL contains the list of all revoked certificates since the last time a full certificate revocaton list was created.
    delta_certificate_revocation_list_url: Optional[str] = None
    # Required. true if the trusted certificate is a root authority, false if the trusted certificate is an intermediate authority.
    is_root_authority: Optional[bool] = None
    # The issuer of the certificate, calculated from the certificate value. Read-only.
    issuer: Optional[str] = None
    # The subject key identifier of the certificate, calculated from the certificate value. Read-only.
    issuer_ski: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CertificateAuthority:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CertificateAuthority
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CertificateAuthority()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "certificate": lambda n : setattr(self, 'certificate', n.get_bytes_value()),
            "certificateRevocationListUrl": lambda n : setattr(self, 'certificate_revocation_list_url', n.get_str_value()),
            "deltaCertificateRevocationListUrl": lambda n : setattr(self, 'delta_certificate_revocation_list_url', n.get_str_value()),
            "isRootAuthority": lambda n : setattr(self, 'is_root_authority', n.get_bool_value()),
            "issuer": lambda n : setattr(self, 'issuer', n.get_str_value()),
            "issuerSki": lambda n : setattr(self, 'issuer_ski', n.get_str_value()),
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
        writer.write_bytes_value("certificate", self.certificate)
        writer.write_str_value("certificateRevocationListUrl", self.certificate_revocation_list_url)
        writer.write_str_value("deltaCertificateRevocationListUrl", self.delta_certificate_revocation_list_url)
        writer.write_bool_value("isRootAuthority", self.is_root_authority)
        writer.write_str_value("issuer", self.issuer)
        writer.write_str_value("issuerSki", self.issuer_ski)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

