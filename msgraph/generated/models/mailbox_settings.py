from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import automatic_replies_setting, delegate_meeting_message_delivery_options, locale_info, user_purpose, working_hours

@dataclass
class MailboxSettings(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Folder ID of an archive folder for the user.
    archive_folder: Optional[str] = None
    # Configuration settings to automatically notify the sender of an incoming email with a message from the signed-in user.
    automatic_replies_setting: Optional[automatic_replies_setting.AutomaticRepliesSetting] = None
    # The date format for the user's mailbox.
    date_format: Optional[str] = None
    # If the user has a calendar delegate, this specifies whether the delegate, mailbox owner, or both receive meeting messages and meeting responses. Possible values are: sendToDelegateAndInformationToPrincipal, sendToDelegateAndPrincipal, sendToDelegateOnly.
    delegate_meeting_message_delivery_options: Optional[delegate_meeting_message_delivery_options.DelegateMeetingMessageDeliveryOptions] = None
    # The locale information for the user, including the preferred language and country/region.
    language: Optional[locale_info.LocaleInfo] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The time format for the user's mailbox.
    time_format: Optional[str] = None
    # The default time zone for the user's mailbox.
    time_zone: Optional[str] = None
    # The purpose of the mailbox. Differentiates a mailbox for a single user from a shared mailbox and equipment mailbox in Exchange Online. Possible values are: user, linked, shared, room, equipment, others, unknownFutureValue. Read-only.
    user_purpose: Optional[user_purpose.UserPurpose] = None
    # The days of the week and hours in a specific time zone that the user works.
    working_hours: Optional[working_hours.WorkingHours] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MailboxSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MailboxSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MailboxSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import automatic_replies_setting, delegate_meeting_message_delivery_options, locale_info, user_purpose, working_hours

        fields: Dict[str, Callable[[Any], None]] = {
            "archiveFolder": lambda n : setattr(self, 'archive_folder', n.get_str_value()),
            "automaticRepliesSetting": lambda n : setattr(self, 'automatic_replies_setting', n.get_object_value(automatic_replies_setting.AutomaticRepliesSetting)),
            "dateFormat": lambda n : setattr(self, 'date_format', n.get_str_value()),
            "delegateMeetingMessageDeliveryOptions": lambda n : setattr(self, 'delegate_meeting_message_delivery_options', n.get_enum_value(delegate_meeting_message_delivery_options.DelegateMeetingMessageDeliveryOptions)),
            "language": lambda n : setattr(self, 'language', n.get_object_value(locale_info.LocaleInfo)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "timeFormat": lambda n : setattr(self, 'time_format', n.get_str_value()),
            "timeZone": lambda n : setattr(self, 'time_zone', n.get_str_value()),
            "userPurpose": lambda n : setattr(self, 'user_purpose', n.get_enum_value(user_purpose.UserPurpose)),
            "workingHours": lambda n : setattr(self, 'working_hours', n.get_object_value(working_hours.WorkingHours)),
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
    

