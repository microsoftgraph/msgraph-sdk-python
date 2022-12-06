from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

optional_claim = lazy_import('msgraph.generated.models.optional_claim')

class OptionalClaims(AdditionalDataHolder, Parsable):
    @property
    def access_token(self,) -> Optional[List[optional_claim.OptionalClaim]]:
        """
        Gets the accessToken property value. The optional claims returned in the JWT access token.
        Returns: Optional[List[optional_claim.OptionalClaim]]
        """
        return self._access_token
    
    @access_token.setter
    def access_token(self,value: Optional[List[optional_claim.OptionalClaim]] = None) -> None:
        """
        Sets the accessToken property value. The optional claims returned in the JWT access token.
        Args:
            value: Value to set for the accessToken property.
        """
        self._access_token = value
    
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
        Instantiates a new optionalClaims and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The optional claims returned in the JWT access token.
        self._access_token: Optional[List[optional_claim.OptionalClaim]] = None
        # The optional claims returned in the JWT ID token.
        self._id_token: Optional[List[optional_claim.OptionalClaim]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The optional claims returned in the SAML token.
        self._saml2_token: Optional[List[optional_claim.OptionalClaim]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OptionalClaims:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OptionalClaims
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return OptionalClaims()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "access_token": lambda n : setattr(self, 'access_token', n.get_collection_of_object_values(optional_claim.OptionalClaim)),
            "id_token": lambda n : setattr(self, 'id_token', n.get_collection_of_object_values(optional_claim.OptionalClaim)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "saml2_token": lambda n : setattr(self, 'saml2_token', n.get_collection_of_object_values(optional_claim.OptionalClaim)),
        }
        return fields
    
    @property
    def id_token(self,) -> Optional[List[optional_claim.OptionalClaim]]:
        """
        Gets the idToken property value. The optional claims returned in the JWT ID token.
        Returns: Optional[List[optional_claim.OptionalClaim]]
        """
        return self._id_token
    
    @id_token.setter
    def id_token(self,value: Optional[List[optional_claim.OptionalClaim]] = None) -> None:
        """
        Sets the idToken property value. The optional claims returned in the JWT ID token.
        Args:
            value: Value to set for the idToken property.
        """
        self._id_token = value
    
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
    def saml2_token(self,) -> Optional[List[optional_claim.OptionalClaim]]:
        """
        Gets the saml2Token property value. The optional claims returned in the SAML token.
        Returns: Optional[List[optional_claim.OptionalClaim]]
        """
        return self._saml2_token
    
    @saml2_token.setter
    def saml2_token(self,value: Optional[List[optional_claim.OptionalClaim]] = None) -> None:
        """
        Sets the saml2Token property value. The optional claims returned in the SAML token.
        Args:
            value: Value to set for the saml2Token property.
        """
        self._saml2_token = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_object_values("accessToken", self.access_token)
        writer.write_collection_of_object_values("idToken", self.id_token)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("saml2Token", self.saml2_token)
        writer.write_additional_data_value(self.additional_data)
    

