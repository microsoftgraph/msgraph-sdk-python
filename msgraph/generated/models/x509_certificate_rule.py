from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

x509_certificate_authentication_mode = lazy_import('msgraph.generated.models.x509_certificate_authentication_mode')
x509_certificate_rule_type = lazy_import('msgraph.generated.models.x509_certificate_rule_type')

class X509CertificateRule(AdditionalDataHolder, Parsable):
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
        Instantiates a new x509CertificateRule and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The identifier of the X.509 certificate. Required.
        self._identifier: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The type of strong authentication mode. The possible values are: x509CertificateSingleFactor, x509CertificateMultiFactor, unknownFutureValue. Required.
        self._x509_certificate_authentication_mode: Optional[x509_certificate_authentication_mode.X509CertificateAuthenticationMode] = None
        # The type of the X.509 certificate mode configuration rule. The possible values are: issuerSubject, policyOID, unknownFutureValue. Required.
        self._x509_certificate_rule_type: Optional[x509_certificate_rule_type.X509CertificateRuleType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> X509CertificateRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: X509CertificateRule
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return X509CertificateRule()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "identifier": lambda n : setattr(self, 'identifier', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "x509_certificate_authentication_mode": lambda n : setattr(self, 'x509_certificate_authentication_mode', n.get_enum_value(x509_certificate_authentication_mode.X509CertificateAuthenticationMode)),
            "x509_certificate_rule_type": lambda n : setattr(self, 'x509_certificate_rule_type', n.get_enum_value(x509_certificate_rule_type.X509CertificateRuleType)),
        }
        return fields
    
    @property
    def identifier(self,) -> Optional[str]:
        """
        Gets the identifier property value. The identifier of the X.509 certificate. Required.
        Returns: Optional[str]
        """
        return self._identifier
    
    @identifier.setter
    def identifier(self,value: Optional[str] = None) -> None:
        """
        Sets the identifier property value. The identifier of the X.509 certificate. Required.
        Args:
            value: Value to set for the identifier property.
        """
        self._identifier = value
    
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
        writer.write_str_value("identifier", self.identifier)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("x509CertificateAuthenticationMode", self.x509_certificate_authentication_mode)
        writer.write_enum_value("x509CertificateRuleType", self.x509_certificate_rule_type)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def x509_certificate_authentication_mode(self,) -> Optional[x509_certificate_authentication_mode.X509CertificateAuthenticationMode]:
        """
        Gets the x509CertificateAuthenticationMode property value. The type of strong authentication mode. The possible values are: x509CertificateSingleFactor, x509CertificateMultiFactor, unknownFutureValue. Required.
        Returns: Optional[x509_certificate_authentication_mode.X509CertificateAuthenticationMode]
        """
        return self._x509_certificate_authentication_mode
    
    @x509_certificate_authentication_mode.setter
    def x509_certificate_authentication_mode(self,value: Optional[x509_certificate_authentication_mode.X509CertificateAuthenticationMode] = None) -> None:
        """
        Sets the x509CertificateAuthenticationMode property value. The type of strong authentication mode. The possible values are: x509CertificateSingleFactor, x509CertificateMultiFactor, unknownFutureValue. Required.
        Args:
            value: Value to set for the x509CertificateAuthenticationMode property.
        """
        self._x509_certificate_authentication_mode = value
    
    @property
    def x509_certificate_rule_type(self,) -> Optional[x509_certificate_rule_type.X509CertificateRuleType]:
        """
        Gets the x509CertificateRuleType property value. The type of the X.509 certificate mode configuration rule. The possible values are: issuerSubject, policyOID, unknownFutureValue. Required.
        Returns: Optional[x509_certificate_rule_type.X509CertificateRuleType]
        """
        return self._x509_certificate_rule_type
    
    @x509_certificate_rule_type.setter
    def x509_certificate_rule_type(self,value: Optional[x509_certificate_rule_type.X509CertificateRuleType] = None) -> None:
        """
        Sets the x509CertificateRuleType property value. The type of the X.509 certificate mode configuration rule. The possible values are: issuerSubject, policyOID, unknownFutureValue. Required.
        Args:
            value: Value to set for the x509CertificateRuleType property.
        """
        self._x509_certificate_rule_type = value
    

