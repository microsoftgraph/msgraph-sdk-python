from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

automatic_replies_setting = lazy_import('msgraph.generated.models.automatic_replies_setting')
delegate_meeting_message_delivery_options = lazy_import('msgraph.generated.models.delegate_meeting_message_delivery_options')
locale_info = lazy_import('msgraph.generated.models.locale_info')
user_purpose = lazy_import('msgraph.generated.models.user_purpose')
working_hours = lazy_import('msgraph.generated.models.working_hours')

class MailboxSettings(AdditionalDataHolder, Parsable):
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
    
    @property
    def archive_folder(self,) -> Optional[str]:
        """
        Gets the archiveFolder property value. Folder ID of an archive folder for the user.
        Returns: Optional[str]
        """
        return self._archive_folder
    
    @archive_folder.setter
    def archive_folder(self,value: Optional[str] = None) -> None:
        """
        Sets the archiveFolder property value. Folder ID of an archive folder for the user.
        Args:
            value: Value to set for the archiveFolder property.
        """
        self._archive_folder = value
    
    @property
    def automatic_replies_setting(self,) -> Optional[automatic_replies_setting.AutomaticRepliesSetting]:
        """
        Gets the automaticRepliesSetting property value. Configuration settings to automatically notify the sender of an incoming email with a message from the signed-in user.
        Returns: Optional[automatic_replies_setting.AutomaticRepliesSetting]
        """
        return self._automatic_replies_setting
    
    @automatic_replies_setting.setter
    def automatic_replies_setting(self,value: Optional[automatic_replies_setting.AutomaticRepliesSetting] = None) -> None:
        """
        Sets the automaticRepliesSetting property value. Configuration settings to automatically notify the sender of an incoming email with a message from the signed-in user.
        Args:
            value: Value to set for the automaticRepliesSetting property.
        """
        self._automatic_replies_setting = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new mailboxSettings and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Folder ID of an archive folder for the user.
        self._archive_folder: Optional[str] = None
        # Configuration settings to automatically notify the sender of an incoming email with a message from the signed-in user.
        self._automatic_replies_setting: Optional[automatic_replies_setting.AutomaticRepliesSetting] = None
        # The date format for the user's mailbox.
        self._date_format: Optional[str] = None
        # If the user has a calendar delegate, this specifies whether the delegate, mailbox owner, or both receive meeting messages and meeting responses. Possible values are: sendToDelegateAndInformationToPrincipal, sendToDelegateAndPrincipal, sendToDelegateOnly.
        self._delegate_meeting_message_delivery_options: Optional[delegate_meeting_message_delivery_options.DelegateMeetingMessageDeliveryOptions] = None
        # The locale information for the user, including the preferred language and country/region.
        self._language: Optional[locale_info.LocaleInfo] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The time format for the user's mailbox.
        self._time_format: Optional[str] = None
        # The default time zone for the user's mailbox.
        self._time_zone: Optional[str] = None
        # The userPurpose property
        self._user_purpose: Optional[user_purpose.UserPurpose] = None
        # The days of the week and hours in a specific time zone that the user works.
        self._working_hours: Optional[working_hours.WorkingHours] = None
    
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
    
    @property
    def date_format(self,) -> Optional[str]:
        """
        Gets the dateFormat property value. The date format for the user's mailbox.
        Returns: Optional[str]
        """
        return self._date_format
    
    @date_format.setter
    def date_format(self,value: Optional[str] = None) -> None:
        """
        Sets the dateFormat property value. The date format for the user's mailbox.
        Args:
            value: Value to set for the dateFormat property.
        """
        self._date_format = value
    
    @property
    def delegate_meeting_message_delivery_options(self,) -> Optional[delegate_meeting_message_delivery_options.DelegateMeetingMessageDeliveryOptions]:
        """
        Gets the delegateMeetingMessageDeliveryOptions property value. If the user has a calendar delegate, this specifies whether the delegate, mailbox owner, or both receive meeting messages and meeting responses. Possible values are: sendToDelegateAndInformationToPrincipal, sendToDelegateAndPrincipal, sendToDelegateOnly.
        Returns: Optional[delegate_meeting_message_delivery_options.DelegateMeetingMessageDeliveryOptions]
        """
        return self._delegate_meeting_message_delivery_options
    
    @delegate_meeting_message_delivery_options.setter
    def delegate_meeting_message_delivery_options(self,value: Optional[delegate_meeting_message_delivery_options.DelegateMeetingMessageDeliveryOptions] = None) -> None:
        """
        Sets the delegateMeetingMessageDeliveryOptions property value. If the user has a calendar delegate, this specifies whether the delegate, mailbox owner, or both receive meeting messages and meeting responses. Possible values are: sendToDelegateAndInformationToPrincipal, sendToDelegateAndPrincipal, sendToDelegateOnly.
        Args:
            value: Value to set for the delegateMeetingMessageDeliveryOptions property.
        """
        self._delegate_meeting_message_delivery_options = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "archive_folder": lambda n : setattr(self, 'archive_folder', n.get_str_value()),
            "automatic_replies_setting": lambda n : setattr(self, 'automatic_replies_setting', n.get_object_value(automatic_replies_setting.AutomaticRepliesSetting)),
            "date_format": lambda n : setattr(self, 'date_format', n.get_str_value()),
            "delegate_meeting_message_delivery_options": lambda n : setattr(self, 'delegate_meeting_message_delivery_options', n.get_enum_value(delegate_meeting_message_delivery_options.DelegateMeetingMessageDeliveryOptions)),
            "language": lambda n : setattr(self, 'language', n.get_object_value(locale_info.LocaleInfo)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "time_format": lambda n : setattr(self, 'time_format', n.get_str_value()),
            "time_zone": lambda n : setattr(self, 'time_zone', n.get_str_value()),
            "user_purpose": lambda n : setattr(self, 'user_purpose', n.get_enum_value(user_purpose.UserPurpose)),
            "working_hours": lambda n : setattr(self, 'working_hours', n.get_object_value(working_hours.WorkingHours)),
        }
        return fields
    
    @property
    def language(self,) -> Optional[locale_info.LocaleInfo]:
        """
        Gets the language property value. The locale information for the user, including the preferred language and country/region.
        Returns: Optional[locale_info.LocaleInfo]
        """
        return self._language
    
    @language.setter
    def language(self,value: Optional[locale_info.LocaleInfo] = None) -> None:
        """
        Sets the language property value. The locale information for the user, including the preferred language and country/region.
        Args:
            value: Value to set for the language property.
        """
        self._language = value
    
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
    
    @property
    def time_format(self,) -> Optional[str]:
        """
        Gets the timeFormat property value. The time format for the user's mailbox.
        Returns: Optional[str]
        """
        return self._time_format
    
    @time_format.setter
    def time_format(self,value: Optional[str] = None) -> None:
        """
        Sets the timeFormat property value. The time format for the user's mailbox.
        Args:
            value: Value to set for the timeFormat property.
        """
        self._time_format = value
    
    @property
    def time_zone(self,) -> Optional[str]:
        """
        Gets the timeZone property value. The default time zone for the user's mailbox.
        Returns: Optional[str]
        """
        return self._time_zone
    
    @time_zone.setter
    def time_zone(self,value: Optional[str] = None) -> None:
        """
        Sets the timeZone property value. The default time zone for the user's mailbox.
        Args:
            value: Value to set for the timeZone property.
        """
        self._time_zone = value
    
    @property
    def user_purpose(self,) -> Optional[user_purpose.UserPurpose]:
        """
        Gets the userPurpose property value. The userPurpose property
        Returns: Optional[user_purpose.UserPurpose]
        """
        return self._user_purpose
    
    @user_purpose.setter
    def user_purpose(self,value: Optional[user_purpose.UserPurpose] = None) -> None:
        """
        Sets the userPurpose property value. The userPurpose property
        Args:
            value: Value to set for the userPurpose property.
        """
        self._user_purpose = value
    
    @property
    def working_hours(self,) -> Optional[working_hours.WorkingHours]:
        """
        Gets the workingHours property value. The days of the week and hours in a specific time zone that the user works.
        Returns: Optional[working_hours.WorkingHours]
        """
        return self._working_hours
    
    @working_hours.setter
    def working_hours(self,value: Optional[working_hours.WorkingHours] = None) -> None:
        """
        Sets the workingHours property value. The days of the week and hours in a specific time zone that the user works.
        Args:
            value: Value to set for the workingHours property.
        """
        self._working_hours = value
    

