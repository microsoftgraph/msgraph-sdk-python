from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .......models import synchronization_secret_key_string_value_pair

class ValidateCredentialsPostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new validateCredentialsPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The applicationIdentifier property
        self._application_identifier: Optional[str] = None
        # The credentials property
        self._credentials: Optional[List[synchronization_secret_key_string_value_pair.SynchronizationSecretKeyStringValuePair]] = None
        # The templateId property
        self._template_id: Optional[str] = None
        # The useSavedCredentials property
        self._use_saved_credentials: Optional[bool] = None
    
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
    def application_identifier(self,) -> Optional[str]:
        """
        Gets the applicationIdentifier property value. The applicationIdentifier property
        Returns: Optional[str]
        """
        return self._application_identifier
    
    @application_identifier.setter
    def application_identifier(self,value: Optional[str] = None) -> None:
        """
        Sets the applicationIdentifier property value. The applicationIdentifier property
        Args:
            value: Value to set for the application_identifier property.
        """
        self._application_identifier = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ValidateCredentialsPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ValidateCredentialsPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ValidateCredentialsPostRequestBody()
    
    @property
    def credentials(self,) -> Optional[List[synchronization_secret_key_string_value_pair.SynchronizationSecretKeyStringValuePair]]:
        """
        Gets the credentials property value. The credentials property
        Returns: Optional[List[synchronization_secret_key_string_value_pair.SynchronizationSecretKeyStringValuePair]]
        """
        return self._credentials
    
    @credentials.setter
    def credentials(self,value: Optional[List[synchronization_secret_key_string_value_pair.SynchronizationSecretKeyStringValuePair]] = None) -> None:
        """
        Sets the credentials property value. The credentials property
        Args:
            value: Value to set for the credentials property.
        """
        self._credentials = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .......models import synchronization_secret_key_string_value_pair

        fields: Dict[str, Callable[[Any], None]] = {
            "applicationIdentifier": lambda n : setattr(self, 'application_identifier', n.get_str_value()),
            "credentials": lambda n : setattr(self, 'credentials', n.get_collection_of_object_values(synchronization_secret_key_string_value_pair.SynchronizationSecretKeyStringValuePair)),
            "templateId": lambda n : setattr(self, 'template_id', n.get_str_value()),
            "useSavedCredentials": lambda n : setattr(self, 'use_saved_credentials', n.get_bool_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("applicationIdentifier", self.application_identifier)
        writer.write_collection_of_object_values("credentials", self.credentials)
        writer.write_str_value("templateId", self.template_id)
        writer.write_bool_value("useSavedCredentials", self.use_saved_credentials)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def template_id(self,) -> Optional[str]:
        """
        Gets the templateId property value. The templateId property
        Returns: Optional[str]
        """
        return self._template_id
    
    @template_id.setter
    def template_id(self,value: Optional[str] = None) -> None:
        """
        Sets the templateId property value. The templateId property
        Args:
            value: Value to set for the template_id property.
        """
        self._template_id = value
    
    @property
    def use_saved_credentials(self,) -> Optional[bool]:
        """
        Gets the useSavedCredentials property value. The useSavedCredentials property
        Returns: Optional[bool]
        """
        return self._use_saved_credentials
    
    @use_saved_credentials.setter
    def use_saved_credentials(self,value: Optional[bool] = None) -> None:
        """
        Sets the useSavedCredentials property value. The useSavedCredentials property
        Args:
            value: Value to set for the use_saved_credentials property.
        """
        self._use_saved_credentials = value
    

