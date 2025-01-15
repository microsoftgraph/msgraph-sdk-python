from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .compliance_status import ComplianceStatus
    from .entity import Entity

from .entity import Entity

@dataclass
class DeviceComplianceSettingState(Entity, Parsable):
    """
    Device compliance setting State for a given device.
    """
    # The DateTime when device compliance grace period expires
    compliance_grace_period_expiration_date_time: Optional[datetime.datetime] = None
    # The Device Id that is being reported
    device_id: Optional[str] = None
    # The device model that is being reported
    device_model: Optional[str] = None
    # The Device Name that is being reported
    device_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The setting class name and property name.
    setting: Optional[str] = None
    # The Setting Name that is being reported
    setting_name: Optional[str] = None
    # The state property
    state: Optional[ComplianceStatus] = None
    # The User email address that is being reported
    user_email: Optional[str] = None
    # The user Id that is being reported
    user_id: Optional[str] = None
    # The User Name that is being reported
    user_name: Optional[str] = None
    # The User PrincipalName that is being reported
    user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceComplianceSettingState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceComplianceSettingState
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceComplianceSettingState()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .compliance_status import ComplianceStatus
        from .entity import Entity

        from .compliance_status import ComplianceStatus
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "complianceGracePeriodExpirationDateTime": lambda n : setattr(self, 'compliance_grace_period_expiration_date_time', n.get_datetime_value()),
            "deviceId": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "deviceModel": lambda n : setattr(self, 'device_model', n.get_str_value()),
            "deviceName": lambda n : setattr(self, 'device_name', n.get_str_value()),
            "setting": lambda n : setattr(self, 'setting', n.get_str_value()),
            "settingName": lambda n : setattr(self, 'setting_name', n.get_str_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(ComplianceStatus)),
            "userEmail": lambda n : setattr(self, 'user_email', n.get_str_value()),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
            "userName": lambda n : setattr(self, 'user_name', n.get_str_value()),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
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
        if writer is None:
            raise TypeError("writer cannot be null.")
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
    

