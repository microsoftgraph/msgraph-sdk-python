from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .enrollment_state import EnrollmentState
    from .entity import Entity

from .entity import Entity

@dataclass
class WindowsAutopilotDeviceIdentity(Entity, Parsable):
    """
    The windowsAutopilotDeviceIdentity resource represents a Windows Autopilot Device.
    """
    # Addressable user name.
    addressable_user_name: Optional[str] = None
    # AAD Device ID - to be deprecated
    azure_active_directory_device_id: Optional[str] = None
    # Display Name
    display_name: Optional[str] = None
    # The enrollmentState property
    enrollment_state: Optional[EnrollmentState] = None
    # Group Tag of the Windows autopilot device.
    group_tag: Optional[str] = None
    # Intune Last Contacted Date Time of the Windows autopilot device.
    last_contacted_date_time: Optional[datetime.datetime] = None
    # Managed Device ID
    managed_device_id: Optional[str] = None
    # Oem manufacturer of the Windows autopilot device.
    manufacturer: Optional[str] = None
    # Model name of the Windows autopilot device.
    model: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Product Key of the Windows autopilot device.
    product_key: Optional[str] = None
    # Purchase Order Identifier of the Windows autopilot device.
    purchase_order_identifier: Optional[str] = None
    # Resource Name.
    resource_name: Optional[str] = None
    # Serial number of the Windows autopilot device.
    serial_number: Optional[str] = None
    # SKU Number
    sku_number: Optional[str] = None
    # System Family
    system_family: Optional[str] = None
    # User Principal Name.
    user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WindowsAutopilotDeviceIdentity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsAutopilotDeviceIdentity
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WindowsAutopilotDeviceIdentity()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .enrollment_state import EnrollmentState
        from .entity import Entity

        from .enrollment_state import EnrollmentState
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "addressableUserName": lambda n : setattr(self, 'addressable_user_name', n.get_str_value()),
            "azureActiveDirectoryDeviceId": lambda n : setattr(self, 'azure_active_directory_device_id', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "enrollmentState": lambda n : setattr(self, 'enrollment_state', n.get_enum_value(EnrollmentState)),
            "groupTag": lambda n : setattr(self, 'group_tag', n.get_str_value()),
            "lastContactedDateTime": lambda n : setattr(self, 'last_contacted_date_time', n.get_datetime_value()),
            "managedDeviceId": lambda n : setattr(self, 'managed_device_id', n.get_str_value()),
            "manufacturer": lambda n : setattr(self, 'manufacturer', n.get_str_value()),
            "model": lambda n : setattr(self, 'model', n.get_str_value()),
            "productKey": lambda n : setattr(self, 'product_key', n.get_str_value()),
            "purchaseOrderIdentifier": lambda n : setattr(self, 'purchase_order_identifier', n.get_str_value()),
            "resourceName": lambda n : setattr(self, 'resource_name', n.get_str_value()),
            "serialNumber": lambda n : setattr(self, 'serial_number', n.get_str_value()),
            "skuNumber": lambda n : setattr(self, 'sku_number', n.get_str_value()),
            "systemFamily": lambda n : setattr(self, 'system_family', n.get_str_value()),
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
        writer.write_str_value("addressableUserName", self.addressable_user_name)
        writer.write_str_value("azureActiveDirectoryDeviceId", self.azure_active_directory_device_id)
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("enrollmentState", self.enrollment_state)
        writer.write_str_value("groupTag", self.group_tag)
        writer.write_datetime_value("lastContactedDateTime", self.last_contacted_date_time)
        writer.write_str_value("managedDeviceId", self.managed_device_id)
        writer.write_str_value("manufacturer", self.manufacturer)
        writer.write_str_value("model", self.model)
        writer.write_str_value("productKey", self.product_key)
        writer.write_str_value("purchaseOrderIdentifier", self.purchase_order_identifier)
        writer.write_str_value("resourceName", self.resource_name)
        writer.write_str_value("serialNumber", self.serial_number)
        writer.write_str_value("skuNumber", self.sku_number)
        writer.write_str_value("systemFamily", self.system_family)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
    

