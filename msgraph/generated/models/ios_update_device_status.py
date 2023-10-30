from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .compliance_status import ComplianceStatus
    from .entity import Entity
    from .ios_updates_install_status import IosUpdatesInstallStatus

from .entity import Entity

@dataclass
class IosUpdateDeviceStatus(Entity):
    # The DateTime when device compliance grace period expires
    compliance_grace_period_expiration_date_time: Optional[datetime.datetime] = None
    # Device name of the DevicePolicyStatus.
    device_display_name: Optional[str] = None
    # The device id that is being reported.
    device_id: Optional[str] = None
    # The device model that is being reported
    device_model: Optional[str] = None
    # The installStatus property
    install_status: Optional[IosUpdatesInstallStatus] = None
    # Last modified date time of the policy report.
    last_reported_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The device version that is being reported.
    os_version: Optional[str] = None
    # The status property
    status: Optional[ComplianceStatus] = None
    # The User id that is being reported.
    user_id: Optional[str] = None
    # The User Name that is being reported
    user_name: Optional[str] = None
    # UserPrincipalName.
    user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IosUpdateDeviceStatus:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IosUpdateDeviceStatus
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return IosUpdateDeviceStatus()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .compliance_status import ComplianceStatus
        from .entity import Entity
        from .ios_updates_install_status import IosUpdatesInstallStatus

        from .compliance_status import ComplianceStatus
        from .entity import Entity
        from .ios_updates_install_status import IosUpdatesInstallStatus

        fields: Dict[str, Callable[[Any], None]] = {
            "compliance_grace_period_expiration_date_time": lambda n : setattr(self, 'compliance_grace_period_expiration_date_time', n.get_datetime_value()),
            "device_display_name": lambda n : setattr(self, 'device_display_name', n.get_str_value()),
            "device_id": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "device_model": lambda n : setattr(self, 'device_model', n.get_str_value()),
            "install_status": lambda n : setattr(self, 'install_status', n.get_enum_value(IosUpdatesInstallStatus)),
            "last_reported_date_time": lambda n : setattr(self, 'last_reported_date_time', n.get_datetime_value()),
            "os_version": lambda n : setattr(self, 'os_version', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(ComplianceStatus)),
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
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_datetime_value("compliance_grace_period_expiration_date_time", self.compliance_grace_period_expiration_date_time)
        writer.write_str_value("device_display_name", self.device_display_name)
        writer.write_str_value("device_id", self.device_id)
        writer.write_str_value("device_model", self.device_model)
        writer.write_enum_value("install_status", self.install_status)
        writer.write_datetime_value("last_reported_date_time", self.last_reported_date_time)
        writer.write_str_value("os_version", self.os_version)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("user_id", self.user_id)
        writer.write_str_value("user_name", self.user_name)
        writer.write_str_value("user_principal_name", self.user_principal_name)
    

