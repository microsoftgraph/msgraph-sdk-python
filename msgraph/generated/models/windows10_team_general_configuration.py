from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_configuration import DeviceConfiguration
    from .miracast_channel import MiracastChannel
    from .welcome_screen_meeting_information import WelcomeScreenMeetingInformation

from .device_configuration import DeviceConfiguration

@dataclass
class Windows10TeamGeneralConfiguration(DeviceConfiguration):
    """
    This topic provides descriptions of the declared methods, properties and relationships exposed by the windows10TeamGeneralConfiguration resource.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windows10TeamGeneralConfiguration"
    # Indicates whether or not to Block Azure Operational Insights.
    azure_operational_insights_block_telemetry: Optional[bool] = None
    # The Azure Operational Insights workspace id.
    azure_operational_insights_workspace_id: Optional[str] = None
    # The Azure Operational Insights Workspace key.
    azure_operational_insights_workspace_key: Optional[str] = None
    # Specifies whether to automatically launch the Connect app whenever a projection is initiated.
    connect_app_block_auto_launch: Optional[bool] = None
    # Indicates whether or not to Block setting a maintenance window for device updates.
    maintenance_window_blocked: Optional[bool] = None
    # Maintenance window duration for device updates. Valid values 0 to 5
    maintenance_window_duration_in_hours: Optional[int] = None
    # Maintenance window start time for device updates.
    maintenance_window_start_time: Optional[datetime.time] = None
    # Indicates whether or not to Block wireless projection.
    miracast_blocked: Optional[bool] = None
    # Possible values for Miracast channel.
    miracast_channel: Optional[MiracastChannel] = None
    # Indicates whether or not to require a pin for wireless projection.
    miracast_require_pin: Optional[bool] = None
    # Specifies whether to disable the 'My meetings and files' feature in the Start menu, which shows the signed-in user's meetings and files from Office 365.
    settings_block_my_meetings_and_files: Optional[bool] = None
    # Specifies whether to allow the ability to resume a session when the session times out.
    settings_block_session_resume: Optional[bool] = None
    # Specifies whether to disable auto-populating of the sign-in dialog with invitees from scheduled meetings.
    settings_block_signin_suggestions: Optional[bool] = None
    # Specifies the default volume value for a new session. Permitted values are 0-100. The default is 45. Valid values 0 to 100
    settings_default_volume: Optional[int] = None
    # Specifies the number of minutes until the Hub screen turns off.
    settings_screen_timeout_in_minutes: Optional[int] = None
    # Specifies the number of minutes until the session times out.
    settings_session_timeout_in_minutes: Optional[int] = None
    # Specifies the number of minutes until the Hub enters sleep mode.
    settings_sleep_timeout_in_minutes: Optional[int] = None
    # The welcome screen background image URL. The URL must use the HTTPS protocol and return a PNG image.
    welcome_screen_background_image_url: Optional[str] = None
    # Indicates whether or not to Block the welcome screen from waking up automatically when someone enters the room.
    welcome_screen_block_automatic_wake_up: Optional[bool] = None
    # Possible values for welcome screen meeting information.
    welcome_screen_meeting_information: Optional[WelcomeScreenMeetingInformation] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Windows10TeamGeneralConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Windows10TeamGeneralConfiguration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Windows10TeamGeneralConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .device_configuration import DeviceConfiguration
        from .miracast_channel import MiracastChannel
        from .welcome_screen_meeting_information import WelcomeScreenMeetingInformation

        from .device_configuration import DeviceConfiguration
        from .miracast_channel import MiracastChannel
        from .welcome_screen_meeting_information import WelcomeScreenMeetingInformation

        fields: Dict[str, Callable[[Any], None]] = {
            "azure_operational_insights_block_telemetry": lambda n : setattr(self, 'azure_operational_insights_block_telemetry', n.get_bool_value()),
            "azure_operational_insights_workspace_id": lambda n : setattr(self, 'azure_operational_insights_workspace_id', n.get_str_value()),
            "azure_operational_insights_workspace_key": lambda n : setattr(self, 'azure_operational_insights_workspace_key', n.get_str_value()),
            "connect_app_block_auto_launch": lambda n : setattr(self, 'connect_app_block_auto_launch', n.get_bool_value()),
            "maintenance_window_blocked": lambda n : setattr(self, 'maintenance_window_blocked', n.get_bool_value()),
            "maintenance_window_duration_in_hours": lambda n : setattr(self, 'maintenance_window_duration_in_hours', n.get_int_value()),
            "maintenance_window_start_time": lambda n : setattr(self, 'maintenance_window_start_time', n.get_time_value()),
            "miracast_blocked": lambda n : setattr(self, 'miracast_blocked', n.get_bool_value()),
            "miracast_channel": lambda n : setattr(self, 'miracast_channel', n.get_enum_value(MiracastChannel)),
            "miracast_require_pin": lambda n : setattr(self, 'miracast_require_pin', n.get_bool_value()),
            "settings_block_my_meetings_and_files": lambda n : setattr(self, 'settings_block_my_meetings_and_files', n.get_bool_value()),
            "settings_block_session_resume": lambda n : setattr(self, 'settings_block_session_resume', n.get_bool_value()),
            "settings_block_signin_suggestions": lambda n : setattr(self, 'settings_block_signin_suggestions', n.get_bool_value()),
            "settings_default_volume": lambda n : setattr(self, 'settings_default_volume', n.get_int_value()),
            "settings_screen_timeout_in_minutes": lambda n : setattr(self, 'settings_screen_timeout_in_minutes', n.get_int_value()),
            "settings_session_timeout_in_minutes": lambda n : setattr(self, 'settings_session_timeout_in_minutes', n.get_int_value()),
            "settings_sleep_timeout_in_minutes": lambda n : setattr(self, 'settings_sleep_timeout_in_minutes', n.get_int_value()),
            "welcome_screen_background_image_url": lambda n : setattr(self, 'welcome_screen_background_image_url', n.get_str_value()),
            "welcome_screen_block_automatic_wake_up": lambda n : setattr(self, 'welcome_screen_block_automatic_wake_up', n.get_bool_value()),
            "welcome_screen_meeting_information": lambda n : setattr(self, 'welcome_screen_meeting_information', n.get_enum_value(WelcomeScreenMeetingInformation)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_bool_value("azure_operational_insights_block_telemetry", self.azure_operational_insights_block_telemetry)
        writer.write_str_value("azure_operational_insights_workspace_id", self.azure_operational_insights_workspace_id)
        writer.write_str_value("azure_operational_insights_workspace_key", self.azure_operational_insights_workspace_key)
        writer.write_bool_value("connect_app_block_auto_launch", self.connect_app_block_auto_launch)
        writer.write_bool_value("maintenance_window_blocked", self.maintenance_window_blocked)
        writer.write_int_value("maintenance_window_duration_in_hours", self.maintenance_window_duration_in_hours)
        writer.write_time_value("maintenance_window_start_time", self.maintenance_window_start_time)
        writer.write_bool_value("miracast_blocked", self.miracast_blocked)
        writer.write_enum_value("miracast_channel", self.miracast_channel)
        writer.write_bool_value("miracast_require_pin", self.miracast_require_pin)
        writer.write_bool_value("settings_block_my_meetings_and_files", self.settings_block_my_meetings_and_files)
        writer.write_bool_value("settings_block_session_resume", self.settings_block_session_resume)
        writer.write_bool_value("settings_block_signin_suggestions", self.settings_block_signin_suggestions)
        writer.write_int_value("settings_default_volume", self.settings_default_volume)
        writer.write_int_value("settings_screen_timeout_in_minutes", self.settings_screen_timeout_in_minutes)
        writer.write_int_value("settings_session_timeout_in_minutes", self.settings_session_timeout_in_minutes)
        writer.write_int_value("settings_sleep_timeout_in_minutes", self.settings_sleep_timeout_in_minutes)
        writer.write_str_value("welcome_screen_background_image_url", self.welcome_screen_background_image_url)
        writer.write_bool_value("welcome_screen_block_automatic_wake_up", self.welcome_screen_block_automatic_wake_up)
        writer.write_enum_value("welcome_screen_meeting_information", self.welcome_screen_meeting_information)
    

