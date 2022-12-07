from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

x509_certificate_authentication_mode = lazy_import('msgraph.generated.models.x509_certificate_authentication_mode')
x509_certificate_rule = lazy_import('msgraph.generated.models.x509_certificate_rule')

class X509CertificateAuthenticationModeConfiguration(AdditionalDataHolder, Parsable):
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
        Instantiates a new x509CertificateAuthenticationModeConfiguration and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # Rules are configured in addition to the authentication mode to bind a specific x509CertificateRuleType to an x509CertificateAuthenticationMode. For example, bind the policyOID with identifier 1.32.132.343 to x509CertificateMultiFactor authentication mode.
        self._rules: Optional[List[x509_certificate_rule.X509CertificateRule]] = None
        # The type of strong authentication mode. The possible values are: x509CertificateSingleFactor, x509CertificateMultiFactor, unknownFutureValue.
        self._x509_certificate_authentication_default_mode: Optional[x509_certificate_authentication_mode.X509CertificateAuthenticationMode] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> X509CertificateAuthenticationModeConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: X509CertificateAuthenticationModeConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return X509CertificateAuthenticationModeConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "rules": lambda n : setattr(self, 'rules', n.get_collection_of_object_values(x509_certificate_rule.X509CertificateRule)),
            "x509_certificate_authentication_default_mode": lambda n : setattr(self, 'x509_certificate_authentication_default_mode', n.get_enum_value(x509_certificate_authentication_mode.X509CertificateAuthenticationMode)),
        }
        return fields
    
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
    
    @property
    def rules(self,) -> Optional[List[x509_certificate_rule.X509CertificateRule]]:
        """
        Gets the rules property value. Rules are configured in addition to the authentication mode to bind a specific x509CertificateRuleType to an x509CertificateAuthenticationMode. For example, bind the policyOID with identifier 1.32.132.343 to x509CertificateMultiFactor authentication mode.
        Returns: Optional[List[x509_certificate_rule.X509CertificateRule]]
        """
        return self._rules
    
    @rules.setter
    def rules(self,value: Optional[List[x509_certificate_rule.X509CertificateRule]] = None) -> None:
        """
        Sets the rules property value. Rules are configured in addition to the authentication mode to bind a specific x509CertificateRuleType to an x509CertificateAuthenticationMode. For example, bind the policyOID with identifier 1.32.132.343 to x509CertificateMultiFactor authentication mode.
        Args:
            value: Value to set for the rules property.
        """
        self._rules = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("rules", self.rules)
        writer.write_enum_value("x509CertificateAuthenticationDefaultMode", self.x509_certificate_authentication_default_mode)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def x509_certificate_authentication_default_mode(self,) -> Optional[x509_certificate_authentication_mode.X509CertificateAuthenticationMode]:
        """
        Gets the x509CertificateAuthenticationDefaultMode property value. The type of strong authentication mode. The possible values are: x509CertificateSingleFactor, x509CertificateMultiFactor, unknownFutureValue.
        Returns: Optional[x509_certificate_authentication_mode.X509CertificateAuthenticationMode]
        """
        return self._x509_certificate_authentication_default_mode
    
    @x509_certificate_authentication_default_mode.setter
    def x509_certificate_authentication_default_mode(self,value: Optional[x509_certificate_authentication_mode.X509CertificateAuthenticationMode] = None) -> None:
        """
        Sets the x509CertificateAuthenticationDefaultMode property value. The type of strong authentication mode. The possible values are: x509CertificateSingleFactor, x509CertificateMultiFactor, unknownFutureValue.
        Args:
            value: Value to set for the x509CertificateAuthenticationDefaultMode property.
        """
        self._x509_certificate_authentication_default_mode = value
    

