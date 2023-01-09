from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class FederatedIdentityCredential(entity.Entity):
    """
    Provides operations to manage the collection of application entities.
    """
    @property
    def audiences(self,) -> Optional[List[str]]:
        """
        Gets the audiences property value. The audience that can appear in the external token. This field is mandatory and should be set to api://AzureADTokenExchange for Azure AD. It says what Microsoft identity platform should accept in the aud claim in the incoming token. This value represents Azure AD in your external identity provider and has no fixed value across identity providers - you may need to create a new application registration in your identity provider to serve as the audience of this token. This field can only accept a single value and has a limit of 600 characters. Required.
        Returns: Optional[List[str]]
        """
        return self._audiences
    
    @audiences.setter
    def audiences(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the audiences property value. The audience that can appear in the external token. This field is mandatory and should be set to api://AzureADTokenExchange for Azure AD. It says what Microsoft identity platform should accept in the aud claim in the incoming token. This value represents Azure AD in your external identity provider and has no fixed value across identity providers - you may need to create a new application registration in your identity provider to serve as the audience of this token. This field can only accept a single value and has a limit of 600 characters. Required.
        Args:
            value: Value to set for the audiences property.
        """
        self._audiences = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new federatedIdentityCredential and sets the default values.
        """
        super().__init__()
        # The audience that can appear in the external token. This field is mandatory and should be set to api://AzureADTokenExchange for Azure AD. It says what Microsoft identity platform should accept in the aud claim in the incoming token. This value represents Azure AD in your external identity provider and has no fixed value across identity providers - you may need to create a new application registration in your identity provider to serve as the audience of this token. This field can only accept a single value and has a limit of 600 characters. Required.
        self._audiences: Optional[List[str]] = None
        # The un-validated, user-provided description of the federated identity credential. It has a limit of 600 characters. Optional.
        self._description: Optional[str] = None
        # The URL of the external identity provider and must match the issuer claim of the external token being exchanged. The combination of the values of issuer and subject must be unique on the app. It has a limit of 600 characters. Required.
        self._issuer: Optional[str] = None
        # is the unique identifier for the federated identity credential, which has a limit of 120 characters and must be URL friendly. It is immutable once created. Required. Not nullable. Supports $filter (eq).
        self._name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Required. The identifier of the external software workload within the external identity provider. Like the audience value, it has no fixed format, as each identity provider uses their own - sometimes a GUID, sometimes a colon delimited identifier, sometimes arbitrary strings. The value here must match the sub claim within the token presented to Azure AD. The combination of issuer and subject must be unique on the app. It has a limit of 600 characters. Supports $filter (eq).
        self._subject: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> FederatedIdentityCredential:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: FederatedIdentityCredential
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return FederatedIdentityCredential()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The un-validated, user-provided description of the federated identity credential. It has a limit of 600 characters. Optional.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The un-validated, user-provided description of the federated identity credential. It has a limit of 600 characters. Optional.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "audiences": lambda n : setattr(self, 'audiences', n.get_collection_of_primitive_values(str)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "issuer": lambda n : setattr(self, 'issuer', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "subject": lambda n : setattr(self, 'subject', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def issuer(self,) -> Optional[str]:
        """
        Gets the issuer property value. The URL of the external identity provider and must match the issuer claim of the external token being exchanged. The combination of the values of issuer and subject must be unique on the app. It has a limit of 600 characters. Required.
        Returns: Optional[str]
        """
        return self._issuer
    
    @issuer.setter
    def issuer(self,value: Optional[str] = None) -> None:
        """
        Sets the issuer property value. The URL of the external identity provider and must match the issuer claim of the external token being exchanged. The combination of the values of issuer and subject must be unique on the app. It has a limit of 600 characters. Required.
        Args:
            value: Value to set for the issuer property.
        """
        self._issuer = value
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. is the unique identifier for the federated identity credential, which has a limit of 120 characters and must be URL friendly. It is immutable once created. Required. Not nullable. Supports $filter (eq).
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. is the unique identifier for the federated identity credential, which has a limit of 120 characters and must be URL friendly. It is immutable once created. Required. Not nullable. Supports $filter (eq).
        Args:
            value: Value to set for the name property.
        """
        self._name = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_primitive_values("audiences", self.audiences)
        writer.write_str_value("description", self.description)
        writer.write_str_value("issuer", self.issuer)
        writer.write_str_value("name", self.name)
        writer.write_str_value("subject", self.subject)
    
    @property
    def subject(self,) -> Optional[str]:
        """
        Gets the subject property value. Required. The identifier of the external software workload within the external identity provider. Like the audience value, it has no fixed format, as each identity provider uses their own - sometimes a GUID, sometimes a colon delimited identifier, sometimes arbitrary strings. The value here must match the sub claim within the token presented to Azure AD. The combination of issuer and subject must be unique on the app. It has a limit of 600 characters. Supports $filter (eq).
        Returns: Optional[str]
        """
        return self._subject
    
    @subject.setter
    def subject(self,value: Optional[str] = None) -> None:
        """
        Sets the subject property value. Required. The identifier of the external software workload within the external identity provider. Like the audience value, it has no fixed format, as each identity provider uses their own - sometimes a GUID, sometimes a colon delimited identifier, sometimes arbitrary strings. The value here must match the sub claim within the token presented to Azure AD. The combination of issuer and subject must be unique on the app. It has a limit of 600 characters. Supports $filter (eq).
        Args:
            value: Value to set for the subject property.
        """
        self._subject = value
    

