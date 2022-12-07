from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class ImplicitGrantSettings(AdditionalDataHolder, Parsable):
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
        Instantiates a new implicitGrantSettings and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Specifies whether this web application can request an access token using the OAuth 2.0 implicit flow.
        self._enable_access_token_issuance: Optional[bool] = None
        # Specifies whether this web application can request an ID token using the OAuth 2.0 implicit flow.
        self._enable_id_token_issuance: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ImplicitGrantSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ImplicitGrantSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ImplicitGrantSettings()
    
    @property
    def enable_access_token_issuance(self,) -> Optional[bool]:
        """
        Gets the enableAccessTokenIssuance property value. Specifies whether this web application can request an access token using the OAuth 2.0 implicit flow.
        Returns: Optional[bool]
        """
        return self._enable_access_token_issuance
    
    @enable_access_token_issuance.setter
    def enable_access_token_issuance(self,value: Optional[bool] = None) -> None:
        """
        Sets the enableAccessTokenIssuance property value. Specifies whether this web application can request an access token using the OAuth 2.0 implicit flow.
        Args:
            value: Value to set for the enableAccessTokenIssuance property.
        """
        self._enable_access_token_issuance = value
    
    @property
    def enable_id_token_issuance(self,) -> Optional[bool]:
        """
        Gets the enableIdTokenIssuance property value. Specifies whether this web application can request an ID token using the OAuth 2.0 implicit flow.
        Returns: Optional[bool]
        """
        return self._enable_id_token_issuance
    
    @enable_id_token_issuance.setter
    def enable_id_token_issuance(self,value: Optional[bool] = None) -> None:
        """
        Sets the enableIdTokenIssuance property value. Specifies whether this web application can request an ID token using the OAuth 2.0 implicit flow.
        Args:
            value: Value to set for the enableIdTokenIssuance property.
        """
        self._enable_id_token_issuance = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "enable_access_token_issuance": lambda n : setattr(self, 'enable_access_token_issuance', n.get_bool_value()),
            "enable_id_token_issuance": lambda n : setattr(self, 'enable_id_token_issuance', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_bool_value("enableAccessTokenIssuance", self.enable_access_token_issuance)
        writer.write_bool_value("enableIdTokenIssuance", self.enable_id_token_issuance)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

