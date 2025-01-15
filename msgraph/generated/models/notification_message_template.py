from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .localized_notification_message import LocalizedNotificationMessage
    from .notification_template_branding_options import NotificationTemplateBrandingOptions

from .entity import Entity

@dataclass
class NotificationMessageTemplate(Entity, Parsable):
    """
    Notification messages are messages that are sent to end users who are determined to be not-compliant with the compliance policies defined by the administrator. Administrators choose notifications and configure them in the Intune Admin Console using the compliance policy creation page under the “Actions for non-compliance” section. Use the notificationMessageTemplate object to create your own custom notifications for administrators to choose while configuring actions for non-compliance.
    """
    # Branding Options for the Message Template. Branding is defined in the Intune Admin Console.
    branding_options: Optional[NotificationTemplateBrandingOptions] = None
    # The default locale to fallback onto when the requested locale is not available.
    default_locale: Optional[str] = None
    # Display name for the Notification Message Template.
    display_name: Optional[str] = None
    # DateTime the object was last modified.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The list of localized messages for this Notification Message Template.
    localized_notification_messages: Optional[list[LocalizedNotificationMessage]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # List of Scope Tags for this Entity instance.
    role_scope_tag_ids: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> NotificationMessageTemplate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: NotificationMessageTemplate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return NotificationMessageTemplate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .localized_notification_message import LocalizedNotificationMessage
        from .notification_template_branding_options import NotificationTemplateBrandingOptions

        from .entity import Entity
        from .localized_notification_message import LocalizedNotificationMessage
        from .notification_template_branding_options import NotificationTemplateBrandingOptions

        fields: dict[str, Callable[[Any], None]] = {
            "brandingOptions": lambda n : setattr(self, 'branding_options', n.get_collection_of_enum_values(NotificationTemplateBrandingOptions)),
            "defaultLocale": lambda n : setattr(self, 'default_locale', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "localizedNotificationMessages": lambda n : setattr(self, 'localized_notification_messages', n.get_collection_of_object_values(LocalizedNotificationMessage)),
            "roleScopeTagIds": lambda n : setattr(self, 'role_scope_tag_ids', n.get_collection_of_primitive_values(str)),
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
        writer.write_enum_value("brandingOptions", self.branding_options)
        writer.write_str_value("defaultLocale", self.default_locale)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_collection_of_object_values("localizedNotificationMessages", self.localized_notification_messages)
        writer.write_collection_of_primitive_values("roleScopeTagIds", self.role_scope_tag_ids)
    

