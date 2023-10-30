from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .automatic_replies_setting import AutomaticRepliesSetting
    from .delegate_meeting_message_delivery_options import DelegateMeetingMessageDeliveryOptions
    from .locale_info import LocaleInfo
    from .user_purpose import UserPurpose
    from .working_hours import WorkingHours

@dataclass
class MailboxSettings(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Folder ID of an archive folder for the user.
    archive_folder: Optional[str] = None
    # Configuration settings to automatically notify the sender of an incoming email with a message from the signed-in user.
    automatic_replies_setting: Optional[AutomaticRepliesSetting] = None
    # The date format for the user's mailbox.
    date_format: Optional[str] = None
    # If the user has a calendar delegate, this specifies whether the delegate, mailbox owner, or both receive meeting messages and meeting responses. Possible values are: sendToDelegateAndInformationToPrincipal, sendToDelegateAndPrincipal, sendToDelegateOnly.
    delegate_meeting_message_delivery_options: Optional[DelegateMeetingMessageDeliveryOptions] = None
    # The locale information for the user, including the preferred language and country/region.
    language: Optional[LocaleInfo] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The time format for the user's mailbox.
    time_format: Optional[str] = None
    # The default time zone for the user's mailbox.
    time_zone: Optional[str] = None
    # The purpose of the mailbox. Differentiates a mailbox for a single user from a shared mailbox and equipment mailbox in Exchange Online. Possible values are: user, linked, shared, room, equipment, others, unknownFutureValue. Read-only.
    user_purpose: Optional[UserPurpose] = None
    # The days of the week and hours in a specific time zone that the user works.
    working_hours: Optional[WorkingHours] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MailboxSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MailboxSettings
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return MailboxSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .automatic_replies_setting import AutomaticRepliesSetting
        from .delegate_meeting_message_delivery_options import DelegateMeetingMessageDeliveryOptions
        from .locale_info import LocaleInfo
        from .user_purpose import UserPurpose
        from .working_hours import WorkingHours

        from .automatic_replies_setting import AutomaticRepliesSetting
        from .delegate_meeting_message_delivery_options import DelegateMeetingMessageDeliveryOptions
        from .locale_info import LocaleInfo
        from .user_purpose import UserPurpose
        from .working_hours import WorkingHours

        fields: Dict[str, Callable[[Any], None]] = {
            "archive_folder": lambda n : setattr(self, 'archive_folder', n.get_str_value()),
            "automatic_replies_setting": lambda n : setattr(self, 'automatic_replies_setting', n.get_object_value(AutomaticRepliesSetting)),
            "date_format": lambda n : setattr(self, 'date_format', n.get_str_value()),
            "delegate_meeting_message_delivery_options": lambda n : setattr(self, 'delegate_meeting_message_delivery_options', n.get_enum_value(DelegateMeetingMessageDeliveryOptions)),
            "language": lambda n : setattr(self, 'language', n.get_object_value(LocaleInfo)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "time_format": lambda n : setattr(self, 'time_format', n.get_str_value()),
            "time_zone": lambda n : setattr(self, 'time_zone', n.get_str_value()),
            "user_purpose": lambda n : setattr(self, 'user_purpose', n.get_enum_value(UserPurpose)),
            "working_hours": lambda n : setattr(self, 'working_hours', n.get_object_value(WorkingHours)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("archive_folder", self.archive_folder)
        writer.write_object_value("automatic_replies_setting", self.automatic_replies_setting)
        writer.write_str_value("date_format", self.date_format)
        writer.write_enum_value("delegate_meeting_message_delivery_options", self.delegate_meeting_message_delivery_options)
        writer.write_object_value("language", self.language)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("time_format", self.time_format)
        writer.write_str_value("time_zone", self.time_zone)
        writer.write_enum_value("user_purpose", self.user_purpose)
        writer.write_object_value("working_hours", self.working_hours)
        writer.write_additional_data_value(self.additional_data)
    

