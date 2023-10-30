from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .enrollment_state import EnrollmentState
    from .entity import Entity

from .entity import Entity

@dataclass
class WindowsAutopilotDeviceIdentity(Entity):
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsAutopilotDeviceIdentity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsAutopilotDeviceIdentity
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return WindowsAutopilotDeviceIdentity()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .enrollment_state import EnrollmentState
        from .entity import Entity

        from .enrollment_state import EnrollmentState
        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "addressable_user_name": lambda n : setattr(self, 'addressable_user_name', n.get_str_value()),
            "azure_active_directory_device_id": lambda n : setattr(self, 'azure_active_directory_device_id', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "enrollment_state": lambda n : setattr(self, 'enrollment_state', n.get_enum_value(EnrollmentState)),
            "group_tag": lambda n : setattr(self, 'group_tag', n.get_str_value()),
            "last_contacted_date_time": lambda n : setattr(self, 'last_contacted_date_time', n.get_datetime_value()),
            "managed_device_id": lambda n : setattr(self, 'managed_device_id', n.get_str_value()),
            "manufacturer": lambda n : setattr(self, 'manufacturer', n.get_str_value()),
            "model": lambda n : setattr(self, 'model', n.get_str_value()),
            "product_key": lambda n : setattr(self, 'product_key', n.get_str_value()),
            "purchase_order_identifier": lambda n : setattr(self, 'purchase_order_identifier', n.get_str_value()),
            "resource_name": lambda n : setattr(self, 'resource_name', n.get_str_value()),
            "serial_number": lambda n : setattr(self, 'serial_number', n.get_str_value()),
            "sku_number": lambda n : setattr(self, 'sku_number', n.get_str_value()),
            "system_family": lambda n : setattr(self, 'system_family', n.get_str_value()),
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
        writer.write_str_value("addressable_user_name", self.addressable_user_name)
        writer.write_str_value("azure_active_directory_device_id", self.azure_active_directory_device_id)
        writer.write_str_value("display_name", self.display_name)
        writer.write_enum_value("enrollment_state", self.enrollment_state)
        writer.write_str_value("group_tag", self.group_tag)
        writer.write_datetime_value("last_contacted_date_time", self.last_contacted_date_time)
        writer.write_str_value("managed_device_id", self.managed_device_id)
        writer.write_str_value("manufacturer", self.manufacturer)
        writer.write_str_value("model", self.model)
        writer.write_str_value("product_key", self.product_key)
        writer.write_str_value("purchase_order_identifier", self.purchase_order_identifier)
        writer.write_str_value("resource_name", self.resource_name)
        writer.write_str_value("serial_number", self.serial_number)
        writer.write_str_value("sku_number", self.sku_number)
        writer.write_str_value("system_family", self.system_family)
        writer.write_str_value("user_principal_name", self.user_principal_name)
    

