from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

authentication_method_target_type = lazy_import('msgraph.generated.models.authentication_method_target_type')

class AuthenticationMethodsRegistrationCampaignIncludeTarget(AdditionalDataHolder, Parsable):
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
        Instantiates a new authenticationMethodsRegistrationCampaignIncludeTarget and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The object identifier of an Azure Active Directory user or group.
        self._id: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The authentication method that the user is prompted to register. The value must be microsoftAuthenticator.
        self._targeted_authentication_method: Optional[str] = None
        # The targetType property
        self._target_type: Optional[authentication_method_target_type.AuthenticationMethodTargetType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AuthenticationMethodsRegistrationCampaignIncludeTarget:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AuthenticationMethodsRegistrationCampaignIncludeTarget
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AuthenticationMethodsRegistrationCampaignIncludeTarget()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "targeted_authentication_method": lambda n : setattr(self, 'targeted_authentication_method', n.get_str_value()),
            "target_type": lambda n : setattr(self, 'target_type', n.get_enum_value(authentication_method_target_type.AuthenticationMethodTargetType)),
        }
        return fields
    
    @property
    def id(self,) -> Optional[str]:
        """
        Gets the id property value. The object identifier of an Azure Active Directory user or group.
        Returns: Optional[str]
        """
        return self._id
    
    @id.setter
    def id(self,value: Optional[str] = None) -> None:
        """
        Sets the id property value. The object identifier of an Azure Active Directory user or group.
        Args:
            value: Value to set for the id property.
        """
        self._id = value
    
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
        writer.write_str_value("id", self.id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("targetedAuthenticationMethod", self.targeted_authentication_method)
        writer.write_enum_value("targetType", self.target_type)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def targeted_authentication_method(self,) -> Optional[str]:
        """
        Gets the targetedAuthenticationMethod property value. The authentication method that the user is prompted to register. The value must be microsoftAuthenticator.
        Returns: Optional[str]
        """
        return self._targeted_authentication_method
    
    @targeted_authentication_method.setter
    def targeted_authentication_method(self,value: Optional[str] = None) -> None:
        """
        Sets the targetedAuthenticationMethod property value. The authentication method that the user is prompted to register. The value must be microsoftAuthenticator.
        Args:
            value: Value to set for the targetedAuthenticationMethod property.
        """
        self._targeted_authentication_method = value
    
    @property
    def target_type(self,) -> Optional[authentication_method_target_type.AuthenticationMethodTargetType]:
        """
        Gets the targetType property value. The targetType property
        Returns: Optional[authentication_method_target_type.AuthenticationMethodTargetType]
        """
        return self._target_type
    
    @target_type.setter
    def target_type(self,value: Optional[authentication_method_target_type.AuthenticationMethodTargetType] = None) -> None:
        """
        Sets the targetType property value. The targetType property
        Args:
            value: Value to set for the targetType property.
        """
        self._target_type = value
    

