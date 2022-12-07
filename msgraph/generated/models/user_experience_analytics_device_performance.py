from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

disk_type = lazy_import('msgraph.generated.models.disk_type')
entity = lazy_import('msgraph.generated.models.entity')
user_experience_analytics_health_state = lazy_import('msgraph.generated.models.user_experience_analytics_health_state')

class UserExperienceAnalyticsDevicePerformance(entity.Entity):
    @property
    def average_blue_screens(self,) -> Optional[float]:
        """
        Gets the averageBlueScreens property value. Average (mean) number of Blue Screens per device in the last 30 days. Valid values 0 to 9999999
        Returns: Optional[float]
        """
        return self._average_blue_screens
    
    @average_blue_screens.setter
    def average_blue_screens(self,value: Optional[float] = None) -> None:
        """
        Sets the averageBlueScreens property value. Average (mean) number of Blue Screens per device in the last 30 days. Valid values 0 to 9999999
        Args:
            value: Value to set for the averageBlueScreens property.
        """
        self._average_blue_screens = value
    
    @property
    def average_restarts(self,) -> Optional[float]:
        """
        Gets the averageRestarts property value. Average (mean) number of Restarts per device in the last 30 days. Valid values 0 to 9999999
        Returns: Optional[float]
        """
        return self._average_restarts
    
    @average_restarts.setter
    def average_restarts(self,value: Optional[float] = None) -> None:
        """
        Sets the averageRestarts property value. Average (mean) number of Restarts per device in the last 30 days. Valid values 0 to 9999999
        Args:
            value: Value to set for the averageRestarts property.
        """
        self._average_restarts = value
    
    @property
    def blue_screen_count(self,) -> Optional[int]:
        """
        Gets the blueScreenCount property value. Number of Blue Screens in the last 30 days. Valid values 0 to 9999999
        Returns: Optional[int]
        """
        return self._blue_screen_count
    
    @blue_screen_count.setter
    def blue_screen_count(self,value: Optional[int] = None) -> None:
        """
        Sets the blueScreenCount property value. Number of Blue Screens in the last 30 days. Valid values 0 to 9999999
        Args:
            value: Value to set for the blueScreenCount property.
        """
        self._blue_screen_count = value
    
    @property
    def boot_score(self,) -> Optional[int]:
        """
        Gets the bootScore property value. The user experience analytics device boot score.
        Returns: Optional[int]
        """
        return self._boot_score
    
    @boot_score.setter
    def boot_score(self,value: Optional[int] = None) -> None:
        """
        Sets the bootScore property value. The user experience analytics device boot score.
        Args:
            value: Value to set for the bootScore property.
        """
        self._boot_score = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new UserExperienceAnalyticsDevicePerformance and sets the default values.
        """
        super().__init__()
        # Average (mean) number of Blue Screens per device in the last 30 days. Valid values 0 to 9999999
        self._average_blue_screens: Optional[float] = None
        # Average (mean) number of Restarts per device in the last 30 days. Valid values 0 to 9999999
        self._average_restarts: Optional[float] = None
        # Number of Blue Screens in the last 30 days. Valid values 0 to 9999999
        self._blue_screen_count: Optional[int] = None
        # The user experience analytics device boot score.
        self._boot_score: Optional[int] = None
        # The user experience analytics device core boot time in milliseconds.
        self._core_boot_time_in_ms: Optional[int] = None
        # The user experience analytics device core login time in milliseconds.
        self._core_login_time_in_ms: Optional[int] = None
        # User experience analytics summarized device count.
        self._device_count: Optional[int] = None
        # The user experience analytics device name.
        self._device_name: Optional[str] = None
        # The diskType property
        self._disk_type: Optional[disk_type.DiskType] = None
        # The user experience analytics device group policy boot time in milliseconds.
        self._group_policy_boot_time_in_ms: Optional[int] = None
        # The user experience analytics device group policy login time in milliseconds.
        self._group_policy_login_time_in_ms: Optional[int] = None
        # The healthStatus property
        self._health_status: Optional[user_experience_analytics_health_state.UserExperienceAnalyticsHealthState] = None
        # The user experience analytics device login score.
        self._login_score: Optional[int] = None
        # The user experience analytics device manufacturer.
        self._manufacturer: Optional[str] = None
        # The user experience analytics device model.
        self._model: Optional[str] = None
        # The user experience analytics model level startup performance score. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        self._model_startup_performance_score: Optional[float] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The user experience analytics device Operating System version.
        self._operating_system_version: Optional[str] = None
        # The user experience analytics responsive desktop time in milliseconds.
        self._responsive_desktop_time_in_ms: Optional[int] = None
        # Number of Restarts in the last 30 days. Valid values 0 to 9999999
        self._restart_count: Optional[int] = None
        # The user experience analytics device startup performance score. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        self._startup_performance_score: Optional[float] = None
    
    @property
    def core_boot_time_in_ms(self,) -> Optional[int]:
        """
        Gets the coreBootTimeInMs property value. The user experience analytics device core boot time in milliseconds.
        Returns: Optional[int]
        """
        return self._core_boot_time_in_ms
    
    @core_boot_time_in_ms.setter
    def core_boot_time_in_ms(self,value: Optional[int] = None) -> None:
        """
        Sets the coreBootTimeInMs property value. The user experience analytics device core boot time in milliseconds.
        Args:
            value: Value to set for the coreBootTimeInMs property.
        """
        self._core_boot_time_in_ms = value
    
    @property
    def core_login_time_in_ms(self,) -> Optional[int]:
        """
        Gets the coreLoginTimeInMs property value. The user experience analytics device core login time in milliseconds.
        Returns: Optional[int]
        """
        return self._core_login_time_in_ms
    
    @core_login_time_in_ms.setter
    def core_login_time_in_ms(self,value: Optional[int] = None) -> None:
        """
        Sets the coreLoginTimeInMs property value. The user experience analytics device core login time in milliseconds.
        Args:
            value: Value to set for the coreLoginTimeInMs property.
        """
        self._core_login_time_in_ms = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserExperienceAnalyticsDevicePerformance:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsDevicePerformance
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserExperienceAnalyticsDevicePerformance()
    
    @property
    def device_count(self,) -> Optional[int]:
        """
        Gets the deviceCount property value. User experience analytics summarized device count.
        Returns: Optional[int]
        """
        return self._device_count
    
    @device_count.setter
    def device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the deviceCount property value. User experience analytics summarized device count.
        Args:
            value: Value to set for the deviceCount property.
        """
        self._device_count = value
    
    @property
    def device_name(self,) -> Optional[str]:
        """
        Gets the deviceName property value. The user experience analytics device name.
        Returns: Optional[str]
        """
        return self._device_name
    
    @device_name.setter
    def device_name(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceName property value. The user experience analytics device name.
        Args:
            value: Value to set for the deviceName property.
        """
        self._device_name = value
    
    @property
    def disk_type(self,) -> Optional[disk_type.DiskType]:
        """
        Gets the diskType property value. The diskType property
        Returns: Optional[disk_type.DiskType]
        """
        return self._disk_type
    
    @disk_type.setter
    def disk_type(self,value: Optional[disk_type.DiskType] = None) -> None:
        """
        Sets the diskType property value. The diskType property
        Args:
            value: Value to set for the diskType property.
        """
        self._disk_type = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "average_blue_screens": lambda n : setattr(self, 'average_blue_screens', n.get_float_value()),
            "average_restarts": lambda n : setattr(self, 'average_restarts', n.get_float_value()),
            "blue_screen_count": lambda n : setattr(self, 'blue_screen_count', n.get_int_value()),
            "boot_score": lambda n : setattr(self, 'boot_score', n.get_int_value()),
            "core_boot_time_in_ms": lambda n : setattr(self, 'core_boot_time_in_ms', n.get_int_value()),
            "core_login_time_in_ms": lambda n : setattr(self, 'core_login_time_in_ms', n.get_int_value()),
            "device_count": lambda n : setattr(self, 'device_count', n.get_int_value()),
            "device_name": lambda n : setattr(self, 'device_name', n.get_str_value()),
            "disk_type": lambda n : setattr(self, 'disk_type', n.get_enum_value(disk_type.DiskType)),
            "group_policy_boot_time_in_ms": lambda n : setattr(self, 'group_policy_boot_time_in_ms', n.get_int_value()),
            "group_policy_login_time_in_ms": lambda n : setattr(self, 'group_policy_login_time_in_ms', n.get_int_value()),
            "health_status": lambda n : setattr(self, 'health_status', n.get_enum_value(user_experience_analytics_health_state.UserExperienceAnalyticsHealthState)),
            "login_score": lambda n : setattr(self, 'login_score', n.get_int_value()),
            "manufacturer": lambda n : setattr(self, 'manufacturer', n.get_str_value()),
            "model": lambda n : setattr(self, 'model', n.get_str_value()),
            "model_startup_performance_score": lambda n : setattr(self, 'model_startup_performance_score', n.get_float_value()),
            "operating_system_version": lambda n : setattr(self, 'operating_system_version', n.get_str_value()),
            "responsive_desktop_time_in_ms": lambda n : setattr(self, 'responsive_desktop_time_in_ms', n.get_int_value()),
            "restart_count": lambda n : setattr(self, 'restart_count', n.get_int_value()),
            "startup_performance_score": lambda n : setattr(self, 'startup_performance_score', n.get_float_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def group_policy_boot_time_in_ms(self,) -> Optional[int]:
        """
        Gets the groupPolicyBootTimeInMs property value. The user experience analytics device group policy boot time in milliseconds.
        Returns: Optional[int]
        """
        return self._group_policy_boot_time_in_ms
    
    @group_policy_boot_time_in_ms.setter
    def group_policy_boot_time_in_ms(self,value: Optional[int] = None) -> None:
        """
        Sets the groupPolicyBootTimeInMs property value. The user experience analytics device group policy boot time in milliseconds.
        Args:
            value: Value to set for the groupPolicyBootTimeInMs property.
        """
        self._group_policy_boot_time_in_ms = value
    
    @property
    def group_policy_login_time_in_ms(self,) -> Optional[int]:
        """
        Gets the groupPolicyLoginTimeInMs property value. The user experience analytics device group policy login time in milliseconds.
        Returns: Optional[int]
        """
        return self._group_policy_login_time_in_ms
    
    @group_policy_login_time_in_ms.setter
    def group_policy_login_time_in_ms(self,value: Optional[int] = None) -> None:
        """
        Sets the groupPolicyLoginTimeInMs property value. The user experience analytics device group policy login time in milliseconds.
        Args:
            value: Value to set for the groupPolicyLoginTimeInMs property.
        """
        self._group_policy_login_time_in_ms = value
    
    @property
    def health_status(self,) -> Optional[user_experience_analytics_health_state.UserExperienceAnalyticsHealthState]:
        """
        Gets the healthStatus property value. The healthStatus property
        Returns: Optional[user_experience_analytics_health_state.UserExperienceAnalyticsHealthState]
        """
        return self._health_status
    
    @health_status.setter
    def health_status(self,value: Optional[user_experience_analytics_health_state.UserExperienceAnalyticsHealthState] = None) -> None:
        """
        Sets the healthStatus property value. The healthStatus property
        Args:
            value: Value to set for the healthStatus property.
        """
        self._health_status = value
    
    @property
    def login_score(self,) -> Optional[int]:
        """
        Gets the loginScore property value. The user experience analytics device login score.
        Returns: Optional[int]
        """
        return self._login_score
    
    @login_score.setter
    def login_score(self,value: Optional[int] = None) -> None:
        """
        Sets the loginScore property value. The user experience analytics device login score.
        Args:
            value: Value to set for the loginScore property.
        """
        self._login_score = value
    
    @property
    def manufacturer(self,) -> Optional[str]:
        """
        Gets the manufacturer property value. The user experience analytics device manufacturer.
        Returns: Optional[str]
        """
        return self._manufacturer
    
    @manufacturer.setter
    def manufacturer(self,value: Optional[str] = None) -> None:
        """
        Sets the manufacturer property value. The user experience analytics device manufacturer.
        Args:
            value: Value to set for the manufacturer property.
        """
        self._manufacturer = value
    
    @property
    def model(self,) -> Optional[str]:
        """
        Gets the model property value. The user experience analytics device model.
        Returns: Optional[str]
        """
        return self._model
    
    @model.setter
    def model(self,value: Optional[str] = None) -> None:
        """
        Sets the model property value. The user experience analytics device model.
        Args:
            value: Value to set for the model property.
        """
        self._model = value
    
    @property
    def model_startup_performance_score(self,) -> Optional[float]:
        """
        Gets the modelStartupPerformanceScore property value. The user experience analytics model level startup performance score. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        Returns: Optional[float]
        """
        return self._model_startup_performance_score
    
    @model_startup_performance_score.setter
    def model_startup_performance_score(self,value: Optional[float] = None) -> None:
        """
        Sets the modelStartupPerformanceScore property value. The user experience analytics model level startup performance score. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        Args:
            value: Value to set for the modelStartupPerformanceScore property.
        """
        self._model_startup_performance_score = value
    
    @property
    def operating_system_version(self,) -> Optional[str]:
        """
        Gets the operatingSystemVersion property value. The user experience analytics device Operating System version.
        Returns: Optional[str]
        """
        return self._operating_system_version
    
    @operating_system_version.setter
    def operating_system_version(self,value: Optional[str] = None) -> None:
        """
        Sets the operatingSystemVersion property value. The user experience analytics device Operating System version.
        Args:
            value: Value to set for the operatingSystemVersion property.
        """
        self._operating_system_version = value
    
    @property
    def responsive_desktop_time_in_ms(self,) -> Optional[int]:
        """
        Gets the responsiveDesktopTimeInMs property value. The user experience analytics responsive desktop time in milliseconds.
        Returns: Optional[int]
        """
        return self._responsive_desktop_time_in_ms
    
    @responsive_desktop_time_in_ms.setter
    def responsive_desktop_time_in_ms(self,value: Optional[int] = None) -> None:
        """
        Sets the responsiveDesktopTimeInMs property value. The user experience analytics responsive desktop time in milliseconds.
        Args:
            value: Value to set for the responsiveDesktopTimeInMs property.
        """
        self._responsive_desktop_time_in_ms = value
    
    @property
    def restart_count(self,) -> Optional[int]:
        """
        Gets the restartCount property value. Number of Restarts in the last 30 days. Valid values 0 to 9999999
        Returns: Optional[int]
        """
        return self._restart_count
    
    @restart_count.setter
    def restart_count(self,value: Optional[int] = None) -> None:
        """
        Sets the restartCount property value. Number of Restarts in the last 30 days. Valid values 0 to 9999999
        Args:
            value: Value to set for the restartCount property.
        """
        self._restart_count = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_float_value("averageBlueScreens", self.average_blue_screens)
        writer.write_float_value("averageRestarts", self.average_restarts)
        writer.write_int_value("blueScreenCount", self.blue_screen_count)
        writer.write_int_value("bootScore", self.boot_score)
        writer.write_int_value("coreBootTimeInMs", self.core_boot_time_in_ms)
        writer.write_int_value("coreLoginTimeInMs", self.core_login_time_in_ms)
        writer.write_int_value("deviceCount", self.device_count)
        writer.write_str_value("deviceName", self.device_name)
        writer.write_enum_value("diskType", self.disk_type)
        writer.write_int_value("groupPolicyBootTimeInMs", self.group_policy_boot_time_in_ms)
        writer.write_int_value("groupPolicyLoginTimeInMs", self.group_policy_login_time_in_ms)
        writer.write_enum_value("healthStatus", self.health_status)
        writer.write_int_value("loginScore", self.login_score)
        writer.write_str_value("manufacturer", self.manufacturer)
        writer.write_str_value("model", self.model)
        writer.write_float_value("modelStartupPerformanceScore", self.model_startup_performance_score)
        writer.write_str_value("operatingSystemVersion", self.operating_system_version)
        writer.write_int_value("responsiveDesktopTimeInMs", self.responsive_desktop_time_in_ms)
        writer.write_int_value("restartCount", self.restart_count)
        writer.write_float_value("startupPerformanceScore", self.startup_performance_score)
    
    @property
    def startup_performance_score(self,) -> Optional[float]:
        """
        Gets the startupPerformanceScore property value. The user experience analytics device startup performance score. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        Returns: Optional[float]
        """
        return self._startup_performance_score
    
    @startup_performance_score.setter
    def startup_performance_score(self,value: Optional[float] = None) -> None:
        """
        Sets the startupPerformanceScore property value. The user experience analytics device startup performance score. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
        Args:
            value: Value to set for the startupPerformanceScore property.
        """
        self._startup_performance_score = value
    

