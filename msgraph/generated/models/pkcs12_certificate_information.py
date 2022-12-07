from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class Pkcs12CertificateInformation(AdditionalDataHolder, Parsable):
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new pkcs12CertificateInformation and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Represents whether the certificate is the active certificate to be used for calling the API connector. The active certificate is the most recently uploaded certificate which is not yet expired but whose notBefore time is in the past.
        self._is_active: Optional[bool] = None
        # The certificate's expiry. This value is a NumericDate as defined in RFC 7519 (A JSON numeric value representing the number of seconds from 1970-01-01T00:00:00Z UTC until the specified UTC date/time, ignoring leap seconds.)
        self._not_after: Optional[int] = None
        # The certificate's issue time (not before). This value is a NumericDate as defined in RFC 7519 (A JSON numeric value representing the number of seconds from 1970-01-01T00:00:00Z UTC until the specified UTC date/time, ignoring leap seconds.)
        self._not_before: Optional[int] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The certificate thumbprint.
        self._thumbprint: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Pkcs12CertificateInformation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Pkcs12CertificateInformation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Pkcs12CertificateInformation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "is_active": lambda n : setattr(self, 'is_active', n.get_bool_value()),
            "not_after": lambda n : setattr(self, 'not_after', n.get_int_value()),
            "not_before": lambda n : setattr(self, 'not_before', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "thumbprint": lambda n : setattr(self, 'thumbprint', n.get_str_value()),
        }
        return fields
    
    @property
    def is_active(self,) -> Optional[bool]:
        """
        Gets the isActive property value. Represents whether the certificate is the active certificate to be used for calling the API connector. The active certificate is the most recently uploaded certificate which is not yet expired but whose notBefore time is in the past.
        Returns: Optional[bool]
        """
        return self._is_active
    
    @is_active.setter
    def is_active(self,value: Optional[bool] = None) -> None:
        """
        Sets the isActive property value. Represents whether the certificate is the active certificate to be used for calling the API connector. The active certificate is the most recently uploaded certificate which is not yet expired but whose notBefore time is in the past.
        Args:
            value: Value to set for the isActive property.
        """
        self._is_active = value
    
    @property
    def not_after(self,) -> Optional[int]:
        """
        Gets the notAfter property value. The certificate's expiry. This value is a NumericDate as defined in RFC 7519 (A JSON numeric value representing the number of seconds from 1970-01-01T00:00:00Z UTC until the specified UTC date/time, ignoring leap seconds.)
        Returns: Optional[int]
        """
        return self._not_after
    
    @not_after.setter
    def not_after(self,value: Optional[int] = None) -> None:
        """
        Sets the notAfter property value. The certificate's expiry. This value is a NumericDate as defined in RFC 7519 (A JSON numeric value representing the number of seconds from 1970-01-01T00:00:00Z UTC until the specified UTC date/time, ignoring leap seconds.)
        Args:
            value: Value to set for the notAfter property.
        """
        self._not_after = value
    
    @property
    def not_before(self,) -> Optional[int]:
        """
        Gets the notBefore property value. The certificate's issue time (not before). This value is a NumericDate as defined in RFC 7519 (A JSON numeric value representing the number of seconds from 1970-01-01T00:00:00Z UTC until the specified UTC date/time, ignoring leap seconds.)
        Returns: Optional[int]
        """
        return self._not_before
    
    @not_before.setter
    def not_before(self,value: Optional[int] = None) -> None:
        """
        Sets the notBefore property value. The certificate's issue time (not before). This value is a NumericDate as defined in RFC 7519 (A JSON numeric value representing the number of seconds from 1970-01-01T00:00:00Z UTC until the specified UTC date/time, ignoring leap seconds.)
        Args:
            value: Value to set for the notBefore property.
        """
        self._not_before = value
    
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
        writer.write_bool_value("isActive", self.is_active)
        writer.write_int_value("notAfter", self.not_after)
        writer.write_int_value("notBefore", self.not_before)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("thumbprint", self.thumbprint)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def thumbprint(self,) -> Optional[str]:
        """
        Gets the thumbprint property value. The certificate thumbprint.
        Returns: Optional[str]
        """
        return self._thumbprint
    
    @thumbprint.setter
    def thumbprint(self,value: Optional[str] = None) -> None:
        """
        Sets the thumbprint property value. The certificate thumbprint.
        Args:
            value: Value to set for the thumbprint property.
        """
        self._thumbprint = value
    

