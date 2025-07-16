from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .content_customization import ContentCustomization
    from .entity import Entity
    from .login_page_layout_configuration import LoginPageLayoutConfiguration
    from .login_page_text_visibility_settings import LoginPageTextVisibilitySettings
    from .organizational_branding import OrganizationalBranding
    from .organizational_branding_localization import OrganizationalBrandingLocalization

from .entity import Entity

@dataclass
class OrganizationalBrandingProperties(Entity, Parsable):
    # Color that appears in place of the background image in low-bandwidth connections. We recommend that you use the primary color of your banner logo or your organization color. Specify this in hexadecimal format, for example, white is #FFFFFF.
    background_color: Optional[str] = None
    # Image that appears as the background of the sign-in page. The allowed types are PNG or JPEG not smaller than 300 KB and not larger than 1920 × 1080 pixels. A smaller image reduces bandwidth requirements and make the page load faster.
    background_image: Optional[bytes] = None
    # A relative URL for the backgroundImage property that is combined with a CDN base URL from the cdnList to provide the version served by a CDN. Read-only.
    background_image_relative_url: Optional[str] = None
    # A banner version of your company logo that appears on the sign-in page. The allowed types are PNG or JPEG not larger than 36 × 245 pixels. We recommend using a transparent image with no padding around the logo.
    banner_logo: Optional[bytes] = None
    # A relative URL for the bannerLogo property that is combined with a CDN base URL from the cdnList to provide the read-only version served by a CDN. Read-only.
    banner_logo_relative_url: Optional[str] = None
    # A list of base URLs for all available CDN providers that are serving the assets of the current resource. Several CDN providers are used at the same time for high availability of read requests. Read-only.
    cdn_list: Optional[list[str]] = None
    # Represents the content options to be customized throughout the authentication flow for a tenant. NOTE: Supported by Microsoft Entra External ID in external tenants only.
    content_customization: Optional[ContentCustomization] = None
    # A custom URL for resetting account credentials. This URL must be in ASCII format or non-ASCII characters must be URL encoded, and not exceed 128 characters.
    custom_account_reset_credentials_url: Optional[str] = None
    # CSS styling that appears on the sign-in page. The allowed format is .css format only and not larger than 25 KB.
    custom_c_s_s: Optional[bytes] = None
    # A relative URL for the customCSS property that is combined with a CDN base URL from the cdnList to provide the version served by a CDN. Read-only.
    custom_c_s_s_relative_url: Optional[str] = None
    # A string to replace the default 'Can't access your account?' self-service password reset (SSPR) hyperlink text on the sign-in page. This text must be in Unicode format and not exceed 256 characters.
    custom_cannot_access_your_account_text: Optional[str] = None
    # A custom URL to replace the default URL of the self-service password reset (SSPR) 'Can't access your account?' hyperlink on the sign-in page. This URL must be in ASCII format or non-ASCII characters must be URL encoded, and not exceed 128 characters. DO NOT USE. Use customAccountResetCredentialsUrl instead.
    custom_cannot_access_your_account_url: Optional[str] = None
    # A string to replace the default 'Forgot my password' hyperlink text on the sign-in form. This text must be in Unicode format and not exceed 256 characters.
    custom_forgot_my_password_text: Optional[str] = None
    # A string to replace the default 'Privacy and Cookies' hyperlink text in the footer. This text must be in Unicode format and not exceed 256 characters.
    custom_privacy_and_cookies_text: Optional[str] = None
    # A custom URL to replace the default URL of the 'Privacy and Cookies' hyperlink in the footer. This URL must be in ASCII format or non-ASCII characters must be URL encoded, and not exceed 128 characters.
    custom_privacy_and_cookies_url: Optional[str] = None
    # A string to replace the default 'reset it now' hyperlink text on the sign-in form. This text must be in Unicode format and not exceed 256 characters. DO NOT USE: Customization of the 'reset it now' hyperlink text is currently not supported.
    custom_reset_it_now_text: Optional[str] = None
    # A string to replace the the default 'Terms of Use' hyperlink text in the footer. This text must be in Unicode format and not exceed 256 characters.
    custom_terms_of_use_text: Optional[str] = None
    # A custom URL to replace the default URL of the 'Terms of Use' hyperlink in the footer. This URL must be in ASCII format or non-ASCII characters must be URL encoded, and not exceed 128characters.
    custom_terms_of_use_url: Optional[str] = None
    # A custom icon (favicon) to replace a default Microsoft product favicon on a Microsoft Entra tenant.
    favicon: Optional[bytes] = None
    # A relative url for the favicon above that is combined with a CDN base URL from the cdnList to provide the version served by a CDN. Read-only.
    favicon_relative_url: Optional[str] = None
    # The RGB color to apply to customize the color of the header.
    header_background_color: Optional[str] = None
    # A company logo that appears in the header of the sign-in page. The allowed types are PNG or JPEG not larger than 36 × 245 pixels. We recommend using a transparent image with no padding around the logo.
    header_logo: Optional[bytes] = None
    # A relative URL for the headerLogo property that is combined with a CDN base URL from the cdnList to provide the read-only version served by a CDN. Read-only.
    header_logo_relative_url: Optional[str] = None
    # Represents the layout configuration to be displayed on the login page for a tenant.
    login_page_layout_configuration: Optional[LoginPageLayoutConfiguration] = None
    # Represents the various texts that can be hidden on the login page for a tenant.
    login_page_text_visibility_settings: Optional[LoginPageTextVisibilitySettings] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Text that appears at the bottom of the sign-in box. Use this to communicate additional information, such as the phone number to your help desk or a legal statement. This text must be in Unicode format and not exceed 1024 characters.
    sign_in_page_text: Optional[str] = None
    # A square version of your company logo that appears in Windows 10 out-of-box experiences (OOBE) and when Windows Autopilot is enabled for deployment. Allowed types are PNG or JPEG not larger than 240 x 240 pixels and not more than 10 KB in size. We recommend using a transparent image with no padding around the logo.
    square_logo: Optional[bytes] = None
    # A square dark version of your company logo that appears in Windows 10 out-of-box experiences (OOBE) and when Windows Autopilot is enabled for deployment. Allowed types are PNG or JPEG not larger than 240 x 240 pixels and not more than 10 KB in size. We recommend using a transparent image with no padding around the logo.
    square_logo_dark: Optional[bytes] = None
    # A relative URL for the squareLogoDark property that is combined with a CDN base URL from the cdnList to provide the version served by a CDN. Read-only.
    square_logo_dark_relative_url: Optional[str] = None
    # A relative URL for the squareLogo property that is combined with a CDN base URL from the cdnList to provide the version served by a CDN. Read-only.
    square_logo_relative_url: Optional[str] = None
    # A string that shows as the hint in the username textbox on the sign-in screen. This text must be a Unicode, without links or code, and can't exceed 64 characters.
    username_hint_text: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OrganizationalBrandingProperties:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OrganizationalBrandingProperties
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.organizationalBranding".casefold():
            from .organizational_branding import OrganizationalBranding

            return OrganizationalBranding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.organizationalBrandingLocalization".casefold():
            from .organizational_branding_localization import OrganizationalBrandingLocalization

            return OrganizationalBrandingLocalization()
        return OrganizationalBrandingProperties()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .content_customization import ContentCustomization
        from .entity import Entity
        from .login_page_layout_configuration import LoginPageLayoutConfiguration
        from .login_page_text_visibility_settings import LoginPageTextVisibilitySettings
        from .organizational_branding import OrganizationalBranding
        from .organizational_branding_localization import OrganizationalBrandingLocalization

        from .content_customization import ContentCustomization
        from .entity import Entity
        from .login_page_layout_configuration import LoginPageLayoutConfiguration
        from .login_page_text_visibility_settings import LoginPageTextVisibilitySettings
        from .organizational_branding import OrganizationalBranding
        from .organizational_branding_localization import OrganizationalBrandingLocalization

        fields: dict[str, Callable[[Any], None]] = {
            "backgroundColor": lambda n : setattr(self, 'background_color', n.get_str_value()),
            "backgroundImage": lambda n : setattr(self, 'background_image', n.get_bytes_value()),
            "backgroundImageRelativeUrl": lambda n : setattr(self, 'background_image_relative_url', n.get_str_value()),
            "bannerLogo": lambda n : setattr(self, 'banner_logo', n.get_bytes_value()),
            "bannerLogoRelativeUrl": lambda n : setattr(self, 'banner_logo_relative_url', n.get_str_value()),
            "cdnList": lambda n : setattr(self, 'cdn_list', n.get_collection_of_primitive_values(str)),
            "contentCustomization": lambda n : setattr(self, 'content_customization', n.get_object_value(ContentCustomization)),
            "customAccountResetCredentialsUrl": lambda n : setattr(self, 'custom_account_reset_credentials_url', n.get_str_value()),
            "customCSS": lambda n : setattr(self, 'custom_c_s_s', n.get_bytes_value()),
            "customCSSRelativeUrl": lambda n : setattr(self, 'custom_c_s_s_relative_url', n.get_str_value()),
            "customCannotAccessYourAccountText": lambda n : setattr(self, 'custom_cannot_access_your_account_text', n.get_str_value()),
            "customCannotAccessYourAccountUrl": lambda n : setattr(self, 'custom_cannot_access_your_account_url', n.get_str_value()),
            "customForgotMyPasswordText": lambda n : setattr(self, 'custom_forgot_my_password_text', n.get_str_value()),
            "customPrivacyAndCookiesText": lambda n : setattr(self, 'custom_privacy_and_cookies_text', n.get_str_value()),
            "customPrivacyAndCookiesUrl": lambda n : setattr(self, 'custom_privacy_and_cookies_url', n.get_str_value()),
            "customResetItNowText": lambda n : setattr(self, 'custom_reset_it_now_text', n.get_str_value()),
            "customTermsOfUseText": lambda n : setattr(self, 'custom_terms_of_use_text', n.get_str_value()),
            "customTermsOfUseUrl": lambda n : setattr(self, 'custom_terms_of_use_url', n.get_str_value()),
            "favicon": lambda n : setattr(self, 'favicon', n.get_bytes_value()),
            "faviconRelativeUrl": lambda n : setattr(self, 'favicon_relative_url', n.get_str_value()),
            "headerBackgroundColor": lambda n : setattr(self, 'header_background_color', n.get_str_value()),
            "headerLogo": lambda n : setattr(self, 'header_logo', n.get_bytes_value()),
            "headerLogoRelativeUrl": lambda n : setattr(self, 'header_logo_relative_url', n.get_str_value()),
            "loginPageLayoutConfiguration": lambda n : setattr(self, 'login_page_layout_configuration', n.get_object_value(LoginPageLayoutConfiguration)),
            "loginPageTextVisibilitySettings": lambda n : setattr(self, 'login_page_text_visibility_settings', n.get_object_value(LoginPageTextVisibilitySettings)),
            "signInPageText": lambda n : setattr(self, 'sign_in_page_text', n.get_str_value()),
            "squareLogo": lambda n : setattr(self, 'square_logo', n.get_bytes_value()),
            "squareLogoDark": lambda n : setattr(self, 'square_logo_dark', n.get_bytes_value()),
            "squareLogoDarkRelativeUrl": lambda n : setattr(self, 'square_logo_dark_relative_url', n.get_str_value()),
            "squareLogoRelativeUrl": lambda n : setattr(self, 'square_logo_relative_url', n.get_str_value()),
            "usernameHintText": lambda n : setattr(self, 'username_hint_text', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("backgroundColor", self.background_color)
        writer.write_bytes_value("backgroundImage", self.background_image)
        writer.write_str_value("backgroundImageRelativeUrl", self.background_image_relative_url)
        writer.write_bytes_value("bannerLogo", self.banner_logo)
        writer.write_str_value("bannerLogoRelativeUrl", self.banner_logo_relative_url)
        writer.write_collection_of_primitive_values("cdnList", self.cdn_list)
        writer.write_object_value("contentCustomization", self.content_customization)
        writer.write_str_value("customAccountResetCredentialsUrl", self.custom_account_reset_credentials_url)
        writer.write_bytes_value("customCSS", self.custom_c_s_s)
        writer.write_str_value("customCSSRelativeUrl", self.custom_c_s_s_relative_url)
        writer.write_str_value("customCannotAccessYourAccountText", self.custom_cannot_access_your_account_text)
        writer.write_str_value("customCannotAccessYourAccountUrl", self.custom_cannot_access_your_account_url)
        writer.write_str_value("customForgotMyPasswordText", self.custom_forgot_my_password_text)
        writer.write_str_value("customPrivacyAndCookiesText", self.custom_privacy_and_cookies_text)
        writer.write_str_value("customPrivacyAndCookiesUrl", self.custom_privacy_and_cookies_url)
        writer.write_str_value("customResetItNowText", self.custom_reset_it_now_text)
        writer.write_str_value("customTermsOfUseText", self.custom_terms_of_use_text)
        writer.write_str_value("customTermsOfUseUrl", self.custom_terms_of_use_url)
        writer.write_bytes_value("favicon", self.favicon)
        writer.write_str_value("faviconRelativeUrl", self.favicon_relative_url)
        writer.write_str_value("headerBackgroundColor", self.header_background_color)
        writer.write_bytes_value("headerLogo", self.header_logo)
        writer.write_str_value("headerLogoRelativeUrl", self.header_logo_relative_url)
        writer.write_object_value("loginPageLayoutConfiguration", self.login_page_layout_configuration)
        writer.write_object_value("loginPageTextVisibilitySettings", self.login_page_text_visibility_settings)
        writer.write_str_value("signInPageText", self.sign_in_page_text)
        writer.write_bytes_value("squareLogo", self.square_logo)
        writer.write_bytes_value("squareLogoDark", self.square_logo_dark)
        writer.write_str_value("squareLogoDarkRelativeUrl", self.square_logo_dark_relative_url)
        writer.write_str_value("squareLogoRelativeUrl", self.square_logo_relative_url)
        writer.write_str_value("usernameHintText", self.username_hint_text)
    

