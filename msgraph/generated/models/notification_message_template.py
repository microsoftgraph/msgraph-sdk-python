from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
localized_notification_message = lazy_import('msgraph.generated.models.localized_notification_message')
notification_template_branding_options = lazy_import('msgraph.generated.models.notification_template_branding_options')

class NotificationMessageTemplate(entity.Entity):
    """
    Notification messages are messages that are sent to end users who are determined to be not-compliant with the compliance policies defined by the administrator. Administrators choose notifications and configure them in the Intune Admin Console using the compliance policy creation page under the “Actions for non-compliance” section. Use the notificationMessageTemplate object to create your own custom notifications for administrators to choose while configuring actions for non-compliance.
    """
    @property
    def branding_options(self,) -> Optional[notification_template_branding_options.NotificationTemplateBrandingOptions]:
        """
        Gets the brandingOptions property value. Branding Options for the Message Template. Branding is defined in the Intune Admin Console.
        Returns: Optional[notification_template_branding_options.NotificationTemplateBrandingOptions]
        """
        return self._branding_options
    
    @branding_options.setter
    def branding_options(self,value: Optional[notification_template_branding_options.NotificationTemplateBrandingOptions] = None) -> None:
        """
        Sets the brandingOptions property value. Branding Options for the Message Template. Branding is defined in the Intune Admin Console.
        Args:
            value: Value to set for the brandingOptions property.
        """
        self._branding_options = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new notificationMessageTemplate and sets the default values.
        """
        super().__init__()
        # Branding Options for the Message Template. Branding is defined in the Intune Admin Console.
        self._branding_options: Optional[notification_template_branding_options.NotificationTemplateBrandingOptions] = None
        # The default locale to fallback onto when the requested locale is not available.
        self._default_locale: Optional[str] = None
        # Display name for the Notification Message Template.
        self._display_name: Optional[str] = None
        # DateTime the object was last modified.
        self._last_modified_date_time: Optional[datetime] = None
        # The list of localized messages for this Notification Message Template.
        self._localized_notification_messages: Optional[List[localized_notification_message.LocalizedNotificationMessage]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> NotificationMessageTemplate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: NotificationMessageTemplate
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return NotificationMessageTemplate()
    
    @property
    def default_locale(self,) -> Optional[str]:
        """
        Gets the defaultLocale property value. The default locale to fallback onto when the requested locale is not available.
        Returns: Optional[str]
        """
        return self._default_locale
    
    @default_locale.setter
    def default_locale(self,value: Optional[str] = None) -> None:
        """
        Sets the defaultLocale property value. The default locale to fallback onto when the requested locale is not available.
        Args:
            value: Value to set for the defaultLocale property.
        """
        self._default_locale = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Display name for the Notification Message Template.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Display name for the Notification Message Template.
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
            "branding_options": lambda n : setattr(self, 'branding_options', n.get_enum_value(notification_template_branding_options.NotificationTemplateBrandingOptions)),
            "default_locale": lambda n : setattr(self, 'default_locale', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "localized_notification_messages": lambda n : setattr(self, 'localized_notification_messages', n.get_collection_of_object_values(localized_notification_message.LocalizedNotificationMessage)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. DateTime the object was last modified.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. DateTime the object was last modified.
        Args:
            value: Value to set for the lastModifiedDateTime property.
        """
        self._last_modified_date_time = value
    
    @property
    def localized_notification_messages(self,) -> Optional[List[localized_notification_message.LocalizedNotificationMessage]]:
        """
        Gets the localizedNotificationMessages property value. The list of localized messages for this Notification Message Template.
        Returns: Optional[List[localized_notification_message.LocalizedNotificationMessage]]
        """
        return self._localized_notification_messages
    
    @localized_notification_messages.setter
    def localized_notification_messages(self,value: Optional[List[localized_notification_message.LocalizedNotificationMessage]] = None) -> None:
        """
        Sets the localizedNotificationMessages property value. The list of localized messages for this Notification Message Template.
        Args:
            value: Value to set for the localizedNotificationMessages property.
        """
        self._localized_notification_messages = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("brandingOptions", self.branding_options)
        writer.write_str_value("defaultLocale", self.default_locale)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_collection_of_object_values("localizedNotificationMessages", self.localized_notification_messages)
    

