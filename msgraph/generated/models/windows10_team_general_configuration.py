from __future__ import annotations
from datetime import time
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_configuration = lazy_import('msgraph.generated.models.device_configuration')
miracast_channel = lazy_import('msgraph.generated.models.miracast_channel')
welcome_screen_meeting_information = lazy_import('msgraph.generated.models.welcome_screen_meeting_information')

class Windows10TeamGeneralConfiguration(device_configuration.DeviceConfiguration):
    @property
    def azure_operational_insights_block_telemetry(self,) -> Optional[bool]:
        """
        Gets the azureOperationalInsightsBlockTelemetry property value. Indicates whether or not to Block Azure Operational Insights.
        Returns: Optional[bool]
        """
        return self._azure_operational_insights_block_telemetry
    
    @azure_operational_insights_block_telemetry.setter
    def azure_operational_insights_block_telemetry(self,value: Optional[bool] = None) -> None:
        """
        Sets the azureOperationalInsightsBlockTelemetry property value. Indicates whether or not to Block Azure Operational Insights.
        Args:
            value: Value to set for the azureOperationalInsightsBlockTelemetry property.
        """
        self._azure_operational_insights_block_telemetry = value
    
    @property
    def azure_operational_insights_workspace_id(self,) -> Optional[str]:
        """
        Gets the azureOperationalInsightsWorkspaceId property value. The Azure Operational Insights workspace id.
        Returns: Optional[str]
        """
        return self._azure_operational_insights_workspace_id
    
    @azure_operational_insights_workspace_id.setter
    def azure_operational_insights_workspace_id(self,value: Optional[str] = None) -> None:
        """
        Sets the azureOperationalInsightsWorkspaceId property value. The Azure Operational Insights workspace id.
        Args:
            value: Value to set for the azureOperationalInsightsWorkspaceId property.
        """
        self._azure_operational_insights_workspace_id = value
    
    @property
    def azure_operational_insights_workspace_key(self,) -> Optional[str]:
        """
        Gets the azureOperationalInsightsWorkspaceKey property value. The Azure Operational Insights Workspace key.
        Returns: Optional[str]
        """
        return self._azure_operational_insights_workspace_key
    
    @azure_operational_insights_workspace_key.setter
    def azure_operational_insights_workspace_key(self,value: Optional[str] = None) -> None:
        """
        Sets the azureOperationalInsightsWorkspaceKey property value. The Azure Operational Insights Workspace key.
        Args:
            value: Value to set for the azureOperationalInsightsWorkspaceKey property.
        """
        self._azure_operational_insights_workspace_key = value
    
    @property
    def connect_app_block_auto_launch(self,) -> Optional[bool]:
        """
        Gets the connectAppBlockAutoLaunch property value. Specifies whether to automatically launch the Connect app whenever a projection is initiated.
        Returns: Optional[bool]
        """
        return self._connect_app_block_auto_launch
    
    @connect_app_block_auto_launch.setter
    def connect_app_block_auto_launch(self,value: Optional[bool] = None) -> None:
        """
        Sets the connectAppBlockAutoLaunch property value. Specifies whether to automatically launch the Connect app whenever a projection is initiated.
        Args:
            value: Value to set for the connectAppBlockAutoLaunch property.
        """
        self._connect_app_block_auto_launch = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new Windows10TeamGeneralConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windows10TeamGeneralConfiguration"
        # Indicates whether or not to Block Azure Operational Insights.
        self._azure_operational_insights_block_telemetry: Optional[bool] = None
        # The Azure Operational Insights workspace id.
        self._azure_operational_insights_workspace_id: Optional[str] = None
        # The Azure Operational Insights Workspace key.
        self._azure_operational_insights_workspace_key: Optional[str] = None
        # Specifies whether to automatically launch the Connect app whenever a projection is initiated.
        self._connect_app_block_auto_launch: Optional[bool] = None
        # Indicates whether or not to Block setting a maintenance window for device updates.
        self._maintenance_window_blocked: Optional[bool] = None
        # Maintenance window duration for device updates. Valid values 0 to 5
        self._maintenance_window_duration_in_hours: Optional[int] = None
        # Maintenance window start time for device updates.
        self._maintenance_window_start_time: Optional[Time] = None
        # Indicates whether or not to Block wireless projection.
        self._miracast_blocked: Optional[bool] = None
        # Possible values for Miracast channel.
        self._miracast_channel: Optional[miracast_channel.MiracastChannel] = None
        # Indicates whether or not to require a pin for wireless projection.
        self._miracast_require_pin: Optional[bool] = None
        # Specifies whether to disable the 'My meetings and files' feature in the Start menu, which shows the signed-in user's meetings and files from Office 365.
        self._settings_block_my_meetings_and_files: Optional[bool] = None
        # Specifies whether to allow the ability to resume a session when the session times out.
        self._settings_block_session_resume: Optional[bool] = None
        # Specifies whether to disable auto-populating of the sign-in dialog with invitees from scheduled meetings.
        self._settings_block_signin_suggestions: Optional[bool] = None
        # Specifies the default volume value for a new session. Permitted values are 0-100. The default is 45. Valid values 0 to 100
        self._settings_default_volume: Optional[int] = None
        # Specifies the number of minutes until the Hub screen turns off.
        self._settings_screen_timeout_in_minutes: Optional[int] = None
        # Specifies the number of minutes until the session times out.
        self._settings_session_timeout_in_minutes: Optional[int] = None
        # Specifies the number of minutes until the Hub enters sleep mode.
        self._settings_sleep_timeout_in_minutes: Optional[int] = None
        # The welcome screen background image URL. The URL must use the HTTPS protocol and return a PNG image.
        self._welcome_screen_background_image_url: Optional[str] = None
        # Indicates whether or not to Block the welcome screen from waking up automatically when someone enters the room.
        self._welcome_screen_block_automatic_wake_up: Optional[bool] = None
        # Possible values for welcome screen meeting information.
        self._welcome_screen_meeting_information: Optional[welcome_screen_meeting_information.WelcomeScreenMeetingInformation] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Windows10TeamGeneralConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Windows10TeamGeneralConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Windows10TeamGeneralConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "azure_operational_insights_block_telemetry": lambda n : setattr(self, 'azure_operational_insights_block_telemetry', n.get_bool_value()),
            "azure_operational_insights_workspace_id": lambda n : setattr(self, 'azure_operational_insights_workspace_id', n.get_str_value()),
            "azure_operational_insights_workspace_key": lambda n : setattr(self, 'azure_operational_insights_workspace_key', n.get_str_value()),
            "connect_app_block_auto_launch": lambda n : setattr(self, 'connect_app_block_auto_launch', n.get_bool_value()),
            "maintenance_window_blocked": lambda n : setattr(self, 'maintenance_window_blocked', n.get_bool_value()),
            "maintenance_window_duration_in_hours": lambda n : setattr(self, 'maintenance_window_duration_in_hours', n.get_int_value()),
            "maintenance_window_start_time": lambda n : setattr(self, 'maintenance_window_start_time', n.get_object_value(Time)),
            "miracast_blocked": lambda n : setattr(self, 'miracast_blocked', n.get_bool_value()),
            "miracast_channel": lambda n : setattr(self, 'miracast_channel', n.get_enum_value(miracast_channel.MiracastChannel)),
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
            "welcome_screen_meeting_information": lambda n : setattr(self, 'welcome_screen_meeting_information', n.get_enum_value(welcome_screen_meeting_information.WelcomeScreenMeetingInformation)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def maintenance_window_blocked(self,) -> Optional[bool]:
        """
        Gets the maintenanceWindowBlocked property value. Indicates whether or not to Block setting a maintenance window for device updates.
        Returns: Optional[bool]
        """
        return self._maintenance_window_blocked
    
    @maintenance_window_blocked.setter
    def maintenance_window_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the maintenanceWindowBlocked property value. Indicates whether or not to Block setting a maintenance window for device updates.
        Args:
            value: Value to set for the maintenanceWindowBlocked property.
        """
        self._maintenance_window_blocked = value
    
    @property
    def maintenance_window_duration_in_hours(self,) -> Optional[int]:
        """
        Gets the maintenanceWindowDurationInHours property value. Maintenance window duration for device updates. Valid values 0 to 5
        Returns: Optional[int]
        """
        return self._maintenance_window_duration_in_hours
    
    @maintenance_window_duration_in_hours.setter
    def maintenance_window_duration_in_hours(self,value: Optional[int] = None) -> None:
        """
        Sets the maintenanceWindowDurationInHours property value. Maintenance window duration for device updates. Valid values 0 to 5
        Args:
            value: Value to set for the maintenanceWindowDurationInHours property.
        """
        self._maintenance_window_duration_in_hours = value
    
    @property
    def maintenance_window_start_time(self,) -> Optional[Time]:
        """
        Gets the maintenanceWindowStartTime property value. Maintenance window start time for device updates.
        Returns: Optional[Time]
        """
        return self._maintenance_window_start_time
    
    @maintenance_window_start_time.setter
    def maintenance_window_start_time(self,value: Optional[Time] = None) -> None:
        """
        Sets the maintenanceWindowStartTime property value. Maintenance window start time for device updates.
        Args:
            value: Value to set for the maintenanceWindowStartTime property.
        """
        self._maintenance_window_start_time = value
    
    @property
    def miracast_blocked(self,) -> Optional[bool]:
        """
        Gets the miracastBlocked property value. Indicates whether or not to Block wireless projection.
        Returns: Optional[bool]
        """
        return self._miracast_blocked
    
    @miracast_blocked.setter
    def miracast_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the miracastBlocked property value. Indicates whether or not to Block wireless projection.
        Args:
            value: Value to set for the miracastBlocked property.
        """
        self._miracast_blocked = value
    
    @property
    def miracast_channel(self,) -> Optional[miracast_channel.MiracastChannel]:
        """
        Gets the miracastChannel property value. Possible values for Miracast channel.
        Returns: Optional[miracast_channel.MiracastChannel]
        """
        return self._miracast_channel
    
    @miracast_channel.setter
    def miracast_channel(self,value: Optional[miracast_channel.MiracastChannel] = None) -> None:
        """
        Sets the miracastChannel property value. Possible values for Miracast channel.
        Args:
            value: Value to set for the miracastChannel property.
        """
        self._miracast_channel = value
    
    @property
    def miracast_require_pin(self,) -> Optional[bool]:
        """
        Gets the miracastRequirePin property value. Indicates whether or not to require a pin for wireless projection.
        Returns: Optional[bool]
        """
        return self._miracast_require_pin
    
    @miracast_require_pin.setter
    def miracast_require_pin(self,value: Optional[bool] = None) -> None:
        """
        Sets the miracastRequirePin property value. Indicates whether or not to require a pin for wireless projection.
        Args:
            value: Value to set for the miracastRequirePin property.
        """
        self._miracast_require_pin = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("azureOperationalInsightsBlockTelemetry", self.azure_operational_insights_block_telemetry)
        writer.write_str_value("azureOperationalInsightsWorkspaceId", self.azure_operational_insights_workspace_id)
        writer.write_str_value("azureOperationalInsightsWorkspaceKey", self.azure_operational_insights_workspace_key)
        writer.write_bool_value("connectAppBlockAutoLaunch", self.connect_app_block_auto_launch)
        writer.write_bool_value("maintenanceWindowBlocked", self.maintenance_window_blocked)
        writer.write_int_value("maintenanceWindowDurationInHours", self.maintenance_window_duration_in_hours)
        writer.write_object_value("maintenanceWindowStartTime", self.maintenance_window_start_time)
        writer.write_bool_value("miracastBlocked", self.miracast_blocked)
        writer.write_enum_value("miracastChannel", self.miracast_channel)
        writer.write_bool_value("miracastRequirePin", self.miracast_require_pin)
        writer.write_bool_value("settingsBlockMyMeetingsAndFiles", self.settings_block_my_meetings_and_files)
        writer.write_bool_value("settingsBlockSessionResume", self.settings_block_session_resume)
        writer.write_bool_value("settingsBlockSigninSuggestions", self.settings_block_signin_suggestions)
        writer.write_int_value("settingsDefaultVolume", self.settings_default_volume)
        writer.write_int_value("settingsScreenTimeoutInMinutes", self.settings_screen_timeout_in_minutes)
        writer.write_int_value("settingsSessionTimeoutInMinutes", self.settings_session_timeout_in_minutes)
        writer.write_int_value("settingsSleepTimeoutInMinutes", self.settings_sleep_timeout_in_minutes)
        writer.write_str_value("welcomeScreenBackgroundImageUrl", self.welcome_screen_background_image_url)
        writer.write_bool_value("welcomeScreenBlockAutomaticWakeUp", self.welcome_screen_block_automatic_wake_up)
        writer.write_enum_value("welcomeScreenMeetingInformation", self.welcome_screen_meeting_information)
    
    @property
    def settings_block_my_meetings_and_files(self,) -> Optional[bool]:
        """
        Gets the settingsBlockMyMeetingsAndFiles property value. Specifies whether to disable the 'My meetings and files' feature in the Start menu, which shows the signed-in user's meetings and files from Office 365.
        Returns: Optional[bool]
        """
        return self._settings_block_my_meetings_and_files
    
    @settings_block_my_meetings_and_files.setter
    def settings_block_my_meetings_and_files(self,value: Optional[bool] = None) -> None:
        """
        Sets the settingsBlockMyMeetingsAndFiles property value. Specifies whether to disable the 'My meetings and files' feature in the Start menu, which shows the signed-in user's meetings and files from Office 365.
        Args:
            value: Value to set for the settingsBlockMyMeetingsAndFiles property.
        """
        self._settings_block_my_meetings_and_files = value
    
    @property
    def settings_block_session_resume(self,) -> Optional[bool]:
        """
        Gets the settingsBlockSessionResume property value. Specifies whether to allow the ability to resume a session when the session times out.
        Returns: Optional[bool]
        """
        return self._settings_block_session_resume
    
    @settings_block_session_resume.setter
    def settings_block_session_resume(self,value: Optional[bool] = None) -> None:
        """
        Sets the settingsBlockSessionResume property value. Specifies whether to allow the ability to resume a session when the session times out.
        Args:
            value: Value to set for the settingsBlockSessionResume property.
        """
        self._settings_block_session_resume = value
    
    @property
    def settings_block_signin_suggestions(self,) -> Optional[bool]:
        """
        Gets the settingsBlockSigninSuggestions property value. Specifies whether to disable auto-populating of the sign-in dialog with invitees from scheduled meetings.
        Returns: Optional[bool]
        """
        return self._settings_block_signin_suggestions
    
    @settings_block_signin_suggestions.setter
    def settings_block_signin_suggestions(self,value: Optional[bool] = None) -> None:
        """
        Sets the settingsBlockSigninSuggestions property value. Specifies whether to disable auto-populating of the sign-in dialog with invitees from scheduled meetings.
        Args:
            value: Value to set for the settingsBlockSigninSuggestions property.
        """
        self._settings_block_signin_suggestions = value
    
    @property
    def settings_default_volume(self,) -> Optional[int]:
        """
        Gets the settingsDefaultVolume property value. Specifies the default volume value for a new session. Permitted values are 0-100. The default is 45. Valid values 0 to 100
        Returns: Optional[int]
        """
        return self._settings_default_volume
    
    @settings_default_volume.setter
    def settings_default_volume(self,value: Optional[int] = None) -> None:
        """
        Sets the settingsDefaultVolume property value. Specifies the default volume value for a new session. Permitted values are 0-100. The default is 45. Valid values 0 to 100
        Args:
            value: Value to set for the settingsDefaultVolume property.
        """
        self._settings_default_volume = value
    
    @property
    def settings_screen_timeout_in_minutes(self,) -> Optional[int]:
        """
        Gets the settingsScreenTimeoutInMinutes property value. Specifies the number of minutes until the Hub screen turns off.
        Returns: Optional[int]
        """
        return self._settings_screen_timeout_in_minutes
    
    @settings_screen_timeout_in_minutes.setter
    def settings_screen_timeout_in_minutes(self,value: Optional[int] = None) -> None:
        """
        Sets the settingsScreenTimeoutInMinutes property value. Specifies the number of minutes until the Hub screen turns off.
        Args:
            value: Value to set for the settingsScreenTimeoutInMinutes property.
        """
        self._settings_screen_timeout_in_minutes = value
    
    @property
    def settings_session_timeout_in_minutes(self,) -> Optional[int]:
        """
        Gets the settingsSessionTimeoutInMinutes property value. Specifies the number of minutes until the session times out.
        Returns: Optional[int]
        """
        return self._settings_session_timeout_in_minutes
    
    @settings_session_timeout_in_minutes.setter
    def settings_session_timeout_in_minutes(self,value: Optional[int] = None) -> None:
        """
        Sets the settingsSessionTimeoutInMinutes property value. Specifies the number of minutes until the session times out.
        Args:
            value: Value to set for the settingsSessionTimeoutInMinutes property.
        """
        self._settings_session_timeout_in_minutes = value
    
    @property
    def settings_sleep_timeout_in_minutes(self,) -> Optional[int]:
        """
        Gets the settingsSleepTimeoutInMinutes property value. Specifies the number of minutes until the Hub enters sleep mode.
        Returns: Optional[int]
        """
        return self._settings_sleep_timeout_in_minutes
    
    @settings_sleep_timeout_in_minutes.setter
    def settings_sleep_timeout_in_minutes(self,value: Optional[int] = None) -> None:
        """
        Sets the settingsSleepTimeoutInMinutes property value. Specifies the number of minutes until the Hub enters sleep mode.
        Args:
            value: Value to set for the settingsSleepTimeoutInMinutes property.
        """
        self._settings_sleep_timeout_in_minutes = value
    
    @property
    def welcome_screen_background_image_url(self,) -> Optional[str]:
        """
        Gets the welcomeScreenBackgroundImageUrl property value. The welcome screen background image URL. The URL must use the HTTPS protocol and return a PNG image.
        Returns: Optional[str]
        """
        return self._welcome_screen_background_image_url
    
    @welcome_screen_background_image_url.setter
    def welcome_screen_background_image_url(self,value: Optional[str] = None) -> None:
        """
        Sets the welcomeScreenBackgroundImageUrl property value. The welcome screen background image URL. The URL must use the HTTPS protocol and return a PNG image.
        Args:
            value: Value to set for the welcomeScreenBackgroundImageUrl property.
        """
        self._welcome_screen_background_image_url = value
    
    @property
    def welcome_screen_block_automatic_wake_up(self,) -> Optional[bool]:
        """
        Gets the welcomeScreenBlockAutomaticWakeUp property value. Indicates whether or not to Block the welcome screen from waking up automatically when someone enters the room.
        Returns: Optional[bool]
        """
        return self._welcome_screen_block_automatic_wake_up
    
    @welcome_screen_block_automatic_wake_up.setter
    def welcome_screen_block_automatic_wake_up(self,value: Optional[bool] = None) -> None:
        """
        Sets the welcomeScreenBlockAutomaticWakeUp property value. Indicates whether or not to Block the welcome screen from waking up automatically when someone enters the room.
        Args:
            value: Value to set for the welcomeScreenBlockAutomaticWakeUp property.
        """
        self._welcome_screen_block_automatic_wake_up = value
    
    @property
    def welcome_screen_meeting_information(self,) -> Optional[welcome_screen_meeting_information.WelcomeScreenMeetingInformation]:
        """
        Gets the welcomeScreenMeetingInformation property value. Possible values for welcome screen meeting information.
        Returns: Optional[welcome_screen_meeting_information.WelcomeScreenMeetingInformation]
        """
        return self._welcome_screen_meeting_information
    
    @welcome_screen_meeting_information.setter
    def welcome_screen_meeting_information(self,value: Optional[welcome_screen_meeting_information.WelcomeScreenMeetingInformation] = None) -> None:
        """
        Sets the welcomeScreenMeetingInformation property value. Possible values for welcome screen meeting information.
        Args:
            value: Value to set for the welcomeScreenMeetingInformation property.
        """
        self._welcome_screen_meeting_information = value
    

