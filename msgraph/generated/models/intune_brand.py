from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .mime_content import MimeContent
    from .rgb_color import RgbColor

@dataclass
class IntuneBrand(AdditionalDataHolder, BackedModel, Parsable):
    """
    intuneBrand contains data which is used in customizing the appearance of the Company Portal applications as well as the end user web portal.
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Email address of the person/organization responsible for IT support.
    contact_i_t_email_address: Optional[str] = None
    # Name of the person/organization responsible for IT support.
    contact_i_t_name: Optional[str] = None
    # Text comments regarding the person/organization responsible for IT support.
    contact_i_t_notes: Optional[str] = None
    # Phone number of the person/organization responsible for IT support.
    contact_i_t_phone_number: Optional[str] = None
    # Logo image displayed in Company Portal apps which have a dark background behind the logo.
    dark_background_logo: Optional[MimeContent] = None
    # Company/organization name that is displayed to end users.
    display_name: Optional[str] = None
    # Logo image displayed in Company Portal apps which have a light background behind the logo.
    light_background_logo: Optional[MimeContent] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Display name of the company/organization’s IT helpdesk site.
    online_support_site_name: Optional[str] = None
    # URL to the company/organization’s IT helpdesk site.
    online_support_site_url: Optional[str] = None
    # URL to the company/organization’s privacy policy.
    privacy_url: Optional[str] = None
    # Boolean that represents whether the administrator-supplied display name will be shown next to the logo image.
    show_display_name_next_to_logo: Optional[bool] = None
    # Boolean that represents whether the administrator-supplied logo images are shown or not shown.
    show_logo: Optional[bool] = None
    # Boolean that represents whether the administrator-supplied display name will be shown next to the logo image.
    show_name_next_to_logo: Optional[bool] = None
    # Primary theme color used in the Company Portal applications and web portal.
    theme_color: Optional[RgbColor] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IntuneBrand:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IntuneBrand
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return IntuneBrand()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .mime_content import MimeContent
        from .rgb_color import RgbColor

        from .mime_content import MimeContent
        from .rgb_color import RgbColor

        fields: dict[str, Callable[[Any], None]] = {
            "contactITEmailAddress": lambda n : setattr(self, 'contact_i_t_email_address', n.get_str_value()),
            "contactITName": lambda n : setattr(self, 'contact_i_t_name', n.get_str_value()),
            "contactITNotes": lambda n : setattr(self, 'contact_i_t_notes', n.get_str_value()),
            "contactITPhoneNumber": lambda n : setattr(self, 'contact_i_t_phone_number', n.get_str_value()),
            "darkBackgroundLogo": lambda n : setattr(self, 'dark_background_logo', n.get_object_value(MimeContent)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lightBackgroundLogo": lambda n : setattr(self, 'light_background_logo', n.get_object_value(MimeContent)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "onlineSupportSiteName": lambda n : setattr(self, 'online_support_site_name', n.get_str_value()),
            "onlineSupportSiteUrl": lambda n : setattr(self, 'online_support_site_url', n.get_str_value()),
            "privacyUrl": lambda n : setattr(self, 'privacy_url', n.get_str_value()),
            "showDisplayNameNextToLogo": lambda n : setattr(self, 'show_display_name_next_to_logo', n.get_bool_value()),
            "showLogo": lambda n : setattr(self, 'show_logo', n.get_bool_value()),
            "showNameNextToLogo": lambda n : setattr(self, 'show_name_next_to_logo', n.get_bool_value()),
            "themeColor": lambda n : setattr(self, 'theme_color', n.get_object_value(RgbColor)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
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
    

