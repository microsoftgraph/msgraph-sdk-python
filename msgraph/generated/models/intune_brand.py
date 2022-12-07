from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

mime_content = lazy_import('msgraph.generated.models.mime_content')
rgb_color = lazy_import('msgraph.generated.models.rgb_color')

class IntuneBrand(AdditionalDataHolder, Parsable):
    """
    intuneBrand contains data which is used in customizing the appearance of the Company Portal applications as well as the end user web portal.
    """
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
        Instantiates a new intuneBrand and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Email address of the person/organization responsible for IT support.
        self._contact_i_t_email_address: Optional[str] = None
        # Name of the person/organization responsible for IT support.
        self._contact_i_t_name: Optional[str] = None
        # Text comments regarding the person/organization responsible for IT support.
        self._contact_i_t_notes: Optional[str] = None
        # Phone number of the person/organization responsible for IT support.
        self._contact_i_t_phone_number: Optional[str] = None
        # Logo image displayed in Company Portal apps which have a dark background behind the logo.
        self._dark_background_logo: Optional[mime_content.MimeContent] = None
        # Company/organization name that is displayed to end users.
        self._display_name: Optional[str] = None
        # Logo image displayed in Company Portal apps which have a light background behind the logo.
        self._light_background_logo: Optional[mime_content.MimeContent] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Display name of the company/organization’s IT helpdesk site.
        self._online_support_site_name: Optional[str] = None
        # URL to the company/organization’s IT helpdesk site.
        self._online_support_site_url: Optional[str] = None
        # URL to the company/organization’s privacy policy.
        self._privacy_url: Optional[str] = None
        # Boolean that represents whether the administrator-supplied display name will be shown next to the logo image.
        self._show_display_name_next_to_logo: Optional[bool] = None
        # Boolean that represents whether the administrator-supplied logo images are shown or not shown.
        self._show_logo: Optional[bool] = None
        # Boolean that represents whether the administrator-supplied display name will be shown next to the logo image.
        self._show_name_next_to_logo: Optional[bool] = None
        # Primary theme color used in the Company Portal applications and web portal.
        self._theme_color: Optional[rgb_color.RgbColor] = None
    
    @property
    def contact_i_t_email_address(self,) -> Optional[str]:
        """
        Gets the contactITEmailAddress property value. Email address of the person/organization responsible for IT support.
        Returns: Optional[str]
        """
        return self._contact_i_t_email_address
    
    @contact_i_t_email_address.setter
    def contact_i_t_email_address(self,value: Optional[str] = None) -> None:
        """
        Sets the contactITEmailAddress property value. Email address of the person/organization responsible for IT support.
        Args:
            value: Value to set for the contactITEmailAddress property.
        """
        self._contact_i_t_email_address = value
    
    @property
    def contact_i_t_name(self,) -> Optional[str]:
        """
        Gets the contactITName property value. Name of the person/organization responsible for IT support.
        Returns: Optional[str]
        """
        return self._contact_i_t_name
    
    @contact_i_t_name.setter
    def contact_i_t_name(self,value: Optional[str] = None) -> None:
        """
        Sets the contactITName property value. Name of the person/organization responsible for IT support.
        Args:
            value: Value to set for the contactITName property.
        """
        self._contact_i_t_name = value
    
    @property
    def contact_i_t_notes(self,) -> Optional[str]:
        """
        Gets the contactITNotes property value. Text comments regarding the person/organization responsible for IT support.
        Returns: Optional[str]
        """
        return self._contact_i_t_notes
    
    @contact_i_t_notes.setter
    def contact_i_t_notes(self,value: Optional[str] = None) -> None:
        """
        Sets the contactITNotes property value. Text comments regarding the person/organization responsible for IT support.
        Args:
            value: Value to set for the contactITNotes property.
        """
        self._contact_i_t_notes = value
    
    @property
    def contact_i_t_phone_number(self,) -> Optional[str]:
        """
        Gets the contactITPhoneNumber property value. Phone number of the person/organization responsible for IT support.
        Returns: Optional[str]
        """
        return self._contact_i_t_phone_number
    
    @contact_i_t_phone_number.setter
    def contact_i_t_phone_number(self,value: Optional[str] = None) -> None:
        """
        Sets the contactITPhoneNumber property value. Phone number of the person/organization responsible for IT support.
        Args:
            value: Value to set for the contactITPhoneNumber property.
        """
        self._contact_i_t_phone_number = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IntuneBrand:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IntuneBrand
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IntuneBrand()
    
    @property
    def dark_background_logo(self,) -> Optional[mime_content.MimeContent]:
        """
        Gets the darkBackgroundLogo property value. Logo image displayed in Company Portal apps which have a dark background behind the logo.
        Returns: Optional[mime_content.MimeContent]
        """
        return self._dark_background_logo
    
    @dark_background_logo.setter
    def dark_background_logo(self,value: Optional[mime_content.MimeContent] = None) -> None:
        """
        Sets the darkBackgroundLogo property value. Logo image displayed in Company Portal apps which have a dark background behind the logo.
        Args:
            value: Value to set for the darkBackgroundLogo property.
        """
        self._dark_background_logo = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Company/organization name that is displayed to end users.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Company/organization name that is displayed to end users.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "contact_i_t_email_address": lambda n : setattr(self, 'contact_i_t_email_address', n.get_str_value()),
            "contact_i_t_name": lambda n : setattr(self, 'contact_i_t_name', n.get_str_value()),
            "contact_i_t_notes": lambda n : setattr(self, 'contact_i_t_notes', n.get_str_value()),
            "contact_i_t_phone_number": lambda n : setattr(self, 'contact_i_t_phone_number', n.get_str_value()),
            "dark_background_logo": lambda n : setattr(self, 'dark_background_logo', n.get_object_value(mime_content.MimeContent)),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "light_background_logo": lambda n : setattr(self, 'light_background_logo', n.get_object_value(mime_content.MimeContent)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "online_support_site_name": lambda n : setattr(self, 'online_support_site_name', n.get_str_value()),
            "online_support_site_url": lambda n : setattr(self, 'online_support_site_url', n.get_str_value()),
            "privacy_url": lambda n : setattr(self, 'privacy_url', n.get_str_value()),
            "show_display_name_next_to_logo": lambda n : setattr(self, 'show_display_name_next_to_logo', n.get_bool_value()),
            "show_logo": lambda n : setattr(self, 'show_logo', n.get_bool_value()),
            "show_name_next_to_logo": lambda n : setattr(self, 'show_name_next_to_logo', n.get_bool_value()),
            "theme_color": lambda n : setattr(self, 'theme_color', n.get_object_value(rgb_color.RgbColor)),
        }
        return fields
    
    @property
    def light_background_logo(self,) -> Optional[mime_content.MimeContent]:
        """
        Gets the lightBackgroundLogo property value. Logo image displayed in Company Portal apps which have a light background behind the logo.
        Returns: Optional[mime_content.MimeContent]
        """
        return self._light_background_logo
    
    @light_background_logo.setter
    def light_background_logo(self,value: Optional[mime_content.MimeContent] = None) -> None:
        """
        Sets the lightBackgroundLogo property value. Logo image displayed in Company Portal apps which have a light background behind the logo.
        Args:
            value: Value to set for the lightBackgroundLogo property.
        """
        self._light_background_logo = value
    
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
    def online_support_site_name(self,) -> Optional[str]:
        """
        Gets the onlineSupportSiteName property value. Display name of the company/organization’s IT helpdesk site.
        Returns: Optional[str]
        """
        return self._online_support_site_name
    
    @online_support_site_name.setter
    def online_support_site_name(self,value: Optional[str] = None) -> None:
        """
        Sets the onlineSupportSiteName property value. Display name of the company/organization’s IT helpdesk site.
        Args:
            value: Value to set for the onlineSupportSiteName property.
        """
        self._online_support_site_name = value
    
    @property
    def online_support_site_url(self,) -> Optional[str]:
        """
        Gets the onlineSupportSiteUrl property value. URL to the company/organization’s IT helpdesk site.
        Returns: Optional[str]
        """
        return self._online_support_site_url
    
    @online_support_site_url.setter
    def online_support_site_url(self,value: Optional[str] = None) -> None:
        """
        Sets the onlineSupportSiteUrl property value. URL to the company/organization’s IT helpdesk site.
        Args:
            value: Value to set for the onlineSupportSiteUrl property.
        """
        self._online_support_site_url = value
    
    @property
    def privacy_url(self,) -> Optional[str]:
        """
        Gets the privacyUrl property value. URL to the company/organization’s privacy policy.
        Returns: Optional[str]
        """
        return self._privacy_url
    
    @privacy_url.setter
    def privacy_url(self,value: Optional[str] = None) -> None:
        """
        Sets the privacyUrl property value. URL to the company/organization’s privacy policy.
        Args:
            value: Value to set for the privacyUrl property.
        """
        self._privacy_url = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("contactITEmailAddress", self.contact_i_t_email_address)
        writer.write_str_value("contactITName", self.contact_i_t_name)
        writer.write_str_value("contactITNotes", self.contact_i_t_notes)
        writer.write_str_value("contactITPhoneNumber", self.contact_i_t_phone_number)
        writer.write_object_value("darkBackgroundLogo", self.dark_background_logo)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("lightBackgroundLogo", self.light_background_logo)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("onlineSupportSiteName", self.online_support_site_name)
        writer.write_str_value("onlineSupportSiteUrl", self.online_support_site_url)
        writer.write_str_value("privacyUrl", self.privacy_url)
        writer.write_bool_value("showDisplayNameNextToLogo", self.show_display_name_next_to_logo)
        writer.write_bool_value("showLogo", self.show_logo)
        writer.write_bool_value("showNameNextToLogo", self.show_name_next_to_logo)
        writer.write_object_value("themeColor", self.theme_color)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def show_display_name_next_to_logo(self,) -> Optional[bool]:
        """
        Gets the showDisplayNameNextToLogo property value. Boolean that represents whether the administrator-supplied display name will be shown next to the logo image.
        Returns: Optional[bool]
        """
        return self._show_display_name_next_to_logo
    
    @show_display_name_next_to_logo.setter
    def show_display_name_next_to_logo(self,value: Optional[bool] = None) -> None:
        """
        Sets the showDisplayNameNextToLogo property value. Boolean that represents whether the administrator-supplied display name will be shown next to the logo image.
        Args:
            value: Value to set for the showDisplayNameNextToLogo property.
        """
        self._show_display_name_next_to_logo = value
    
    @property
    def show_logo(self,) -> Optional[bool]:
        """
        Gets the showLogo property value. Boolean that represents whether the administrator-supplied logo images are shown or not shown.
        Returns: Optional[bool]
        """
        return self._show_logo
    
    @show_logo.setter
    def show_logo(self,value: Optional[bool] = None) -> None:
        """
        Sets the showLogo property value. Boolean that represents whether the administrator-supplied logo images are shown or not shown.
        Args:
            value: Value to set for the showLogo property.
        """
        self._show_logo = value
    
    @property
    def show_name_next_to_logo(self,) -> Optional[bool]:
        """
        Gets the showNameNextToLogo property value. Boolean that represents whether the administrator-supplied display name will be shown next to the logo image.
        Returns: Optional[bool]
        """
        return self._show_name_next_to_logo
    
    @show_name_next_to_logo.setter
    def show_name_next_to_logo(self,value: Optional[bool] = None) -> None:
        """
        Sets the showNameNextToLogo property value. Boolean that represents whether the administrator-supplied display name will be shown next to the logo image.
        Args:
            value: Value to set for the showNameNextToLogo property.
        """
        self._show_name_next_to_logo = value
    
    @property
    def theme_color(self,) -> Optional[rgb_color.RgbColor]:
        """
        Gets the themeColor property value. Primary theme color used in the Company Portal applications and web portal.
        Returns: Optional[rgb_color.RgbColor]
        """
        return self._theme_color
    
    @theme_color.setter
    def theme_color(self,value: Optional[rgb_color.RgbColor] = None) -> None:
        """
        Sets the themeColor property value. Primary theme color used in the Company Portal applications and web portal.
        Args:
            value: Value to set for the themeColor property.
        """
        self._theme_color = value
    

