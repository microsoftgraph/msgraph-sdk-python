from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import key_credential_configuration, password_credential_configuration

class AppManagementConfiguration(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new appManagementConfiguration and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Collection of keyCredential restrictions settings to be applied to an application or service principal.
        self._key_credentials: Optional[List[key_credential_configuration.KeyCredentialConfiguration]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Collection of password restrictions settings to be applied to an application or service principal.
        self._password_credentials: Optional[List[password_credential_configuration.PasswordCredentialConfiguration]] = None
    
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
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AppManagementConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AppManagementConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AppManagementConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import key_credential_configuration, password_credential_configuration

        fields: Dict[str, Callable[[Any], None]] = {
            "keyCredentials": lambda n : setattr(self, 'key_credentials', n.get_collection_of_object_values(key_credential_configuration.KeyCredentialConfiguration)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "passwordCredentials": lambda n : setattr(self, 'password_credentials', n.get_collection_of_object_values(password_credential_configuration.PasswordCredentialConfiguration)),
        }
        return fields
    
    @property
    def key_credentials(self,) -> Optional[List[key_credential_configuration.KeyCredentialConfiguration]]:
        """
        Gets the keyCredentials property value. Collection of keyCredential restrictions settings to be applied to an application or service principal.
        Returns: Optional[List[key_credential_configuration.KeyCredentialConfiguration]]
        """
        return self._key_credentials
    
    @key_credentials.setter
    def key_credentials(self,value: Optional[List[key_credential_configuration.KeyCredentialConfiguration]] = None) -> None:
        """
        Sets the keyCredentials property value. Collection of keyCredential restrictions settings to be applied to an application or service principal.
        Args:
            value: Value to set for the key_credentials property.
        """
        self._key_credentials = value
    
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
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    @property
    def password_credentials(self,) -> Optional[List[password_credential_configuration.PasswordCredentialConfiguration]]:
        """
        Gets the passwordCredentials property value. Collection of password restrictions settings to be applied to an application or service principal.
        Returns: Optional[List[password_credential_configuration.PasswordCredentialConfiguration]]
        """
        return self._password_credentials
    
    @password_credentials.setter
    def password_credentials(self,value: Optional[List[password_credential_configuration.PasswordCredentialConfiguration]] = None) -> None:
        """
        Sets the passwordCredentials property value. Collection of password restrictions settings to be applied to an application or service principal.
        Args:
            value: Value to set for the password_credentials property.
        """
        self._password_credentials = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_object_values("keyCredentials", self.key_credentials)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("passwordCredentials", self.password_credentials)
        writer.write_additional_data_value(self.additional_data)
    

