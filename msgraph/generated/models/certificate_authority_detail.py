from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .certificate_authority_type import CertificateAuthorityType
    from .directory_object import DirectoryObject

from .directory_object import DirectoryObject

@dataclass
class CertificateAuthorityDetail(DirectoryObject, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.certificateAuthorityDetail"
    # The public key of the certificate authority.
    certificate: Optional[bytes] = None
    # The type of certificate authority. The possible values are: root, intermediate, unknownFutureValue. Supports $filter (eq).
    certificate_authority_type: Optional[CertificateAuthorityType] = None
    # The URL to check if the certificate is revoked.
    certificate_revocation_list_url: Optional[str] = None
    # The date and time when the certificate authority was created.
    created_date_time: Optional[datetime.datetime] = None
    # The deltaCertificateRevocationListUrl property
    delta_certificate_revocation_list_url: Optional[str] = None
    # The display name of the certificate authority.
    display_name: Optional[str] = None
    # The date and time when the certificate authority expires. Supports $filter (eq) and $orderby.
    expiration_date_time: Optional[datetime.datetime] = None
    # Indicates whether the certificate picker presents the certificate authority to the user to use for authentication. Default value is false. Optional.
    is_issuer_hint_enabled: Optional[bool] = None
    # The issuer of the certificate authority.
    issuer: Optional[str] = None
    # The subject key identifier of certificate authority.
    issuer_subject_key_identifier: Optional[str] = None
    # The thumbprint of certificate authority certificate. Supports $filter (eq, startswith).
    thumbprint: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CertificateAuthorityDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CertificateAuthorityDetail
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CertificateAuthorityDetail()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .certificate_authority_type import CertificateAuthorityType
        from .directory_object import DirectoryObject

        from .certificate_authority_type import CertificateAuthorityType
        from .directory_object import DirectoryObject

        fields: dict[str, Callable[[Any], None]] = {
            "certificate": lambda n : setattr(self, 'certificate', n.get_bytes_value()),
            "certificateAuthorityType": lambda n : setattr(self, 'certificate_authority_type', n.get_enum_value(CertificateAuthorityType)),
            "certificateRevocationListUrl": lambda n : setattr(self, 'certificate_revocation_list_url', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "deltaCertificateRevocationListUrl": lambda n : setattr(self, 'delta_certificate_revocation_list_url', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "expirationDateTime": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "isIssuerHintEnabled": lambda n : setattr(self, 'is_issuer_hint_enabled', n.get_bool_value()),
            "issuer": lambda n : setattr(self, 'issuer', n.get_str_value()),
            "issuerSubjectKeyIdentifier": lambda n : setattr(self, 'issuer_subject_key_identifier', n.get_str_value()),
            "thumbprint": lambda n : setattr(self, 'thumbprint', n.get_str_value()),
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
        writer.write_bytes_value("certificate", self.certificate)
        writer.write_enum_value("certificateAuthorityType", self.certificate_authority_type)
        writer.write_str_value("certificateRevocationListUrl", self.certificate_revocation_list_url)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("deltaCertificateRevocationListUrl", self.delta_certificate_revocation_list_url)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("expirationDateTime", self.expiration_date_time)
        writer.write_bool_value("isIssuerHintEnabled", self.is_issuer_hint_enabled)
        writer.write_str_value("issuer", self.issuer)
        writer.write_str_value("issuerSubjectKeyIdentifier", self.issuer_subject_key_identifier)
        writer.write_str_value("thumbprint", self.thumbprint)
    

