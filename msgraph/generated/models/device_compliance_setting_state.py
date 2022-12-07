from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

compliance_status = lazy_import('msgraph.generated.models.compliance_status')
entity = lazy_import('msgraph.generated.models.entity')

class DeviceComplianceSettingState(entity.Entity):
    """
    Device compliance setting State for a given device.
    """
    @property
    def compliance_grace_period_expiration_date_time(self,) -> Optional[datetime]:
        """
        Gets the complianceGracePeriodExpirationDateTime property value. The DateTime when device compliance grace period expires
        Returns: Optional[datetime]
        """
        return self._compliance_grace_period_expiration_date_time
    
    @compliance_grace_period_expiration_date_time.setter
    def compliance_grace_period_expiration_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the complianceGracePeriodExpirationDateTime property value. The DateTime when device compliance grace period expires
        Args:
            value: Value to set for the complianceGracePeriodExpirationDateTime property.
        """
        self._compliance_grace_period_expiration_date_time = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new deviceComplianceSettingState and sets the default values.
        """
        super().__init__()
        # The DateTime when device compliance grace period expires
        self._compliance_grace_period_expiration_date_time: Optional[datetime] = None
        # The Device Id that is being reported
        self._device_id: Optional[str] = None
        # The device model that is being reported
        self._device_model: Optional[str] = None
        # The Device Name that is being reported
        self._device_name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The setting class name and property name.
        self._setting: Optional[str] = None
        # The Setting Name that is being reported
        self._setting_name: Optional[str] = None
        # The state property
        self._state: Optional[compliance_status.ComplianceStatus] = None
        # The User email address that is being reported
        self._user_email: Optional[str] = None
        # The user Id that is being reported
        self._user_id: Optional[str] = None
        # The User Name that is being reported
        self._user_name: Optional[str] = None
        # The User PrincipalName that is being reported
        self._user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceComplianceSettingState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceComplianceSettingState
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceComplianceSettingState()
    
    @property
    def device_id(self,) -> Optional[str]:
        """
        Gets the deviceId property value. The Device Id that is being reported
        Returns: Optional[str]
        """
        return self._device_id
    
    @device_id.setter
    def device_id(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceId property value. The Device Id that is being reported
        Args:
            value: Value to set for the deviceId property.
        """
        self._device_id = value
    
    @property
    def device_model(self,) -> Optional[str]:
        """
        Gets the deviceModel property value. The device model that is being reported
        Returns: Optional[str]
        """
        return self._device_model
    
    @device_model.setter
    def device_model(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceModel property value. The device model that is being reported
        Args:
            value: Value to set for the deviceModel property.
        """
        self._device_model = value
    
    @property
    def device_name(self,) -> Optional[str]:
        """
        Gets the deviceName property value. The Device Name that is being reported
        Returns: Optional[str]
        """
        return self._device_name
    
    @device_name.setter
    def device_name(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceName property value. The Device Name that is being reported
        Args:
            value: Value to set for the deviceName property.
        """
        self._device_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "compliance_grace_period_expiration_date_time": lambda n : setattr(self, 'compliance_grace_period_expiration_date_time', n.get_datetime_value()),
            "device_id": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "device_model": lambda n : setattr(self, 'device_model', n.get_str_value()),
            "device_name": lambda n : setattr(self, 'device_name', n.get_str_value()),
            "setting": lambda n : setattr(self, 'setting', n.get_str_value()),
            "setting_name": lambda n : setattr(self, 'setting_name', n.get_str_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(compliance_status.ComplianceStatus)),
            "user_email": lambda n : setattr(self, 'user_email', n.get_str_value()),
            "user_id": lambda n : setattr(self, 'user_id', n.get_str_value()),
            "user_name": lambda n : setattr(self, 'user_name', n.get_str_value()),
            "user_principal_name": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_datetime_value("complianceGracePeriodExpirationDateTime", self.compliance_grace_period_expiration_date_time)
        writer.write_str_value("deviceId", self.device_id)
        writer.write_str_value("deviceModel", self.device_model)
        writer.write_str_value("deviceName", self.device_name)
        writer.write_str_value("setting", self.setting)
        writer.write_str_value("settingName", self.setting_name)
        writer.write_enum_value("state", self.state)
        writer.write_str_value("userEmail", self.user_email)
        writer.write_str_value("userId", self.user_id)
        writer.write_str_value("userName", self.user_name)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
    
    @property
    def setting(self,) -> Optional[str]:
        """
        Gets the setting property value. The setting class name and property name.
        Returns: Optional[str]
        """
        return self._setting
    
    @setting.setter
    def setting(self,value: Optional[str] = None) -> None:
        """
        Sets the setting property value. The setting class name and property name.
        Args:
            value: Value to set for the setting property.
        """
        self._setting = value
    
    @property
    def setting_name(self,) -> Optional[str]:
        """
        Gets the settingName property value. The Setting Name that is being reported
        Returns: Optional[str]
        """
        return self._setting_name
    
    @setting_name.setter
    def setting_name(self,value: Optional[str] = None) -> None:
        """
        Sets the settingName property value. The Setting Name that is being reported
        Args:
            value: Value to set for the settingName property.
        """
        self._setting_name = value
    
    @property
    def state(self,) -> Optional[compliance_status.ComplianceStatus]:
        """
        Gets the state property value. The state property
        Returns: Optional[compliance_status.ComplianceStatus]
        """
        return self._state
    
    @state.setter
    def state(self,value: Optional[compliance_status.ComplianceStatus] = None) -> None:
        """
        Sets the state property value. The state property
        Args:
            value: Value to set for the state property.
        """
        self._state = value
    
    @property
    def user_email(self,) -> Optional[str]:
        """
        Gets the userEmail property value. The User email address that is being reported
        Returns: Optional[str]
        """
        return self._user_email
    
    @user_email.setter
    def user_email(self,value: Optional[str] = None) -> None:
        """
        Sets the userEmail property value. The User email address that is being reported
        Args:
            value: Value to set for the userEmail property.
        """
        self._user_email = value
    
    @property
    def user_id(self,) -> Optional[str]:
        """
        Gets the userId property value. The user Id that is being reported
        Returns: Optional[str]
        """
        return self._user_id
    
    @user_id.setter
    def user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the userId property value. The user Id that is being reported
        Args:
            value: Value to set for the userId property.
        """
        self._user_id = value
    
    @property
    def user_name(self,) -> Optional[str]:
        """
        Gets the userName property value. The User Name that is being reported
        Returns: Optional[str]
        """
        return self._user_name
    
    @user_name.setter
    def user_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userName property value. The User Name that is being reported
        Args:
            value: Value to set for the userName property.
        """
        self._user_name = value
    
    @property
    def user_principal_name(self,) -> Optional[str]:
        """
        Gets the userPrincipalName property value. The User PrincipalName that is being reported
        Returns: Optional[str]
        """
        return self._user_principal_name
    
    @user_principal_name.setter
    def user_principal_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userPrincipalName property value. The User PrincipalName that is being reported
        Args:
            value: Value to set for the userPrincipalName property.
        """
        self._user_principal_name = value
    

