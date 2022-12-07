from __future__ import annotations
from datetime import date, datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

auto_restart_notification_dismissal_method = lazy_import('msgraph.generated.models.auto_restart_notification_dismissal_method')
automatic_update_mode = lazy_import('msgraph.generated.models.automatic_update_mode')
device_configuration = lazy_import('msgraph.generated.models.device_configuration')
enablement = lazy_import('msgraph.generated.models.enablement')
prerelease_features = lazy_import('msgraph.generated.models.prerelease_features')
windows_delivery_optimization_mode = lazy_import('msgraph.generated.models.windows_delivery_optimization_mode')
windows_update_for_business_update_weeks = lazy_import('msgraph.generated.models.windows_update_for_business_update_weeks')
windows_update_install_schedule_type = lazy_import('msgraph.generated.models.windows_update_install_schedule_type')
windows_update_notification_display_option = lazy_import('msgraph.generated.models.windows_update_notification_display_option')
windows_update_type = lazy_import('msgraph.generated.models.windows_update_type')

class WindowsUpdateForBusinessConfiguration(device_configuration.DeviceConfiguration):
    @property
    def allow_windows11_upgrade(self,) -> Optional[bool]:
        """
        Gets the allowWindows11Upgrade property value. When TRUE, allows eligible Windows 10 devices to upgrade to Windows 11. When FALSE, implies the device stays on the existing operating system. Returned by default. Query parameters are not supported.
        Returns: Optional[bool]
        """
        return self._allow_windows11_upgrade
    
    @allow_windows11_upgrade.setter
    def allow_windows11_upgrade(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowWindows11Upgrade property value. When TRUE, allows eligible Windows 10 devices to upgrade to Windows 11. When FALSE, implies the device stays on the existing operating system. Returned by default. Query parameters are not supported.
        Args:
            value: Value to set for the allowWindows11Upgrade property.
        """
        self._allow_windows11_upgrade = value
    
    @property
    def automatic_update_mode(self,) -> Optional[automatic_update_mode.AutomaticUpdateMode]:
        """
        Gets the automaticUpdateMode property value. Possible values for automatic update mode.
        Returns: Optional[automatic_update_mode.AutomaticUpdateMode]
        """
        return self._automatic_update_mode
    
    @automatic_update_mode.setter
    def automatic_update_mode(self,value: Optional[automatic_update_mode.AutomaticUpdateMode] = None) -> None:
        """
        Sets the automaticUpdateMode property value. Possible values for automatic update mode.
        Args:
            value: Value to set for the automaticUpdateMode property.
        """
        self._automatic_update_mode = value
    
    @property
    def auto_restart_notification_dismissal(self,) -> Optional[auto_restart_notification_dismissal_method.AutoRestartNotificationDismissalMethod]:
        """
        Gets the autoRestartNotificationDismissal property value. Auto restart required notification dismissal method
        Returns: Optional[auto_restart_notification_dismissal_method.AutoRestartNotificationDismissalMethod]
        """
        return self._auto_restart_notification_dismissal
    
    @auto_restart_notification_dismissal.setter
    def auto_restart_notification_dismissal(self,value: Optional[auto_restart_notification_dismissal_method.AutoRestartNotificationDismissalMethod] = None) -> None:
        """
        Sets the autoRestartNotificationDismissal property value. Auto restart required notification dismissal method
        Args:
            value: Value to set for the autoRestartNotificationDismissal property.
        """
        self._auto_restart_notification_dismissal = value
    
    @property
    def business_ready_updates_only(self,) -> Optional[windows_update_type.WindowsUpdateType]:
        """
        Gets the businessReadyUpdatesOnly property value. Which branch devices will receive their updates from
        Returns: Optional[windows_update_type.WindowsUpdateType]
        """
        return self._business_ready_updates_only
    
    @business_ready_updates_only.setter
    def business_ready_updates_only(self,value: Optional[windows_update_type.WindowsUpdateType] = None) -> None:
        """
        Sets the businessReadyUpdatesOnly property value. Which branch devices will receive their updates from
        Args:
            value: Value to set for the businessReadyUpdatesOnly property.
        """
        self._business_ready_updates_only = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new WindowsUpdateForBusinessConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windowsUpdateForBusinessConfiguration"
        # When TRUE, allows eligible Windows 10 devices to upgrade to Windows 11. When FALSE, implies the device stays on the existing operating system. Returned by default. Query parameters are not supported.
        self._allow_windows11_upgrade: Optional[bool] = None
        # Possible values for automatic update mode.
        self._automatic_update_mode: Optional[automatic_update_mode.AutomaticUpdateMode] = None
        # Auto restart required notification dismissal method
        self._auto_restart_notification_dismissal: Optional[auto_restart_notification_dismissal_method.AutoRestartNotificationDismissalMethod] = None
        # Which branch devices will receive their updates from
        self._business_ready_updates_only: Optional[windows_update_type.WindowsUpdateType] = None
        # Number of days before feature updates are installed automatically with valid range from 0 to 30 days. Returned by default. Query parameters are not supported.
        self._deadline_for_feature_updates_in_days: Optional[int] = None
        # Number of days before quality updates are installed automatically with valid range from 0 to 30 days. Returned by default. Query parameters are not supported.
        self._deadline_for_quality_updates_in_days: Optional[int] = None
        # Number of days after deadline until restarts occur automatically with valid range from 0 to 7 days. Returned by default. Query parameters are not supported.
        self._deadline_grace_period_in_days: Optional[int] = None
        # Delivery optimization mode for peer distribution
        self._delivery_optimization_mode: Optional[windows_delivery_optimization_mode.WindowsDeliveryOptimizationMode] = None
        # When TRUE, excludes Windows update Drivers. When FALSE, does not exclude Windows update Drivers. Returned by default. Query parameters are not supported.
        self._drivers_excluded: Optional[bool] = None
        # Deadline in days before automatically scheduling and executing a pending restart outside of active hours, with valid range from 2 to 30 days. Returned by default. Query parameters are not supported.
        self._engaged_restart_deadline_in_days: Optional[int] = None
        # Number of days a user can snooze Engaged Restart reminder notifications with valid range from 1 to 3 days. Returned by default. Query parameters are not supported.
        self._engaged_restart_snooze_schedule_in_days: Optional[int] = None
        # Number of days before transitioning from Auto Restarts scheduled outside of active hours to Engaged Restart, which requires the user to schedule, with valid range from 0 to 30 days. Returned by default. Query parameters are not supported.
        self._engaged_restart_transition_schedule_in_days: Optional[int] = None
        # Defer Feature Updates by these many days with valid range from 0 to 30 days. Returned by default. Query parameters are not supported.
        self._feature_updates_deferral_period_in_days: Optional[int] = None
        # When TRUE, assigned devices are paused from receiving feature updates for up to 35 days from the time you pause the ring. When FALSE, does not pause Feature Updates. Returned by default. Query parameters are not supported.s
        self._feature_updates_paused: Optional[bool] = None
        # The Feature Updates Pause Expiry datetime. This value is 35 days from the time admin paused or extended the pause for the ring. Returned by default. Query parameters are not supported.
        self._feature_updates_pause_expiry_date_time: Optional[datetime] = None
        # The Feature Updates Pause start date. This value is the time when the admin paused or extended the pause for the ring. Returned by default. Query parameters are not supported. This property is read-only.
        self._feature_updates_pause_start_date: Optional[Date] = None
        # The Feature Updates Rollback Start datetime.This value is the time when the admin rolled back the Feature update for the ring.Returned by default.Query parameters are not supported.
        self._feature_updates_rollback_start_date_time: Optional[datetime] = None
        # The number of days after a Feature Update for which a rollback is valid with valid range from 2 to 60 days. Returned by default. Query parameters are not supported.
        self._feature_updates_rollback_window_in_days: Optional[int] = None
        # When TRUE, rollback Feature Updates on the next device check in. When FALSE, do not rollback Feature Updates on the next device check in. Returned by default.Query parameters are not supported.
        self._feature_updates_will_be_rolled_back: Optional[bool] = None
        # The Installation Schedule. Possible values are: ActiveHoursStart, ActiveHoursEnd, ScheduledInstallDay, ScheduledInstallTime. Returned by default. Query parameters are not supported.
        self._installation_schedule: Optional[windows_update_install_schedule_type.WindowsUpdateInstallScheduleType] = None
        # When TRUE, allows Microsoft Update Service. When FALSE, does not allow Microsoft Update Service. Returned by default. Query parameters are not supported.
        self._microsoft_update_service_allowed: Optional[bool] = None
        # When TRUE the device should wait until deadline for rebooting outside of active hours. When FALSE the device should not wait until deadline for rebooting outside of active hours. Returned by default. Query parameters are not supported.
        self._postpone_reboot_until_after_deadline: Optional[bool] = None
        # Possible values for pre-release features.
        self._prerelease_features: Optional[prerelease_features.PrereleaseFeatures] = None
        # Defer Quality Updates by these many days with valid range from 0 to 30 days. Returned by default. Query parameters are not supported.
        self._quality_updates_deferral_period_in_days: Optional[int] = None
        # When TRUE, assigned devices are paused from receiving quality updates for up to 35 days from the time you pause the ring. When FALSE, does not pause Quality Updates. Returned by default. Query parameters are not supported.
        self._quality_updates_paused: Optional[bool] = None
        # The Quality Updates Pause Expiry datetime. This value is 35 days from the time admin paused or extended the pause for the ring. Returned by default. Query parameters are not supported.
        self._quality_updates_pause_expiry_date_time: Optional[datetime] = None
        # The Quality Updates Pause start date. This value is the time when the admin paused or extended the pause for the ring. Returned by default. Query parameters are not supported. This property is read-only.
        self._quality_updates_pause_start_date: Optional[Date] = None
        # The Quality Updates Rollback Start datetime. This value is the time when the admin rolled back the Quality update for the ring. Returned by default. Query parameters are not supported.
        self._quality_updates_rollback_start_date_time: Optional[datetime] = None
        # When TRUE, rollback Quality Updates on the next device check in. When FALSE, do not rollback Quality Updates on the next device check in. Returned by default. Query parameters are not supported.
        self._quality_updates_will_be_rolled_back: Optional[bool] = None
        # Specify the period for auto-restart imminent warning notifications. Supported values: 15, 30 or 60 (minutes). Returned by default. Query parameters are not supported.
        self._schedule_imminent_restart_warning_in_minutes: Optional[int] = None
        # Specify the period for auto-restart warning reminder notifications. Supported values: 2, 4, 8, 12 or 24 (hours). Returned by default. Query parameters are not supported.
        self._schedule_restart_warning_in_hours: Optional[int] = None
        # When TRUE, skips all checks before restart: Battery level = 40%, User presence, Display Needed, Presentation mode, Full screen mode, phone call state, game mode etc. When FALSE, does not skip all checks before restart. Returned by default. Query parameters are not supported.
        self._skip_checks_before_restart: Optional[bool] = None
        # Windows Update Notification Display Options
        self._update_notification_level: Optional[windows_update_notification_display_option.WindowsUpdateNotificationDisplayOption] = None
        # Schedule the update installation on the weeks of the month. Possible values are: UserDefined, FirstWeek, SecondWeek, ThirdWeek, FourthWeek, EveryWeek. Returned by default. Query parameters are not supported. Possible values are: userDefined, firstWeek, secondWeek, thirdWeek, fourthWeek, everyWeek, unknownFutureValue.
        self._update_weeks: Optional[windows_update_for_business_update_weeks.WindowsUpdateForBusinessUpdateWeeks] = None
        # Possible values of a property
        self._user_pause_access: Optional[enablement.Enablement] = None
        # Possible values of a property
        self._user_windows_update_scan_access: Optional[enablement.Enablement] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsUpdateForBusinessConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsUpdateForBusinessConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsUpdateForBusinessConfiguration()
    
    @property
    def deadline_for_feature_updates_in_days(self,) -> Optional[int]:
        """
        Gets the deadlineForFeatureUpdatesInDays property value. Number of days before feature updates are installed automatically with valid range from 0 to 30 days. Returned by default. Query parameters are not supported.
        Returns: Optional[int]
        """
        return self._deadline_for_feature_updates_in_days
    
    @deadline_for_feature_updates_in_days.setter
    def deadline_for_feature_updates_in_days(self,value: Optional[int] = None) -> None:
        """
        Sets the deadlineForFeatureUpdatesInDays property value. Number of days before feature updates are installed automatically with valid range from 0 to 30 days. Returned by default. Query parameters are not supported.
        Args:
            value: Value to set for the deadlineForFeatureUpdatesInDays property.
        """
        self._deadline_for_feature_updates_in_days = value
    
    @property
    def deadline_for_quality_updates_in_days(self,) -> Optional[int]:
        """
        Gets the deadlineForQualityUpdatesInDays property value. Number of days before quality updates are installed automatically with valid range from 0 to 30 days. Returned by default. Query parameters are not supported.
        Returns: Optional[int]
        """
        return self._deadline_for_quality_updates_in_days
    
    @deadline_for_quality_updates_in_days.setter
    def deadline_for_quality_updates_in_days(self,value: Optional[int] = None) -> None:
        """
        Sets the deadlineForQualityUpdatesInDays property value. Number of days before quality updates are installed automatically with valid range from 0 to 30 days. Returned by default. Query parameters are not supported.
        Args:
            value: Value to set for the deadlineForQualityUpdatesInDays property.
        """
        self._deadline_for_quality_updates_in_days = value
    
    @property
    def deadline_grace_period_in_days(self,) -> Optional[int]:
        """
        Gets the deadlineGracePeriodInDays property value. Number of days after deadline until restarts occur automatically with valid range from 0 to 7 days. Returned by default. Query parameters are not supported.
        Returns: Optional[int]
        """
        return self._deadline_grace_period_in_days
    
    @deadline_grace_period_in_days.setter
    def deadline_grace_period_in_days(self,value: Optional[int] = None) -> None:
        """
        Sets the deadlineGracePeriodInDays property value. Number of days after deadline until restarts occur automatically with valid range from 0 to 7 days. Returned by default. Query parameters are not supported.
        Args:
            value: Value to set for the deadlineGracePeriodInDays property.
        """
        self._deadline_grace_period_in_days = value
    
    @property
    def delivery_optimization_mode(self,) -> Optional[windows_delivery_optimization_mode.WindowsDeliveryOptimizationMode]:
        """
        Gets the deliveryOptimizationMode property value. Delivery optimization mode for peer distribution
        Returns: Optional[windows_delivery_optimization_mode.WindowsDeliveryOptimizationMode]
        """
        return self._delivery_optimization_mode
    
    @delivery_optimization_mode.setter
    def delivery_optimization_mode(self,value: Optional[windows_delivery_optimization_mode.WindowsDeliveryOptimizationMode] = None) -> None:
        """
        Sets the deliveryOptimizationMode property value. Delivery optimization mode for peer distribution
        Args:
            value: Value to set for the deliveryOptimizationMode property.
        """
        self._delivery_optimization_mode = value
    
    @property
    def drivers_excluded(self,) -> Optional[bool]:
        """
        Gets the driversExcluded property value. When TRUE, excludes Windows update Drivers. When FALSE, does not exclude Windows update Drivers. Returned by default. Query parameters are not supported.
        Returns: Optional[bool]
        """
        return self._drivers_excluded
    
    @drivers_excluded.setter
    def drivers_excluded(self,value: Optional[bool] = None) -> None:
        """
        Sets the driversExcluded property value. When TRUE, excludes Windows update Drivers. When FALSE, does not exclude Windows update Drivers. Returned by default. Query parameters are not supported.
        Args:
            value: Value to set for the driversExcluded property.
        """
        self._drivers_excluded = value
    
    @property
    def engaged_restart_deadline_in_days(self,) -> Optional[int]:
        """
        Gets the engagedRestartDeadlineInDays property value. Deadline in days before automatically scheduling and executing a pending restart outside of active hours, with valid range from 2 to 30 days. Returned by default. Query parameters are not supported.
        Returns: Optional[int]
        """
        return self._engaged_restart_deadline_in_days
    
    @engaged_restart_deadline_in_days.setter
    def engaged_restart_deadline_in_days(self,value: Optional[int] = None) -> None:
        """
        Sets the engagedRestartDeadlineInDays property value. Deadline in days before automatically scheduling and executing a pending restart outside of active hours, with valid range from 2 to 30 days. Returned by default. Query parameters are not supported.
        Args:
            value: Value to set for the engagedRestartDeadlineInDays property.
        """
        self._engaged_restart_deadline_in_days = value
    
    @property
    def engaged_restart_snooze_schedule_in_days(self,) -> Optional[int]:
        """
        Gets the engagedRestartSnoozeScheduleInDays property value. Number of days a user can snooze Engaged Restart reminder notifications with valid range from 1 to 3 days. Returned by default. Query parameters are not supported.
        Returns: Optional[int]
        """
        return self._engaged_restart_snooze_schedule_in_days
    
    @engaged_restart_snooze_schedule_in_days.setter
    def engaged_restart_snooze_schedule_in_days(self,value: Optional[int] = None) -> None:
        """
        Sets the engagedRestartSnoozeScheduleInDays property value. Number of days a user can snooze Engaged Restart reminder notifications with valid range from 1 to 3 days. Returned by default. Query parameters are not supported.
        Args:
            value: Value to set for the engagedRestartSnoozeScheduleInDays property.
        """
        self._engaged_restart_snooze_schedule_in_days = value
    
    @property
    def engaged_restart_transition_schedule_in_days(self,) -> Optional[int]:
        """
        Gets the engagedRestartTransitionScheduleInDays property value. Number of days before transitioning from Auto Restarts scheduled outside of active hours to Engaged Restart, which requires the user to schedule, with valid range from 0 to 30 days. Returned by default. Query parameters are not supported.
        Returns: Optional[int]
        """
        return self._engaged_restart_transition_schedule_in_days
    
    @engaged_restart_transition_schedule_in_days.setter
    def engaged_restart_transition_schedule_in_days(self,value: Optional[int] = None) -> None:
        """
        Sets the engagedRestartTransitionScheduleInDays property value. Number of days before transitioning from Auto Restarts scheduled outside of active hours to Engaged Restart, which requires the user to schedule, with valid range from 0 to 30 days. Returned by default. Query parameters are not supported.
        Args:
            value: Value to set for the engagedRestartTransitionScheduleInDays property.
        """
        self._engaged_restart_transition_schedule_in_days = value
    
    @property
    def feature_updates_deferral_period_in_days(self,) -> Optional[int]:
        """
        Gets the featureUpdatesDeferralPeriodInDays property value. Defer Feature Updates by these many days with valid range from 0 to 30 days. Returned by default. Query parameters are not supported.
        Returns: Optional[int]
        """
        return self._feature_updates_deferral_period_in_days
    
    @feature_updates_deferral_period_in_days.setter
    def feature_updates_deferral_period_in_days(self,value: Optional[int] = None) -> None:
        """
        Sets the featureUpdatesDeferralPeriodInDays property value. Defer Feature Updates by these many days with valid range from 0 to 30 days. Returned by default. Query parameters are not supported.
        Args:
            value: Value to set for the featureUpdatesDeferralPeriodInDays property.
        """
        self._feature_updates_deferral_period_in_days = value
    
    @property
    def feature_updates_paused(self,) -> Optional[bool]:
        """
        Gets the featureUpdatesPaused property value. When TRUE, assigned devices are paused from receiving feature updates for up to 35 days from the time you pause the ring. When FALSE, does not pause Feature Updates. Returned by default. Query parameters are not supported.s
        Returns: Optional[bool]
        """
        return self._feature_updates_paused
    
    @feature_updates_paused.setter
    def feature_updates_paused(self,value: Optional[bool] = None) -> None:
        """
        Sets the featureUpdatesPaused property value. When TRUE, assigned devices are paused from receiving feature updates for up to 35 days from the time you pause the ring. When FALSE, does not pause Feature Updates. Returned by default. Query parameters are not supported.s
        Args:
            value: Value to set for the featureUpdatesPaused property.
        """
        self._feature_updates_paused = value
    
    @property
    def feature_updates_pause_expiry_date_time(self,) -> Optional[datetime]:
        """
        Gets the featureUpdatesPauseExpiryDateTime property value. The Feature Updates Pause Expiry datetime. This value is 35 days from the time admin paused or extended the pause for the ring. Returned by default. Query parameters are not supported.
        Returns: Optional[datetime]
        """
        return self._feature_updates_pause_expiry_date_time
    
    @feature_updates_pause_expiry_date_time.setter
    def feature_updates_pause_expiry_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the featureUpdatesPauseExpiryDateTime property value. The Feature Updates Pause Expiry datetime. This value is 35 days from the time admin paused or extended the pause for the ring. Returned by default. Query parameters are not supported.
        Args:
            value: Value to set for the featureUpdatesPauseExpiryDateTime property.
        """
        self._feature_updates_pause_expiry_date_time = value
    
    @property
    def feature_updates_pause_start_date(self,) -> Optional[Date]:
        """
        Gets the featureUpdatesPauseStartDate property value. The Feature Updates Pause start date. This value is the time when the admin paused or extended the pause for the ring. Returned by default. Query parameters are not supported. This property is read-only.
        Returns: Optional[Date]
        """
        return self._feature_updates_pause_start_date
    
    @feature_updates_pause_start_date.setter
    def feature_updates_pause_start_date(self,value: Optional[Date] = None) -> None:
        """
        Sets the featureUpdatesPauseStartDate property value. The Feature Updates Pause start date. This value is the time when the admin paused or extended the pause for the ring. Returned by default. Query parameters are not supported. This property is read-only.
        Args:
            value: Value to set for the featureUpdatesPauseStartDate property.
        """
        self._feature_updates_pause_start_date = value
    
    @property
    def feature_updates_rollback_start_date_time(self,) -> Optional[datetime]:
        """
        Gets the featureUpdatesRollbackStartDateTime property value. The Feature Updates Rollback Start datetime.This value is the time when the admin rolled back the Feature update for the ring.Returned by default.Query parameters are not supported.
        Returns: Optional[datetime]
        """
        return self._feature_updates_rollback_start_date_time
    
    @feature_updates_rollback_start_date_time.setter
    def feature_updates_rollback_start_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the featureUpdatesRollbackStartDateTime property value. The Feature Updates Rollback Start datetime.This value is the time when the admin rolled back the Feature update for the ring.Returned by default.Query parameters are not supported.
        Args:
            value: Value to set for the featureUpdatesRollbackStartDateTime property.
        """
        self._feature_updates_rollback_start_date_time = value
    
    @property
    def feature_updates_rollback_window_in_days(self,) -> Optional[int]:
        """
        Gets the featureUpdatesRollbackWindowInDays property value. The number of days after a Feature Update for which a rollback is valid with valid range from 2 to 60 days. Returned by default. Query parameters are not supported.
        Returns: Optional[int]
        """
        return self._feature_updates_rollback_window_in_days
    
    @feature_updates_rollback_window_in_days.setter
    def feature_updates_rollback_window_in_days(self,value: Optional[int] = None) -> None:
        """
        Sets the featureUpdatesRollbackWindowInDays property value. The number of days after a Feature Update for which a rollback is valid with valid range from 2 to 60 days. Returned by default. Query parameters are not supported.
        Args:
            value: Value to set for the featureUpdatesRollbackWindowInDays property.
        """
        self._feature_updates_rollback_window_in_days = value
    
    @property
    def feature_updates_will_be_rolled_back(self,) -> Optional[bool]:
        """
        Gets the featureUpdatesWillBeRolledBack property value. When TRUE, rollback Feature Updates on the next device check in. When FALSE, do not rollback Feature Updates on the next device check in. Returned by default.Query parameters are not supported.
        Returns: Optional[bool]
        """
        return self._feature_updates_will_be_rolled_back
    
    @feature_updates_will_be_rolled_back.setter
    def feature_updates_will_be_rolled_back(self,value: Optional[bool] = None) -> None:
        """
        Sets the featureUpdatesWillBeRolledBack property value. When TRUE, rollback Feature Updates on the next device check in. When FALSE, do not rollback Feature Updates on the next device check in. Returned by default.Query parameters are not supported.
        Args:
            value: Value to set for the featureUpdatesWillBeRolledBack property.
        """
        self._feature_updates_will_be_rolled_back = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "allow_windows11_upgrade": lambda n : setattr(self, 'allow_windows11_upgrade', n.get_bool_value()),
            "automatic_update_mode": lambda n : setattr(self, 'automatic_update_mode', n.get_enum_value(automatic_update_mode.AutomaticUpdateMode)),
            "auto_restart_notification_dismissal": lambda n : setattr(self, 'auto_restart_notification_dismissal', n.get_enum_value(auto_restart_notification_dismissal_method.AutoRestartNotificationDismissalMethod)),
            "business_ready_updates_only": lambda n : setattr(self, 'business_ready_updates_only', n.get_enum_value(windows_update_type.WindowsUpdateType)),
            "deadline_for_feature_updates_in_days": lambda n : setattr(self, 'deadline_for_feature_updates_in_days', n.get_int_value()),
            "deadline_for_quality_updates_in_days": lambda n : setattr(self, 'deadline_for_quality_updates_in_days', n.get_int_value()),
            "deadline_grace_period_in_days": lambda n : setattr(self, 'deadline_grace_period_in_days', n.get_int_value()),
            "delivery_optimization_mode": lambda n : setattr(self, 'delivery_optimization_mode', n.get_enum_value(windows_delivery_optimization_mode.WindowsDeliveryOptimizationMode)),
            "drivers_excluded": lambda n : setattr(self, 'drivers_excluded', n.get_bool_value()),
            "engaged_restart_deadline_in_days": lambda n : setattr(self, 'engaged_restart_deadline_in_days', n.get_int_value()),
            "engaged_restart_snooze_schedule_in_days": lambda n : setattr(self, 'engaged_restart_snooze_schedule_in_days', n.get_int_value()),
            "engaged_restart_transition_schedule_in_days": lambda n : setattr(self, 'engaged_restart_transition_schedule_in_days', n.get_int_value()),
            "feature_updates_deferral_period_in_days": lambda n : setattr(self, 'feature_updates_deferral_period_in_days', n.get_int_value()),
            "feature_updates_paused": lambda n : setattr(self, 'feature_updates_paused', n.get_bool_value()),
            "feature_updates_pause_expiry_date_time": lambda n : setattr(self, 'feature_updates_pause_expiry_date_time', n.get_datetime_value()),
            "feature_updates_pause_start_date": lambda n : setattr(self, 'feature_updates_pause_start_date', n.get_object_value(Date)),
            "feature_updates_rollback_start_date_time": lambda n : setattr(self, 'feature_updates_rollback_start_date_time', n.get_datetime_value()),
            "feature_updates_rollback_window_in_days": lambda n : setattr(self, 'feature_updates_rollback_window_in_days', n.get_int_value()),
            "feature_updates_will_be_rolled_back": lambda n : setattr(self, 'feature_updates_will_be_rolled_back', n.get_bool_value()),
            "installation_schedule": lambda n : setattr(self, 'installation_schedule', n.get_object_value(windows_update_install_schedule_type.WindowsUpdateInstallScheduleType)),
            "microsoft_update_service_allowed": lambda n : setattr(self, 'microsoft_update_service_allowed', n.get_bool_value()),
            "postpone_reboot_until_after_deadline": lambda n : setattr(self, 'postpone_reboot_until_after_deadline', n.get_bool_value()),
            "prerelease_features": lambda n : setattr(self, 'prerelease_features', n.get_enum_value(prerelease_features.PrereleaseFeatures)),
            "quality_updates_deferral_period_in_days": lambda n : setattr(self, 'quality_updates_deferral_period_in_days', n.get_int_value()),
            "quality_updates_paused": lambda n : setattr(self, 'quality_updates_paused', n.get_bool_value()),
            "quality_updates_pause_expiry_date_time": lambda n : setattr(self, 'quality_updates_pause_expiry_date_time', n.get_datetime_value()),
            "quality_updates_pause_start_date": lambda n : setattr(self, 'quality_updates_pause_start_date', n.get_object_value(Date)),
            "quality_updates_rollback_start_date_time": lambda n : setattr(self, 'quality_updates_rollback_start_date_time', n.get_datetime_value()),
            "quality_updates_will_be_rolled_back": lambda n : setattr(self, 'quality_updates_will_be_rolled_back', n.get_bool_value()),
            "schedule_imminent_restart_warning_in_minutes": lambda n : setattr(self, 'schedule_imminent_restart_warning_in_minutes', n.get_int_value()),
            "schedule_restart_warning_in_hours": lambda n : setattr(self, 'schedule_restart_warning_in_hours', n.get_int_value()),
            "skip_checks_before_restart": lambda n : setattr(self, 'skip_checks_before_restart', n.get_bool_value()),
            "update_notification_level": lambda n : setattr(self, 'update_notification_level', n.get_enum_value(windows_update_notification_display_option.WindowsUpdateNotificationDisplayOption)),
            "update_weeks": lambda n : setattr(self, 'update_weeks', n.get_enum_value(windows_update_for_business_update_weeks.WindowsUpdateForBusinessUpdateWeeks)),
            "user_pause_access": lambda n : setattr(self, 'user_pause_access', n.get_enum_value(enablement.Enablement)),
            "user_windows_update_scan_access": lambda n : setattr(self, 'user_windows_update_scan_access', n.get_enum_value(enablement.Enablement)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def installation_schedule(self,) -> Optional[windows_update_install_schedule_type.WindowsUpdateInstallScheduleType]:
        """
        Gets the installationSchedule property value. The Installation Schedule. Possible values are: ActiveHoursStart, ActiveHoursEnd, ScheduledInstallDay, ScheduledInstallTime. Returned by default. Query parameters are not supported.
        Returns: Optional[windows_update_install_schedule_type.WindowsUpdateInstallScheduleType]
        """
        return self._installation_schedule
    
    @installation_schedule.setter
    def installation_schedule(self,value: Optional[windows_update_install_schedule_type.WindowsUpdateInstallScheduleType] = None) -> None:
        """
        Sets the installationSchedule property value. The Installation Schedule. Possible values are: ActiveHoursStart, ActiveHoursEnd, ScheduledInstallDay, ScheduledInstallTime. Returned by default. Query parameters are not supported.
        Args:
            value: Value to set for the installationSchedule property.
        """
        self._installation_schedule = value
    
    @property
    def microsoft_update_service_allowed(self,) -> Optional[bool]:
        """
        Gets the microsoftUpdateServiceAllowed property value. When TRUE, allows Microsoft Update Service. When FALSE, does not allow Microsoft Update Service. Returned by default. Query parameters are not supported.
        Returns: Optional[bool]
        """
        return self._microsoft_update_service_allowed
    
    @microsoft_update_service_allowed.setter
    def microsoft_update_service_allowed(self,value: Optional[bool] = None) -> None:
        """
        Sets the microsoftUpdateServiceAllowed property value. When TRUE, allows Microsoft Update Service. When FALSE, does not allow Microsoft Update Service. Returned by default. Query parameters are not supported.
        Args:
            value: Value to set for the microsoftUpdateServiceAllowed property.
        """
        self._microsoft_update_service_allowed = value
    
    @property
    def postpone_reboot_until_after_deadline(self,) -> Optional[bool]:
        """
        Gets the postponeRebootUntilAfterDeadline property value. When TRUE the device should wait until deadline for rebooting outside of active hours. When FALSE the device should not wait until deadline for rebooting outside of active hours. Returned by default. Query parameters are not supported.
        Returns: Optional[bool]
        """
        return self._postpone_reboot_until_after_deadline
    
    @postpone_reboot_until_after_deadline.setter
    def postpone_reboot_until_after_deadline(self,value: Optional[bool] = None) -> None:
        """
        Sets the postponeRebootUntilAfterDeadline property value. When TRUE the device should wait until deadline for rebooting outside of active hours. When FALSE the device should not wait until deadline for rebooting outside of active hours. Returned by default. Query parameters are not supported.
        Args:
            value: Value to set for the postponeRebootUntilAfterDeadline property.
        """
        self._postpone_reboot_until_after_deadline = value
    
    @property
    def prerelease_features(self,) -> Optional[prerelease_features.PrereleaseFeatures]:
        """
        Gets the prereleaseFeatures property value. Possible values for pre-release features.
        Returns: Optional[prerelease_features.PrereleaseFeatures]
        """
        return self._prerelease_features
    
    @prerelease_features.setter
    def prerelease_features(self,value: Optional[prerelease_features.PrereleaseFeatures] = None) -> None:
        """
        Sets the prereleaseFeatures property value. Possible values for pre-release features.
        Args:
            value: Value to set for the prereleaseFeatures property.
        """
        self._prerelease_features = value
    
    @property
    def quality_updates_deferral_period_in_days(self,) -> Optional[int]:
        """
        Gets the qualityUpdatesDeferralPeriodInDays property value. Defer Quality Updates by these many days with valid range from 0 to 30 days. Returned by default. Query parameters are not supported.
        Returns: Optional[int]
        """
        return self._quality_updates_deferral_period_in_days
    
    @quality_updates_deferral_period_in_days.setter
    def quality_updates_deferral_period_in_days(self,value: Optional[int] = None) -> None:
        """
        Sets the qualityUpdatesDeferralPeriodInDays property value. Defer Quality Updates by these many days with valid range from 0 to 30 days. Returned by default. Query parameters are not supported.
        Args:
            value: Value to set for the qualityUpdatesDeferralPeriodInDays property.
        """
        self._quality_updates_deferral_period_in_days = value
    
    @property
    def quality_updates_paused(self,) -> Optional[bool]:
        """
        Gets the qualityUpdatesPaused property value. When TRUE, assigned devices are paused from receiving quality updates for up to 35 days from the time you pause the ring. When FALSE, does not pause Quality Updates. Returned by default. Query parameters are not supported.
        Returns: Optional[bool]
        """
        return self._quality_updates_paused
    
    @quality_updates_paused.setter
    def quality_updates_paused(self,value: Optional[bool] = None) -> None:
        """
        Sets the qualityUpdatesPaused property value. When TRUE, assigned devices are paused from receiving quality updates for up to 35 days from the time you pause the ring. When FALSE, does not pause Quality Updates. Returned by default. Query parameters are not supported.
        Args:
            value: Value to set for the qualityUpdatesPaused property.
        """
        self._quality_updates_paused = value
    
    @property
    def quality_updates_pause_expiry_date_time(self,) -> Optional[datetime]:
        """
        Gets the qualityUpdatesPauseExpiryDateTime property value. The Quality Updates Pause Expiry datetime. This value is 35 days from the time admin paused or extended the pause for the ring. Returned by default. Query parameters are not supported.
        Returns: Optional[datetime]
        """
        return self._quality_updates_pause_expiry_date_time
    
    @quality_updates_pause_expiry_date_time.setter
    def quality_updates_pause_expiry_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the qualityUpdatesPauseExpiryDateTime property value. The Quality Updates Pause Expiry datetime. This value is 35 days from the time admin paused or extended the pause for the ring. Returned by default. Query parameters are not supported.
        Args:
            value: Value to set for the qualityUpdatesPauseExpiryDateTime property.
        """
        self._quality_updates_pause_expiry_date_time = value
    
    @property
    def quality_updates_pause_start_date(self,) -> Optional[Date]:
        """
        Gets the qualityUpdatesPauseStartDate property value. The Quality Updates Pause start date. This value is the time when the admin paused or extended the pause for the ring. Returned by default. Query parameters are not supported. This property is read-only.
        Returns: Optional[Date]
        """
        return self._quality_updates_pause_start_date
    
    @quality_updates_pause_start_date.setter
    def quality_updates_pause_start_date(self,value: Optional[Date] = None) -> None:
        """
        Sets the qualityUpdatesPauseStartDate property value. The Quality Updates Pause start date. This value is the time when the admin paused or extended the pause for the ring. Returned by default. Query parameters are not supported. This property is read-only.
        Args:
            value: Value to set for the qualityUpdatesPauseStartDate property.
        """
        self._quality_updates_pause_start_date = value
    
    @property
    def quality_updates_rollback_start_date_time(self,) -> Optional[datetime]:
        """
        Gets the qualityUpdatesRollbackStartDateTime property value. The Quality Updates Rollback Start datetime. This value is the time when the admin rolled back the Quality update for the ring. Returned by default. Query parameters are not supported.
        Returns: Optional[datetime]
        """
        return self._quality_updates_rollback_start_date_time
    
    @quality_updates_rollback_start_date_time.setter
    def quality_updates_rollback_start_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the qualityUpdatesRollbackStartDateTime property value. The Quality Updates Rollback Start datetime. This value is the time when the admin rolled back the Quality update for the ring. Returned by default. Query parameters are not supported.
        Args:
            value: Value to set for the qualityUpdatesRollbackStartDateTime property.
        """
        self._quality_updates_rollback_start_date_time = value
    
    @property
    def quality_updates_will_be_rolled_back(self,) -> Optional[bool]:
        """
        Gets the qualityUpdatesWillBeRolledBack property value. When TRUE, rollback Quality Updates on the next device check in. When FALSE, do not rollback Quality Updates on the next device check in. Returned by default. Query parameters are not supported.
        Returns: Optional[bool]
        """
        return self._quality_updates_will_be_rolled_back
    
    @quality_updates_will_be_rolled_back.setter
    def quality_updates_will_be_rolled_back(self,value: Optional[bool] = None) -> None:
        """
        Sets the qualityUpdatesWillBeRolledBack property value. When TRUE, rollback Quality Updates on the next device check in. When FALSE, do not rollback Quality Updates on the next device check in. Returned by default. Query parameters are not supported.
        Args:
            value: Value to set for the qualityUpdatesWillBeRolledBack property.
        """
        self._quality_updates_will_be_rolled_back = value
    
    @property
    def schedule_imminent_restart_warning_in_minutes(self,) -> Optional[int]:
        """
        Gets the scheduleImminentRestartWarningInMinutes property value. Specify the period for auto-restart imminent warning notifications. Supported values: 15, 30 or 60 (minutes). Returned by default. Query parameters are not supported.
        Returns: Optional[int]
        """
        return self._schedule_imminent_restart_warning_in_minutes
    
    @schedule_imminent_restart_warning_in_minutes.setter
    def schedule_imminent_restart_warning_in_minutes(self,value: Optional[int] = None) -> None:
        """
        Sets the scheduleImminentRestartWarningInMinutes property value. Specify the period for auto-restart imminent warning notifications. Supported values: 15, 30 or 60 (minutes). Returned by default. Query parameters are not supported.
        Args:
            value: Value to set for the scheduleImminentRestartWarningInMinutes property.
        """
        self._schedule_imminent_restart_warning_in_minutes = value
    
    @property
    def schedule_restart_warning_in_hours(self,) -> Optional[int]:
        """
        Gets the scheduleRestartWarningInHours property value. Specify the period for auto-restart warning reminder notifications. Supported values: 2, 4, 8, 12 or 24 (hours). Returned by default. Query parameters are not supported.
        Returns: Optional[int]
        """
        return self._schedule_restart_warning_in_hours
    
    @schedule_restart_warning_in_hours.setter
    def schedule_restart_warning_in_hours(self,value: Optional[int] = None) -> None:
        """
        Sets the scheduleRestartWarningInHours property value. Specify the period for auto-restart warning reminder notifications. Supported values: 2, 4, 8, 12 or 24 (hours). Returned by default. Query parameters are not supported.
        Args:
            value: Value to set for the scheduleRestartWarningInHours property.
        """
        self._schedule_restart_warning_in_hours = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("allowWindows11Upgrade", self.allow_windows11_upgrade)
        writer.write_enum_value("automaticUpdateMode", self.automatic_update_mode)
        writer.write_enum_value("autoRestartNotificationDismissal", self.auto_restart_notification_dismissal)
        writer.write_enum_value("businessReadyUpdatesOnly", self.business_ready_updates_only)
        writer.write_int_value("deadlineForFeatureUpdatesInDays", self.deadline_for_feature_updates_in_days)
        writer.write_int_value("deadlineForQualityUpdatesInDays", self.deadline_for_quality_updates_in_days)
        writer.write_int_value("deadlineGracePeriodInDays", self.deadline_grace_period_in_days)
        writer.write_enum_value("deliveryOptimizationMode", self.delivery_optimization_mode)
        writer.write_bool_value("driversExcluded", self.drivers_excluded)
        writer.write_int_value("engagedRestartDeadlineInDays", self.engaged_restart_deadline_in_days)
        writer.write_int_value("engagedRestartSnoozeScheduleInDays", self.engaged_restart_snooze_schedule_in_days)
        writer.write_int_value("engagedRestartTransitionScheduleInDays", self.engaged_restart_transition_schedule_in_days)
        writer.write_int_value("featureUpdatesDeferralPeriodInDays", self.feature_updates_deferral_period_in_days)
        writer.write_bool_value("featureUpdatesPaused", self.feature_updates_paused)
        writer.write_datetime_value("featureUpdatesPauseExpiryDateTime", self.feature_updates_pause_expiry_date_time)
        writer.write_datetime_value("featureUpdatesRollbackStartDateTime", self.feature_updates_rollback_start_date_time)
        writer.write_int_value("featureUpdatesRollbackWindowInDays", self.feature_updates_rollback_window_in_days)
        writer.write_bool_value("featureUpdatesWillBeRolledBack", self.feature_updates_will_be_rolled_back)
        writer.write_object_value("installationSchedule", self.installation_schedule)
        writer.write_bool_value("microsoftUpdateServiceAllowed", self.microsoft_update_service_allowed)
        writer.write_bool_value("postponeRebootUntilAfterDeadline", self.postpone_reboot_until_after_deadline)
        writer.write_enum_value("prereleaseFeatures", self.prerelease_features)
        writer.write_int_value("qualityUpdatesDeferralPeriodInDays", self.quality_updates_deferral_period_in_days)
        writer.write_bool_value("qualityUpdatesPaused", self.quality_updates_paused)
        writer.write_datetime_value("qualityUpdatesPauseExpiryDateTime", self.quality_updates_pause_expiry_date_time)
        writer.write_datetime_value("qualityUpdatesRollbackStartDateTime", self.quality_updates_rollback_start_date_time)
        writer.write_bool_value("qualityUpdatesWillBeRolledBack", self.quality_updates_will_be_rolled_back)
        writer.write_int_value("scheduleImminentRestartWarningInMinutes", self.schedule_imminent_restart_warning_in_minutes)
        writer.write_int_value("scheduleRestartWarningInHours", self.schedule_restart_warning_in_hours)
        writer.write_bool_value("skipChecksBeforeRestart", self.skip_checks_before_restart)
        writer.write_enum_value("updateNotificationLevel", self.update_notification_level)
        writer.write_enum_value("updateWeeks", self.update_weeks)
        writer.write_enum_value("userPauseAccess", self.user_pause_access)
        writer.write_enum_value("userWindowsUpdateScanAccess", self.user_windows_update_scan_access)
    
    @property
    def skip_checks_before_restart(self,) -> Optional[bool]:
        """
        Gets the skipChecksBeforeRestart property value. When TRUE, skips all checks before restart: Battery level = 40%, User presence, Display Needed, Presentation mode, Full screen mode, phone call state, game mode etc. When FALSE, does not skip all checks before restart. Returned by default. Query parameters are not supported.
        Returns: Optional[bool]
        """
        return self._skip_checks_before_restart
    
    @skip_checks_before_restart.setter
    def skip_checks_before_restart(self,value: Optional[bool] = None) -> None:
        """
        Sets the skipChecksBeforeRestart property value. When TRUE, skips all checks before restart: Battery level = 40%, User presence, Display Needed, Presentation mode, Full screen mode, phone call state, game mode etc. When FALSE, does not skip all checks before restart. Returned by default. Query parameters are not supported.
        Args:
            value: Value to set for the skipChecksBeforeRestart property.
        """
        self._skip_checks_before_restart = value
    
    @property
    def update_notification_level(self,) -> Optional[windows_update_notification_display_option.WindowsUpdateNotificationDisplayOption]:
        """
        Gets the updateNotificationLevel property value. Windows Update Notification Display Options
        Returns: Optional[windows_update_notification_display_option.WindowsUpdateNotificationDisplayOption]
        """
        return self._update_notification_level
    
    @update_notification_level.setter
    def update_notification_level(self,value: Optional[windows_update_notification_display_option.WindowsUpdateNotificationDisplayOption] = None) -> None:
        """
        Sets the updateNotificationLevel property value. Windows Update Notification Display Options
        Args:
            value: Value to set for the updateNotificationLevel property.
        """
        self._update_notification_level = value
    
    @property
    def update_weeks(self,) -> Optional[windows_update_for_business_update_weeks.WindowsUpdateForBusinessUpdateWeeks]:
        """
        Gets the updateWeeks property value. Schedule the update installation on the weeks of the month. Possible values are: UserDefined, FirstWeek, SecondWeek, ThirdWeek, FourthWeek, EveryWeek. Returned by default. Query parameters are not supported. Possible values are: userDefined, firstWeek, secondWeek, thirdWeek, fourthWeek, everyWeek, unknownFutureValue.
        Returns: Optional[windows_update_for_business_update_weeks.WindowsUpdateForBusinessUpdateWeeks]
        """
        return self._update_weeks
    
    @update_weeks.setter
    def update_weeks(self,value: Optional[windows_update_for_business_update_weeks.WindowsUpdateForBusinessUpdateWeeks] = None) -> None:
        """
        Sets the updateWeeks property value. Schedule the update installation on the weeks of the month. Possible values are: UserDefined, FirstWeek, SecondWeek, ThirdWeek, FourthWeek, EveryWeek. Returned by default. Query parameters are not supported. Possible values are: userDefined, firstWeek, secondWeek, thirdWeek, fourthWeek, everyWeek, unknownFutureValue.
        Args:
            value: Value to set for the updateWeeks property.
        """
        self._update_weeks = value
    
    @property
    def user_pause_access(self,) -> Optional[enablement.Enablement]:
        """
        Gets the userPauseAccess property value. Possible values of a property
        Returns: Optional[enablement.Enablement]
        """
        return self._user_pause_access
    
    @user_pause_access.setter
    def user_pause_access(self,value: Optional[enablement.Enablement] = None) -> None:
        """
        Sets the userPauseAccess property value. Possible values of a property
        Args:
            value: Value to set for the userPauseAccess property.
        """
        self._user_pause_access = value
    
    @property
    def user_windows_update_scan_access(self,) -> Optional[enablement.Enablement]:
        """
        Gets the userWindowsUpdateScanAccess property value. Possible values of a property
        Returns: Optional[enablement.Enablement]
        """
        return self._user_windows_update_scan_access
    
    @user_windows_update_scan_access.setter
    def user_windows_update_scan_access(self,value: Optional[enablement.Enablement] = None) -> None:
        """
        Sets the userWindowsUpdateScanAccess property value. Possible values of a property
        Args:
            value: Value to set for the userWindowsUpdateScanAccess property.
        """
        self._user_windows_update_scan_access = value
    

