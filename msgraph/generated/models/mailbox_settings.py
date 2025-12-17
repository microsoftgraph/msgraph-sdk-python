from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

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
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Folder ID of an archive folder for the user.
    archive_folder: Optional[str] = None
    # Configuration settings to automatically notify the sender of an incoming email with a message from the signed-in user.
    automatic_replies_setting: Optional[AutomaticRepliesSetting] = None
    # The date format for the user's mailbox.
    date_format: Optional[str] = None
    # If the user has a calendar delegate, this specifies whether the delegate, mailbox owner, or both receive meeting messages and meeting responses. The possible values are: sendToDelegateAndInformationToPrincipal, sendToDelegateAndPrincipal, sendToDelegateOnly.
    delegate_meeting_message_delivery_options: Optional[DelegateMeetingMessageDeliveryOptions] = None
    # The locale information for the user, including the preferred language and country/region.
    language: Optional[LocaleInfo] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The time format for the user's mailbox.
    time_format: Optional[str] = None
    # The default time zone for the user's mailbox.
    time_zone: Optional[str] = None
    # The purpose of the mailbox. Differentiates a mailbox for a single user from a shared mailbox and equipment mailbox in Exchange Online. The possible values are: user, linked, shared, room, equipment, others, unknownFutureValue. Read-only.
    user_purpose: Optional[UserPurpose] = None
    # The days of the week and hours in a specific time zone that the user works.
    working_hours: Optional[WorkingHours] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MailboxSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MailboxSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MailboxSettings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
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

        fields: dict[str, Callable[[Any], None]] = {
            "archiveFolder": lambda n : setattr(self, 'archive_folder', n.get_str_value()),
            "automaticRepliesSetting": lambda n : setattr(self, 'automatic_replies_setting', n.get_object_value(AutomaticRepliesSetting)),
            "dateFormat": lambda n : setattr(self, 'date_format', n.get_str_value()),
            "delegateMeetingMessageDeliveryOptions": lambda n : setattr(self, 'delegate_meeting_message_delivery_options', n.get_enum_value(DelegateMeetingMessageDeliveryOptions)),
            "language": lambda n : setattr(self, 'language', n.get_object_value(LocaleInfo)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "timeFormat": lambda n : setattr(self, 'time_format', n.get_str_value()),
            "timeZone": lambda n : setattr(self, 'time_zone', n.get_str_value()),
            "userPurpose": lambda n : setattr(self, 'user_purpose', n.get_enum_value(UserPurpose)),
            "workingHours": lambda n : setattr(self, 'working_hours', n.get_object_value(WorkingHours)),
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
        writer.write_str_value("archiveFolder", self.archive_folder)
        writer.write_object_value("automaticRepliesSetting", self.automatic_replies_setting)
        writer.write_str_value("dateFormat", self.date_format)
        writer.write_enum_value("delegateMeetingMessageDeliveryOptions", self.delegate_meeting_message_delivery_options)
        writer.write_object_value("language", self.language)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("timeFormat", self.time_format)
        writer.write_str_value("timeZone", self.time_zone)
        writer.write_enum_value("userPurpose", self.user_purpose)
        writer.write_object_value("workingHours", self.working_hours)
        writer.write_additional_data_value(self.additional_data)
    

