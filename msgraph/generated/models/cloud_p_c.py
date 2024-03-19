from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_pc_provisioning_type import CloudPcProvisioningType
    from .entity import Entity

from .entity import Entity

@dataclass
class CloudPC(Entity):
    # The aadDeviceId property
    aad_device_id: Optional[str] = None
    # The displayName property
    display_name: Optional[str] = None
    # The gracePeriodEndDateTime property
    grace_period_end_date_time: Optional[datetime.datetime] = None
    # The imageDisplayName property
    image_display_name: Optional[str] = None
    # The lastModifiedDateTime property
    last_modified_date_time: Optional[datetime.datetime] = None
    # The managedDeviceId property
    managed_device_id: Optional[str] = None
    # The managedDeviceName property
    managed_device_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The onPremisesConnectionName property
    on_premises_connection_name: Optional[str] = None
    # The provisioningPolicyId property
    provisioning_policy_id: Optional[str] = None
    # The provisioningPolicyName property
    provisioning_policy_name: Optional[str] = None
    # The provisioningType property
    provisioning_type: Optional[CloudPcProvisioningType] = None
    # The servicePlanId property
    service_plan_id: Optional[str] = None
    # The servicePlanName property
    service_plan_name: Optional[str] = None
    # The userPrincipalName property
    user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CloudPC:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPC
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return CloudPC()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_pc_provisioning_type import CloudPcProvisioningType
        from .entity import Entity

        from .cloud_pc_provisioning_type import CloudPcProvisioningType
        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "aadDeviceId": lambda n : setattr(self, 'aad_device_id', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "gracePeriodEndDateTime": lambda n : setattr(self, 'grace_period_end_date_time', n.get_datetime_value()),
            "imageDisplayName": lambda n : setattr(self, 'image_display_name', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "managedDeviceId": lambda n : setattr(self, 'managed_device_id', n.get_str_value()),
            "managedDeviceName": lambda n : setattr(self, 'managed_device_name', n.get_str_value()),
            "onPremisesConnectionName": lambda n : setattr(self, 'on_premises_connection_name', n.get_str_value()),
            "provisioningPolicyId": lambda n : setattr(self, 'provisioning_policy_id', n.get_str_value()),
            "provisioningPolicyName": lambda n : setattr(self, 'provisioning_policy_name', n.get_str_value()),
            "provisioningType": lambda n : setattr(self, 'provisioning_type', n.get_enum_value(CloudPcProvisioningType)),
            "servicePlanId": lambda n : setattr(self, 'service_plan_id', n.get_str_value()),
            "servicePlanName": lambda n : setattr(self, 'service_plan_name', n.get_str_value()),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("aadDeviceId", self.aad_device_id)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("gracePeriodEndDateTime", self.grace_period_end_date_time)
        writer.write_str_value("imageDisplayName", self.image_display_name)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("managedDeviceId", self.managed_device_id)
        writer.write_str_value("managedDeviceName", self.managed_device_name)
        writer.write_str_value("onPremisesConnectionName", self.on_premises_connection_name)
        writer.write_str_value("provisioningPolicyId", self.provisioning_policy_id)
        writer.write_str_value("provisioningPolicyName", self.provisioning_policy_name)
        writer.write_enum_value("provisioningType", self.provisioning_type)
        writer.write_str_value("servicePlanId", self.service_plan_id)
        writer.write_str_value("servicePlanName", self.service_plan_name)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
    

