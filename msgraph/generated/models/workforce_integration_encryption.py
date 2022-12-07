from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

workforce_integration_encryption_protocol = lazy_import('msgraph.generated.models.workforce_integration_encryption_protocol')

class WorkforceIntegrationEncryption(AdditionalDataHolder, Parsable):
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
        Instantiates a new workforceIntegrationEncryption and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # Possible values are: sharedSecret, unknownFutureValue.
        self._protocol: Optional[workforce_integration_encryption_protocol.WorkforceIntegrationEncryptionProtocol] = None
        # Encryption shared secret.
        self._secret: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WorkforceIntegrationEncryption:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WorkforceIntegrationEncryption
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WorkforceIntegrationEncryption()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "protocol": lambda n : setattr(self, 'protocol', n.get_enum_value(workforce_integration_encryption_protocol.WorkforceIntegrationEncryptionProtocol)),
            "secret": lambda n : setattr(self, 'secret', n.get_str_value()),
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
    def protocol(self,) -> Optional[workforce_integration_encryption_protocol.WorkforceIntegrationEncryptionProtocol]:
        """
        Gets the protocol property value. Possible values are: sharedSecret, unknownFutureValue.
        Returns: Optional[workforce_integration_encryption_protocol.WorkforceIntegrationEncryptionProtocol]
        """
        return self._protocol
    
    @protocol.setter
    def protocol(self,value: Optional[workforce_integration_encryption_protocol.WorkforceIntegrationEncryptionProtocol] = None) -> None:
        """
        Sets the protocol property value. Possible values are: sharedSecret, unknownFutureValue.
        Args:
            value: Value to set for the protocol property.
        """
        self._protocol = value
    
    @property
    def secret(self,) -> Optional[str]:
        """
        Gets the secret property value. Encryption shared secret.
        Returns: Optional[str]
        """
        return self._secret
    
    @secret.setter
    def secret(self,value: Optional[str] = None) -> None:
        """
        Sets the secret property value. Encryption shared secret.
        Args:
            value: Value to set for the secret property.
        """
        self._secret = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("protocol", self.protocol)
        writer.write_str_value("secret", self.secret)
        writer.write_additional_data_value(self.additional_data)
    

