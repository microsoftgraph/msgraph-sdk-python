from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import implicit_grant_settings, redirect_uri_settings

@dataclass
class WebApplication(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Home page or landing page of the application.
    home_page_url: Optional[str] = None
    # Specifies whether this web application can request tokens using the OAuth 2.0 implicit flow.
    implicit_grant_settings: Optional[implicit_grant_settings.ImplicitGrantSettings] = None
    # Specifies the URL that will be used by Microsoft's authorization service to logout an user using front-channel, back-channel or SAML logout protocols.
    logout_url: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The redirectUriSettings property
    redirect_uri_settings: Optional[List[redirect_uri_settings.RedirectUriSettings]] = None
    # Specifies the URLs where user tokens are sent for sign-in, or the redirect URIs where OAuth 2.0 authorization codes and access tokens are sent.
    redirect_uris: Optional[List[str]] = None
    
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
        from . import implicit_grant_settings, redirect_uri_settings

        fields: Dict[str, Callable[[Any], None]] = {
            "homePageUrl": lambda n : setattr(self, 'home_page_url', n.get_str_value()),
            "implicitGrantSettings": lambda n : setattr(self, 'implicit_grant_settings', n.get_object_value(implicit_grant_settings.ImplicitGrantSettings)),
            "logoutUrl": lambda n : setattr(self, 'logout_url', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "redirectUris": lambda n : setattr(self, 'redirect_uris', n.get_collection_of_primitive_values(str)),
            "redirectUriSettings": lambda n : setattr(self, 'redirect_uri_settings', n.get_collection_of_object_values(redirect_uri_settings.RedirectUriSettings)),
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
        writer.write_str_value("homePageUrl", self.home_page_url)
        writer.write_object_value("implicitGrantSettings", self.implicit_grant_settings)
        writer.write_str_value("logoutUrl", self.logout_url)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_primitive_values("redirectUris", self.redirect_uris)
        writer.write_collection_of_object_values("redirectUriSettings", self.redirect_uri_settings)
        writer.write_additional_data_value(self.additional_data)
    

