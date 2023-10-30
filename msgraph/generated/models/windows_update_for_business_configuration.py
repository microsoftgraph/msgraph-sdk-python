from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .automatic_update_mode import AutomaticUpdateMode
    from .auto_restart_notification_dismissal_method import AutoRestartNotificationDismissalMethod
    from .device_configuration import DeviceConfiguration
    from .enablement import Enablement
    from .prerelease_features import PrereleaseFeatures
    from .windows_delivery_optimization_mode import WindowsDeliveryOptimizationMode
    from .windows_update_for_business_update_weeks import WindowsUpdateForBusinessUpdateWeeks
    from .windows_update_install_schedule_type import WindowsUpdateInstallScheduleType
    from .windows_update_notification_display_option import WindowsUpdateNotificationDisplayOption
    from .windows_update_type import WindowsUpdateType

from .device_configuration import DeviceConfiguration

@dataclass
class WindowsUpdateForBusinessConfiguration(DeviceConfiguration):
    """
    Windows Update for business configuration, allows you to specify how and when Windows as a Service updates your Windows 10/11 devices with feature and quality updates. Supports ODATA clauses that DeviceConfiguration entity supports: $filter by types of DeviceConfiguration, $top, $select only DeviceConfiguration base properties, $orderby only DeviceConfiguration base properties, and $skip. The query parameter '$search' is not supported.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windowsUpdateForBusinessConfiguration"
    # When TRUE, allows eligible Windows 10 devices to upgrade to Windows 11. When FALSE, implies the device stays on the existing operating system. Returned by default. Query parameters are not supported.
    allow_windows11_upgrade: Optional[bool] = None
    # Auto restart required notification dismissal method
    auto_restart_notification_dismissal: Optional[AutoRestartNotificationDismissalMethod] = None
    # Possible values for automatic update mode.
    automatic_update_mode: Optional[AutomaticUpdateMode] = None
    # Which branch devices will receive their updates from
    business_ready_updates_only: Optional[WindowsUpdateType] = None
    # Number of days before feature updates are installed automatically with valid range from 0 to 30 days. Returned by default. Query parameters are not supported.
    deadline_for_feature_updates_in_days: Optional[int] = None
    # Number of days before quality updates are installed automatically with valid range from 0 to 30 days. Returned by default. Query parameters are not supported.
    deadline_for_quality_updates_in_days: Optional[int] = None
    # Number of days after deadline until restarts occur automatically with valid range from 0 to 7 days. Returned by default. Query parameters are not supported.
    deadline_grace_period_in_days: Optional[int] = None
    # Delivery optimization mode for peer distribution
    delivery_optimization_mode: Optional[WindowsDeliveryOptimizationMode] = None
    # When TRUE, excludes Windows update Drivers. When FALSE, does not exclude Windows update Drivers. Returned by default. Query parameters are not supported.
    drivers_excluded: Optional[bool] = None
    # Deadline in days before automatically scheduling and executing a pending restart outside of active hours, with valid range from 2 to 30 days. Returned by default. Query parameters are not supported.
    engaged_restart_deadline_in_days: Optional[int] = None
    # Number of days a user can snooze Engaged Restart reminder notifications with valid range from 1 to 3 days. Returned by default. Query parameters are not supported.
    engaged_restart_snooze_schedule_in_days: Optional[int] = None
    # Number of days before transitioning from Auto Restarts scheduled outside of active hours to Engaged Restart, which requires the user to schedule, with valid range from 0 to 30 days. Returned by default. Query parameters are not supported.
    engaged_restart_transition_schedule_in_days: Optional[int] = None
    # Defer Feature Updates by these many days with valid range from 0 to 30 days. Returned by default. Query parameters are not supported.
    feature_updates_deferral_period_in_days: Optional[int] = None
    # The Feature Updates Pause Expiry datetime. This value is 35 days from the time admin paused or extended the pause for the ring. Returned by default. Query parameters are not supported.
    feature_updates_pause_expiry_date_time: Optional[datetime.datetime] = None
    # The Feature Updates Pause start date. This value is the time when the admin paused or extended the pause for the ring. Returned by default. Query parameters are not supported. This property is read-only.
    feature_updates_pause_start_date: Optional[datetime.date] = None
    # When TRUE, assigned devices are paused from receiving feature updates for up to 35 days from the time you pause the ring. When FALSE, does not pause Feature Updates. Returned by default. Query parameters are not supported.s
    feature_updates_paused: Optional[bool] = None
    # The Feature Updates Rollback Start datetime.This value is the time when the admin rolled back the Feature update for the ring.Returned by default.Query parameters are not supported.
    feature_updates_rollback_start_date_time: Optional[datetime.datetime] = None
    # The number of days after a Feature Update for which a rollback is valid with valid range from 2 to 60 days. Returned by default. Query parameters are not supported.
    feature_updates_rollback_window_in_days: Optional[int] = None
    # When TRUE, rollback Feature Updates on the next device check in. When FALSE, do not rollback Feature Updates on the next device check in. Returned by default.Query parameters are not supported.
    feature_updates_will_be_rolled_back: Optional[bool] = None
    # The Installation Schedule. Possible values are: ActiveHoursStart, ActiveHoursEnd, ScheduledInstallDay, ScheduledInstallTime. Returned by default. Query parameters are not supported.
    installation_schedule: Optional[WindowsUpdateInstallScheduleType] = None
    # When TRUE, allows Microsoft Update Service. When FALSE, does not allow Microsoft Update Service. Returned by default. Query parameters are not supported.
    microsoft_update_service_allowed: Optional[bool] = None
    # When TRUE the device should wait until deadline for rebooting outside of active hours. When FALSE the device should not wait until deadline for rebooting outside of active hours. Returned by default. Query parameters are not supported.
    postpone_reboot_until_after_deadline: Optional[bool] = None
    # Possible values for pre-release features.
    prerelease_features: Optional[PrereleaseFeatures] = None
    # Defer Quality Updates by these many days with valid range from 0 to 30 days. Returned by default. Query parameters are not supported.
    quality_updates_deferral_period_in_days: Optional[int] = None
    # The Quality Updates Pause Expiry datetime. This value is 35 days from the time admin paused or extended the pause for the ring. Returned by default. Query parameters are not supported.
    quality_updates_pause_expiry_date_time: Optional[datetime.datetime] = None
    # The Quality Updates Pause start date. This value is the time when the admin paused or extended the pause for the ring. Returned by default. Query parameters are not supported. This property is read-only.
    quality_updates_pause_start_date: Optional[datetime.date] = None
    # When TRUE, assigned devices are paused from receiving quality updates for up to 35 days from the time you pause the ring. When FALSE, does not pause Quality Updates. Returned by default. Query parameters are not supported.
    quality_updates_paused: Optional[bool] = None
    # The Quality Updates Rollback Start datetime. This value is the time when the admin rolled back the Quality update for the ring. Returned by default. Query parameters are not supported.
    quality_updates_rollback_start_date_time: Optional[datetime.datetime] = None
    # When TRUE, rollback Quality Updates on the next device check in. When FALSE, do not rollback Quality Updates on the next device check in. Returned by default. Query parameters are not supported.
    quality_updates_will_be_rolled_back: Optional[bool] = None
    # Specify the period for auto-restart imminent warning notifications. Supported values: 15, 30 or 60 (minutes). Returned by default. Query parameters are not supported.
    schedule_imminent_restart_warning_in_minutes: Optional[int] = None
    # Specify the period for auto-restart warning reminder notifications. Supported values: 2, 4, 8, 12 or 24 (hours). Returned by default. Query parameters are not supported.
    schedule_restart_warning_in_hours: Optional[int] = None
    # When TRUE, skips all checks before restart: Battery level = 40%, User presence, Display Needed, Presentation mode, Full screen mode, phone call state, game mode etc. When FALSE, does not skip all checks before restart. Returned by default. Query parameters are not supported.
    skip_checks_before_restart: Optional[bool] = None
    # Windows Update Notification Display Options
    update_notification_level: Optional[WindowsUpdateNotificationDisplayOption] = None
    # Schedule the update installation on the weeks of the month. Possible values are: UserDefined, FirstWeek, SecondWeek, ThirdWeek, FourthWeek, EveryWeek. Returned by default. Query parameters are not supported. Possible values are: userDefined, firstWeek, secondWeek, thirdWeek, fourthWeek, everyWeek, unknownFutureValue.
    update_weeks: Optional[WindowsUpdateForBusinessUpdateWeeks] = None
    # Possible values of a property
    user_pause_access: Optional[Enablement] = None
    # Possible values of a property
    user_windows_update_scan_access: Optional[Enablement] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsUpdateForBusinessConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsUpdateForBusinessConfiguration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return WindowsUpdateForBusinessConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .automatic_update_mode import AutomaticUpdateMode
        from .auto_restart_notification_dismissal_method import AutoRestartNotificationDismissalMethod
        from .device_configuration import DeviceConfiguration
        from .enablement import Enablement
        from .prerelease_features import PrereleaseFeatures
        from .windows_delivery_optimization_mode import WindowsDeliveryOptimizationMode
        from .windows_update_for_business_update_weeks import WindowsUpdateForBusinessUpdateWeeks
        from .windows_update_install_schedule_type import WindowsUpdateInstallScheduleType
        from .windows_update_notification_display_option import WindowsUpdateNotificationDisplayOption
        from .windows_update_type import WindowsUpdateType

        from .automatic_update_mode import AutomaticUpdateMode
        from .auto_restart_notification_dismissal_method import AutoRestartNotificationDismissalMethod
        from .device_configuration import DeviceConfiguration
        from .enablement import Enablement
        from .prerelease_features import PrereleaseFeatures
        from .windows_delivery_optimization_mode import WindowsDeliveryOptimizationMode
        from .windows_update_for_business_update_weeks import WindowsUpdateForBusinessUpdateWeeks
        from .windows_update_install_schedule_type import WindowsUpdateInstallScheduleType
        from .windows_update_notification_display_option import WindowsUpdateNotificationDisplayOption
        from .windows_update_type import WindowsUpdateType

        fields: Dict[str, Callable[[Any], None]] = {
            "allow_windows11_upgrade": lambda n : setattr(self, 'allow_windows11_upgrade', n.get_bool_value()),
            "auto_restart_notification_dismissal": lambda n : setattr(self, 'auto_restart_notification_dismissal', n.get_enum_value(AutoRestartNotificationDismissalMethod)),
            "automatic_update_mode": lambda n : setattr(self, 'automatic_update_mode', n.get_enum_value(AutomaticUpdateMode)),
            "business_ready_updates_only": lambda n : setattr(self, 'business_ready_updates_only', n.get_enum_value(WindowsUpdateType)),
            "deadline_for_feature_updates_in_days": lambda n : setattr(self, 'deadline_for_feature_updates_in_days', n.get_int_value()),
            "deadline_for_quality_updates_in_days": lambda n : setattr(self, 'deadline_for_quality_updates_in_days', n.get_int_value()),
            "deadline_grace_period_in_days": lambda n : setattr(self, 'deadline_grace_period_in_days', n.get_int_value()),
            "delivery_optimization_mode": lambda n : setattr(self, 'delivery_optimization_mode', n.get_enum_value(WindowsDeliveryOptimizationMode)),
            "drivers_excluded": lambda n : setattr(self, 'drivers_excluded', n.get_bool_value()),
            "engaged_restart_deadline_in_days": lambda n : setattr(self, 'engaged_restart_deadline_in_days', n.get_int_value()),
            "engaged_restart_snooze_schedule_in_days": lambda n : setattr(self, 'engaged_restart_snooze_schedule_in_days', n.get_int_value()),
            "engaged_restart_transition_schedule_in_days": lambda n : setattr(self, 'engaged_restart_transition_schedule_in_days', n.get_int_value()),
            "feature_updates_deferral_period_in_days": lambda n : setattr(self, 'feature_updates_deferral_period_in_days', n.get_int_value()),
            "feature_updates_pause_expiry_date_time": lambda n : setattr(self, 'feature_updates_pause_expiry_date_time', n.get_datetime_value()),
            "feature_updates_pause_start_date": lambda n : setattr(self, 'feature_updates_pause_start_date', n.get_date_value()),
            "feature_updates_paused": lambda n : setattr(self, 'feature_updates_paused', n.get_bool_value()),
            "feature_updates_rollback_start_date_time": lambda n : setattr(self, 'feature_updates_rollback_start_date_time', n.get_datetime_value()),
            "feature_updates_rollback_window_in_days": lambda n : setattr(self, 'feature_updates_rollback_window_in_days', n.get_int_value()),
            "feature_updates_will_be_rolled_back": lambda n : setattr(self, 'feature_updates_will_be_rolled_back', n.get_bool_value()),
            "installation_schedule": lambda n : setattr(self, 'installation_schedule', n.get_object_value(WindowsUpdateInstallScheduleType)),
            "microsoft_update_service_allowed": lambda n : setattr(self, 'microsoft_update_service_allowed', n.get_bool_value()),
            "postpone_reboot_until_after_deadline": lambda n : setattr(self, 'postpone_reboot_until_after_deadline', n.get_bool_value()),
            "prerelease_features": lambda n : setattr(self, 'prerelease_features', n.get_enum_value(PrereleaseFeatures)),
            "quality_updates_deferral_period_in_days": lambda n : setattr(self, 'quality_updates_deferral_period_in_days', n.get_int_value()),
            "quality_updates_pause_expiry_date_time": lambda n : setattr(self, 'quality_updates_pause_expiry_date_time', n.get_datetime_value()),
            "quality_updates_pause_start_date": lambda n : setattr(self, 'quality_updates_pause_start_date', n.get_date_value()),
            "quality_updates_paused": lambda n : setattr(self, 'quality_updates_paused', n.get_bool_value()),
            "quality_updates_rollback_start_date_time": lambda n : setattr(self, 'quality_updates_rollback_start_date_time', n.get_datetime_value()),
            "quality_updates_will_be_rolled_back": lambda n : setattr(self, 'quality_updates_will_be_rolled_back', n.get_bool_value()),
            "schedule_imminent_restart_warning_in_minutes": lambda n : setattr(self, 'schedule_imminent_restart_warning_in_minutes', n.get_int_value()),
            "schedule_restart_warning_in_hours": lambda n : setattr(self, 'schedule_restart_warning_in_hours', n.get_int_value()),
            "skip_checks_before_restart": lambda n : setattr(self, 'skip_checks_before_restart', n.get_bool_value()),
            "update_notification_level": lambda n : setattr(self, 'update_notification_level', n.get_enum_value(WindowsUpdateNotificationDisplayOption)),
            "update_weeks": lambda n : setattr(self, 'update_weeks', n.get_collection_of_enum_values(WindowsUpdateForBusinessUpdateWeeks)),
            "user_pause_access": lambda n : setattr(self, 'user_pause_access', n.get_enum_value(Enablement)),
            "user_windows_update_scan_access": lambda n : setattr(self, 'user_windows_update_scan_access', n.get_enum_value(Enablement)),
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
        writer.write_bool_value("allow_windows11_upgrade", self.allow_windows11_upgrade)
        writer.write_enum_value("auto_restart_notification_dismissal", self.auto_restart_notification_dismissal)
        writer.write_enum_value("automatic_update_mode", self.automatic_update_mode)
        writer.write_enum_value("business_ready_updates_only", self.business_ready_updates_only)
        writer.write_int_value("deadline_for_feature_updates_in_days", self.deadline_for_feature_updates_in_days)
        writer.write_int_value("deadline_for_quality_updates_in_days", self.deadline_for_quality_updates_in_days)
        writer.write_int_value("deadline_grace_period_in_days", self.deadline_grace_period_in_days)
        writer.write_enum_value("delivery_optimization_mode", self.delivery_optimization_mode)
        writer.write_bool_value("drivers_excluded", self.drivers_excluded)
        writer.write_int_value("engaged_restart_deadline_in_days", self.engaged_restart_deadline_in_days)
        writer.write_int_value("engaged_restart_snooze_schedule_in_days", self.engaged_restart_snooze_schedule_in_days)
        writer.write_int_value("engaged_restart_transition_schedule_in_days", self.engaged_restart_transition_schedule_in_days)
        writer.write_int_value("feature_updates_deferral_period_in_days", self.feature_updates_deferral_period_in_days)
        writer.write_datetime_value("feature_updates_pause_expiry_date_time", self.feature_updates_pause_expiry_date_time)
        writer.write_bool_value("feature_updates_paused", self.feature_updates_paused)
        writer.write_datetime_value("feature_updates_rollback_start_date_time", self.feature_updates_rollback_start_date_time)
        writer.write_int_value("feature_updates_rollback_window_in_days", self.feature_updates_rollback_window_in_days)
        writer.write_bool_value("feature_updates_will_be_rolled_back", self.feature_updates_will_be_rolled_back)
        writer.write_object_value("installation_schedule", self.installation_schedule)
        writer.write_bool_value("microsoft_update_service_allowed", self.microsoft_update_service_allowed)
        writer.write_bool_value("postpone_reboot_until_after_deadline", self.postpone_reboot_until_after_deadline)
        writer.write_enum_value("prerelease_features", self.prerelease_features)
        writer.write_int_value("quality_updates_deferral_period_in_days", self.quality_updates_deferral_period_in_days)
        writer.write_datetime_value("quality_updates_pause_expiry_date_time", self.quality_updates_pause_expiry_date_time)
        writer.write_bool_value("quality_updates_paused", self.quality_updates_paused)
        writer.write_datetime_value("quality_updates_rollback_start_date_time", self.quality_updates_rollback_start_date_time)
        writer.write_bool_value("quality_updates_will_be_rolled_back", self.quality_updates_will_be_rolled_back)
        writer.write_int_value("schedule_imminent_restart_warning_in_minutes", self.schedule_imminent_restart_warning_in_minutes)
        writer.write_int_value("schedule_restart_warning_in_hours", self.schedule_restart_warning_in_hours)
        writer.write_bool_value("skip_checks_before_restart", self.skip_checks_before_restart)
        writer.write_enum_value("update_notification_level", self.update_notification_level)
        writer.write_enum_value("update_weeks", self.update_weeks)
        writer.write_enum_value("user_pause_access", self.user_pause_access)
        writer.write_enum_value("user_windows_update_scan_access", self.user_windows_update_scan_access)
    

