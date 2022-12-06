from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class CertificateAuthority(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def certificate(self,) -> Optional[bytes]:
        """
        Gets the certificate property value. Required. The base64 encoded string representing the public certificate.
        Returns: Optional[bytes]
        """
        return self._certificate
    
    @certificate.setter
    def certificate(self,value: Optional[bytes] = None) -> None:
        """
        Sets the certificate property value. Required. The base64 encoded string representing the public certificate.
        Args:
            value: Value to set for the certificate property.
        """
        self._certificate = value
    
    @property
    def certificate_revocation_list_url(self,) -> Optional[str]:
        """
        Gets the certificateRevocationListUrl property value. The URL of the certificate revocation list.
        Returns: Optional[str]
        """
        return self._certificate_revocation_list_url
    
    @certificate_revocation_list_url.setter
    def certificate_revocation_list_url(self,value: Optional[str] = None) -> None:
        """
        Sets the certificateRevocationListUrl property value. The URL of the certificate revocation list.
        Args:
            value: Value to set for the certificateRevocationListUrl property.
        """
        self._certificate_revocation_list_url = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new certificateAuthority and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Required. The base64 encoded string representing the public certificate.
        self._certificate: Optional[bytes] = None
        # The URL of the certificate revocation list.
        self._certificate_revocation_list_url: Optional[str] = None
        # The URL contains the list of all revoked certificates since the last time a full certificate revocaton list was created.
        self._delta_certificate_revocation_list_url: Optional[str] = None
        # Required. true if the trusted certificate is a root authority, false if the trusted certificate is an intermediate authority.
        self._is_root_authority: Optional[bool] = None
        # The issuer of the certificate, calculated from the certificate value. Read-only.
        self._issuer: Optional[str] = None
        # The subject key identifier of the certificate, calculated from the certificate value. Read-only.
        self._issuer_ski: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CertificateAuthority:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CertificateAuthority
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CertificateAuthority()
    
    @property
    def delta_certificate_revocation_list_url(self,) -> Optional[str]:
        """
        Gets the deltaCertificateRevocationListUrl property value. The URL contains the list of all revoked certificates since the last time a full certificate revocaton list was created.
        Returns: Optional[str]
        """
        return self._delta_certificate_revocation_list_url
    
    @delta_certificate_revocation_list_url.setter
    def delta_certificate_revocation_list_url(self,value: Optional[str] = None) -> None:
        """
        Sets the deltaCertificateRevocationListUrl property value. The URL contains the list of all revoked certificates since the last time a full certificate revocaton list was created.
        Args:
            value: Value to set for the deltaCertificateRevocationListUrl property.
        """
        self._delta_certificate_revocation_list_url = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "certificate": lambda n : setattr(self, 'certificate', n.get_bytes_value()),
            "certificate_revocation_list_url": lambda n : setattr(self, 'certificate_revocation_list_url', n.get_str_value()),
            "delta_certificate_revocation_list_url": lambda n : setattr(self, 'delta_certificate_revocation_list_url', n.get_str_value()),
            "is_root_authority": lambda n : setattr(self, 'is_root_authority', n.get_bool_value()),
            "issuer": lambda n : setattr(self, 'issuer', n.get_str_value()),
            "issuer_ski": lambda n : setattr(self, 'issuer_ski', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def is_root_authority(self,) -> Optional[bool]:
        """
        Gets the isRootAuthority property value. Required. true if the trusted certificate is a root authority, false if the trusted certificate is an intermediate authority.
        Returns: Optional[bool]
        """
        return self._is_root_authority
    
    @is_root_authority.setter
    def is_root_authority(self,value: Optional[bool] = None) -> None:
        """
        Sets the isRootAuthority property value. Required. true if the trusted certificate is a root authority, false if the trusted certificate is an intermediate authority.
        Args:
            value: Value to set for the isRootAuthority property.
        """
        self._is_root_authority = value
    
    @property
    def issuer(self,) -> Optional[str]:
        """
        Gets the issuer property value. The issuer of the certificate, calculated from the certificate value. Read-only.
        Returns: Optional[str]
        """
        return self._issuer
    
    @issuer.setter
    def issuer(self,value: Optional[str] = None) -> None:
        """
        Sets the issuer property value. The issuer of the certificate, calculated from the certificate value. Read-only.
        Args:
            value: Value to set for the issuer property.
        """
        self._issuer = value
    
    @property
    def issuer_ski(self,) -> Optional[str]:
        """
        Gets the issuerSki property value. The subject key identifier of the certificate, calculated from the certificate value. Read-only.
        Returns: Optional[str]
        """
        return self._issuer_ski
    
    @issuer_ski.setter
    def issuer_ski(self,value: Optional[str] = None) -> None:
        """
        Sets the issuerSki property value. The subject key identifier of the certificate, calculated from the certificate value. Read-only.
        Args:
            value: Value to set for the issuerSki property.
        """
        self._issuer_ski = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("certificate", self.certificate)
        writer.write_str_value("certificateRevocationListUrl", self.certificate_revocation_list_url)
        writer.write_str_value("deltaCertificateRevocationListUrl", self.delta_certificate_revocation_list_url)
        writer.write_bool_value("isRootAuthority", self.is_root_authority)
        writer.write_str_value("issuer", self.issuer)
        writer.write_str_value("issuerSki", self.issuer_ski)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

