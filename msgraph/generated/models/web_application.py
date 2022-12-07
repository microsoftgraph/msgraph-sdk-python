from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

implicit_grant_settings = lazy_import('msgraph.generated.models.implicit_grant_settings')
redirect_uri_settings = lazy_import('msgraph.generated.models.redirect_uri_settings')

class WebApplication(AdditionalDataHolder, Parsable):
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
        Instantiates a new webApplication and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Home page or landing page of the application.
        self._home_page_url: Optional[str] = None
        # Specifies whether this web application can request tokens using the OAuth 2.0 implicit flow.
        self._implicit_grant_settings: Optional[implicit_grant_settings.ImplicitGrantSettings] = None
        # Specifies the URL that will be used by Microsoft's authorization service to logout an user using front-channel, back-channel or SAML logout protocols.
        self._logout_url: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Specifies the URLs where user tokens are sent for sign-in, or the redirect URIs where OAuth 2.0 authorization codes and access tokens are sent.
        self._redirect_uris: Optional[List[str]] = None
        # The redirectUriSettings property
        self._redirect_uri_settings: Optional[List[redirect_uri_settings.RedirectUriSettings]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WebApplication:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WebApplication
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WebApplication()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "home_page_url": lambda n : setattr(self, 'home_page_url', n.get_str_value()),
            "implicit_grant_settings": lambda n : setattr(self, 'implicit_grant_settings', n.get_object_value(implicit_grant_settings.ImplicitGrantSettings)),
            "logout_url": lambda n : setattr(self, 'logout_url', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "redirect_uris": lambda n : setattr(self, 'redirect_uris', n.get_collection_of_primitive_values(str)),
            "redirect_uri_settings": lambda n : setattr(self, 'redirect_uri_settings', n.get_collection_of_object_values(redirect_uri_settings.RedirectUriSettings)),
        }
        return fields
    
    @property
    def home_page_url(self,) -> Optional[str]:
        """
        Gets the homePageUrl property value. Home page or landing page of the application.
        Returns: Optional[str]
        """
        return self._home_page_url
    
    @home_page_url.setter
    def home_page_url(self,value: Optional[str] = None) -> None:
        """
        Sets the homePageUrl property value. Home page or landing page of the application.
        Args:
            value: Value to set for the homePageUrl property.
        """
        self._home_page_url = value
    
    @property
    def implicit_grant_settings(self,) -> Optional[implicit_grant_settings.ImplicitGrantSettings]:
        """
        Gets the implicitGrantSettings property value. Specifies whether this web application can request tokens using the OAuth 2.0 implicit flow.
        Returns: Optional[implicit_grant_settings.ImplicitGrantSettings]
        """
        return self._implicit_grant_settings
    
    @implicit_grant_settings.setter
    def implicit_grant_settings(self,value: Optional[implicit_grant_settings.ImplicitGrantSettings] = None) -> None:
        """
        Sets the implicitGrantSettings property value. Specifies whether this web application can request tokens using the OAuth 2.0 implicit flow.
        Args:
            value: Value to set for the implicitGrantSettings property.
        """
        self._implicit_grant_settings = value
    
    @property
    def logout_url(self,) -> Optional[str]:
        """
        Gets the logoutUrl property value. Specifies the URL that will be used by Microsoft's authorization service to logout an user using front-channel, back-channel or SAML logout protocols.
        Returns: Optional[str]
        """
        return self._logout_url
    
    @logout_url.setter
    def logout_url(self,value: Optional[str] = None) -> None:
        """
        Sets the logoutUrl property value. Specifies the URL that will be used by Microsoft's authorization service to logout an user using front-channel, back-channel or SAML logout protocols.
        Args:
            value: Value to set for the logoutUrl property.
        """
        self._logout_url = value
    
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
    def redirect_uris(self,) -> Optional[List[str]]:
        """
        Gets the redirectUris property value. Specifies the URLs where user tokens are sent for sign-in, or the redirect URIs where OAuth 2.0 authorization codes and access tokens are sent.
        Returns: Optional[List[str]]
        """
        return self._redirect_uris
    
    @redirect_uris.setter
    def redirect_uris(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the redirectUris property value. Specifies the URLs where user tokens are sent for sign-in, or the redirect URIs where OAuth 2.0 authorization codes and access tokens are sent.
        Args:
            value: Value to set for the redirectUris property.
        """
        self._redirect_uris = value
    
    @property
    def redirect_uri_settings(self,) -> Optional[List[redirect_uri_settings.RedirectUriSettings]]:
        """
        Gets the redirectUriSettings property value. The redirectUriSettings property
        Returns: Optional[List[redirect_uri_settings.RedirectUriSettings]]
        """
        return self._redirect_uri_settings
    
    @redirect_uri_settings.setter
    def redirect_uri_settings(self,value: Optional[List[redirect_uri_settings.RedirectUriSettings]] = None) -> None:
        """
        Sets the redirectUriSettings property value. The redirectUriSettings property
        Args:
            value: Value to set for the redirectUriSettings property.
        """
        self._redirect_uri_settings = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("homePageUrl", self.home_page_url)
        writer.write_object_value("implicitGrantSettings", self.implicit_grant_settings)
        writer.write_str_value("logoutUrl", self.logout_url)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_primitive_values("redirectUris", self.redirect_uris)
        writer.write_collection_of_object_values("redirectUriSettings", self.redirect_uri_settings)
        writer.write_additional_data_value(self.additional_data)
    

