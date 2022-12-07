from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class OrganizationalBrandingProperties(entity.Entity):
    @property
    def background_color(self,) -> Optional[str]:
        """
        Gets the backgroundColor property value. Color that will appear in place of the background image in low-bandwidth connections. We recommend that you use the primary color of your banner logo or your organization color. Specify this in hexadecimal format, for example, white is #FFFFFF.
        Returns: Optional[str]
        """
        return self._background_color
    
    @background_color.setter
    def background_color(self,value: Optional[str] = None) -> None:
        """
        Sets the backgroundColor property value. Color that will appear in place of the background image in low-bandwidth connections. We recommend that you use the primary color of your banner logo or your organization color. Specify this in hexadecimal format, for example, white is #FFFFFF.
        Args:
            value: Value to set for the backgroundColor property.
        """
        self._background_color = value
    
    @property
    def background_image(self,) -> Optional[bytes]:
        """
        Gets the backgroundImage property value. Image that appears as the background of the sign-in page. The allowed types are PNG or JPEG not smaller than 300 KB and not larger than 1920 × 1080 pixels. A smaller image will reduce bandwidth requirements and make the page load faster.
        Returns: Optional[bytes]
        """
        return self._background_image
    
    @background_image.setter
    def background_image(self,value: Optional[bytes] = None) -> None:
        """
        Sets the backgroundImage property value. Image that appears as the background of the sign-in page. The allowed types are PNG or JPEG not smaller than 300 KB and not larger than 1920 × 1080 pixels. A smaller image will reduce bandwidth requirements and make the page load faster.
        Args:
            value: Value to set for the backgroundImage property.
        """
        self._background_image = value
    
    @property
    def background_image_relative_url(self,) -> Optional[str]:
        """
        Gets the backgroundImageRelativeUrl property value. A relative URL for the backgroundImage property that is combined with a CDN base URL from the cdnList to provide the version served by a CDN. Read-only.
        Returns: Optional[str]
        """
        return self._background_image_relative_url
    
    @background_image_relative_url.setter
    def background_image_relative_url(self,value: Optional[str] = None) -> None:
        """
        Sets the backgroundImageRelativeUrl property value. A relative URL for the backgroundImage property that is combined with a CDN base URL from the cdnList to provide the version served by a CDN. Read-only.
        Args:
            value: Value to set for the backgroundImageRelativeUrl property.
        """
        self._background_image_relative_url = value
    
    @property
    def banner_logo(self,) -> Optional[bytes]:
        """
        Gets the bannerLogo property value. A banner version of your company logo that appears on the sign-in page. The allowed types are PNG or JPEG no larger than 36 × 245 pixels. We recommend using a transparent image with no padding around the logo.
        Returns: Optional[bytes]
        """
        return self._banner_logo
    
    @banner_logo.setter
    def banner_logo(self,value: Optional[bytes] = None) -> None:
        """
        Sets the bannerLogo property value. A banner version of your company logo that appears on the sign-in page. The allowed types are PNG or JPEG no larger than 36 × 245 pixels. We recommend using a transparent image with no padding around the logo.
        Args:
            value: Value to set for the bannerLogo property.
        """
        self._banner_logo = value
    
    @property
    def banner_logo_relative_url(self,) -> Optional[str]:
        """
        Gets the bannerLogoRelativeUrl property value. A relative url for the bannerLogo property that is combined with a CDN base URL from the cdnList to provide the read-only version served by a CDN. Read-only.
        Returns: Optional[str]
        """
        return self._banner_logo_relative_url
    
    @banner_logo_relative_url.setter
    def banner_logo_relative_url(self,value: Optional[str] = None) -> None:
        """
        Sets the bannerLogoRelativeUrl property value. A relative url for the bannerLogo property that is combined with a CDN base URL from the cdnList to provide the read-only version served by a CDN. Read-only.
        Args:
            value: Value to set for the bannerLogoRelativeUrl property.
        """
        self._banner_logo_relative_url = value
    
    @property
    def cdn_list(self,) -> Optional[List[str]]:
        """
        Gets the cdnList property value. A list of base URLs for all available CDN providers that are serving the assets of the current resource. Several CDN providers are used at the same time for high availability of read requests. Read-only.
        Returns: Optional[List[str]]
        """
        return self._cdn_list
    
    @cdn_list.setter
    def cdn_list(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the cdnList property value. A list of base URLs for all available CDN providers that are serving the assets of the current resource. Several CDN providers are used at the same time for high availability of read requests. Read-only.
        Args:
            value: Value to set for the cdnList property.
        """
        self._cdn_list = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new organizationalBrandingProperties and sets the default values.
        """
        super().__init__()
        # Color that will appear in place of the background image in low-bandwidth connections. We recommend that you use the primary color of your banner logo or your organization color. Specify this in hexadecimal format, for example, white is #FFFFFF.
        self._background_color: Optional[str] = None
        # Image that appears as the background of the sign-in page. The allowed types are PNG or JPEG not smaller than 300 KB and not larger than 1920 × 1080 pixels. A smaller image will reduce bandwidth requirements and make the page load faster.
        self._background_image: Optional[bytes] = None
        # A relative URL for the backgroundImage property that is combined with a CDN base URL from the cdnList to provide the version served by a CDN. Read-only.
        self._background_image_relative_url: Optional[str] = None
        # A banner version of your company logo that appears on the sign-in page. The allowed types are PNG or JPEG no larger than 36 × 245 pixels. We recommend using a transparent image with no padding around the logo.
        self._banner_logo: Optional[bytes] = None
        # A relative url for the bannerLogo property that is combined with a CDN base URL from the cdnList to provide the read-only version served by a CDN. Read-only.
        self._banner_logo_relative_url: Optional[str] = None
        # A list of base URLs for all available CDN providers that are serving the assets of the current resource. Several CDN providers are used at the same time for high availability of read requests. Read-only.
        self._cdn_list: Optional[List[str]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Text that appears at the bottom of the sign-in box. You can use this to communicate additional information, such as the phone number to your help desk or a legal statement. This text must be Unicode and not exceed 1024 characters.
        self._sign_in_page_text: Optional[str] = None
        # A square version of your company logo that appears in Windows 10 out-of-box experiences (OOBE) and when Windows Autopilot is enabled for deployment. Allowed types are PNG or JPEG no larger than 240 x 240 pixels and no more than 10 KB in size. We recommend using a transparent image with no padding around the logo.
        self._square_logo: Optional[bytes] = None
        # A relative url for the squareLogo property that is combined with a CDN base URL from the cdnList to provide the version served by a CDN. Read-only.
        self._square_logo_relative_url: Optional[str] = None
        # String that shows as the hint in the username textbox on the sign-in screen. This text must be a Unicode, without links or code, and can't exceed 64 characters.
        self._username_hint_text: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OrganizationalBrandingProperties:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OrganizationalBrandingProperties
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return OrganizationalBrandingProperties()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "background_color": lambda n : setattr(self, 'background_color', n.get_str_value()),
            "background_image": lambda n : setattr(self, 'background_image', n.get_bytes_value()),
            "background_image_relative_url": lambda n : setattr(self, 'background_image_relative_url', n.get_str_value()),
            "banner_logo": lambda n : setattr(self, 'banner_logo', n.get_bytes_value()),
            "banner_logo_relative_url": lambda n : setattr(self, 'banner_logo_relative_url', n.get_str_value()),
            "cdn_list": lambda n : setattr(self, 'cdn_list', n.get_collection_of_primitive_values(str)),
            "sign_in_page_text": lambda n : setattr(self, 'sign_in_page_text', n.get_str_value()),
            "square_logo": lambda n : setattr(self, 'square_logo', n.get_bytes_value()),
            "square_logo_relative_url": lambda n : setattr(self, 'square_logo_relative_url', n.get_str_value()),
            "username_hint_text": lambda n : setattr(self, 'username_hint_text', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("backgroundColor", self.background_color)
        writer.write_object_value("backgroundImage", self.background_image)
        writer.write_str_value("backgroundImageRelativeUrl", self.background_image_relative_url)
        writer.write_object_value("bannerLogo", self.banner_logo)
        writer.write_str_value("bannerLogoRelativeUrl", self.banner_logo_relative_url)
        writer.write_collection_of_primitive_values("cdnList", self.cdn_list)
        writer.write_str_value("signInPageText", self.sign_in_page_text)
        writer.write_object_value("squareLogo", self.square_logo)
        writer.write_str_value("squareLogoRelativeUrl", self.square_logo_relative_url)
        writer.write_str_value("usernameHintText", self.username_hint_text)
    
    @property
    def sign_in_page_text(self,) -> Optional[str]:
        """
        Gets the signInPageText property value. Text that appears at the bottom of the sign-in box. You can use this to communicate additional information, such as the phone number to your help desk or a legal statement. This text must be Unicode and not exceed 1024 characters.
        Returns: Optional[str]
        """
        return self._sign_in_page_text
    
    @sign_in_page_text.setter
    def sign_in_page_text(self,value: Optional[str] = None) -> None:
        """
        Sets the signInPageText property value. Text that appears at the bottom of the sign-in box. You can use this to communicate additional information, such as the phone number to your help desk or a legal statement. This text must be Unicode and not exceed 1024 characters.
        Args:
            value: Value to set for the signInPageText property.
        """
        self._sign_in_page_text = value
    
    @property
    def square_logo(self,) -> Optional[bytes]:
        """
        Gets the squareLogo property value. A square version of your company logo that appears in Windows 10 out-of-box experiences (OOBE) and when Windows Autopilot is enabled for deployment. Allowed types are PNG or JPEG no larger than 240 x 240 pixels and no more than 10 KB in size. We recommend using a transparent image with no padding around the logo.
        Returns: Optional[bytes]
        """
        return self._square_logo
    
    @square_logo.setter
    def square_logo(self,value: Optional[bytes] = None) -> None:
        """
        Sets the squareLogo property value. A square version of your company logo that appears in Windows 10 out-of-box experiences (OOBE) and when Windows Autopilot is enabled for deployment. Allowed types are PNG or JPEG no larger than 240 x 240 pixels and no more than 10 KB in size. We recommend using a transparent image with no padding around the logo.
        Args:
            value: Value to set for the squareLogo property.
        """
        self._square_logo = value
    
    @property
    def square_logo_relative_url(self,) -> Optional[str]:
        """
        Gets the squareLogoRelativeUrl property value. A relative url for the squareLogo property that is combined with a CDN base URL from the cdnList to provide the version served by a CDN. Read-only.
        Returns: Optional[str]
        """
        return self._square_logo_relative_url
    
    @square_logo_relative_url.setter
    def square_logo_relative_url(self,value: Optional[str] = None) -> None:
        """
        Sets the squareLogoRelativeUrl property value. A relative url for the squareLogo property that is combined with a CDN base URL from the cdnList to provide the version served by a CDN. Read-only.
        Args:
            value: Value to set for the squareLogoRelativeUrl property.
        """
        self._square_logo_relative_url = value
    
    @property
    def username_hint_text(self,) -> Optional[str]:
        """
        Gets the usernameHintText property value. String that shows as the hint in the username textbox on the sign-in screen. This text must be a Unicode, without links or code, and can't exceed 64 characters.
        Returns: Optional[str]
        """
        return self._username_hint_text
    
    @username_hint_text.setter
    def username_hint_text(self,value: Optional[str] = None) -> None:
        """
        Sets the usernameHintText property value. String that shows as the hint in the username textbox on the sign-in screen. This text must be a Unicode, without links or code, and can't exceed 64 characters.
        Args:
            value: Value to set for the usernameHintText property.
        """
        self._username_hint_text = value
    

