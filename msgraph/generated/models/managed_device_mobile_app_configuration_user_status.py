from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .compliance_status import ComplianceStatus
    from .entity import Entity

from .entity import Entity

@dataclass
class ManagedDeviceMobileAppConfigurationUserStatus(Entity, Parsable):
    """
    Contains properties, inherited properties and actions for an MDM mobile app configuration status for a user.
    """
    # Devices count for that user.
    devices_count: Optional[int] = None
    # Last modified date time of the policy report.
    last_reported_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The status property
    status: Optional[ComplianceStatus] = None
    # User name of the DevicePolicyStatus.
    user_display_name: Optional[str] = None
    # UserPrincipalName.
    user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ManagedDeviceMobileAppConfigurationUserStatus:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ManagedDeviceMobileAppConfigurationUserStatus
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ManagedDeviceMobileAppConfigurationUserStatus()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .compliance_status import ComplianceStatus
        from .entity import Entity

        from .compliance_status import ComplianceStatus
        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "devicesCount": lambda n : setattr(self, 'devices_count', n.get_int_value()),
            "lastReportedDateTime": lambda n : setattr(self, 'last_reported_date_time', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(ComplianceStatus)),
            "userDisplayName": lambda n : setattr(self, 'user_display_name', n.get_str_value()),
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
        from .compliance_status import ComplianceStatus
        from .entity import Entity

        writer.write_int_value("devicesCount", self.devices_count)
        writer.write_datetime_value("lastReportedDateTime", self.last_reported_date_time)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("userDisplayName", self.user_display_name)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
    

