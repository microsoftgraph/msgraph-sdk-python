from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .imported_windows_autopilot_device_identity_state import ImportedWindowsAutopilotDeviceIdentityState

from .entity import Entity

@dataclass
class ImportedWindowsAutopilotDeviceIdentity(Entity, Parsable):
    """
    Imported windows autopilot devices.
    """
    # UPN of the user the device will be assigned
    assigned_user_principal_name: Optional[str] = None
    # Group Tag of the Windows autopilot device.
    group_tag: Optional[str] = None
    # Hardware Blob of the Windows autopilot device.
    hardware_identifier: Optional[bytes] = None
    # The Import Id of the Windows autopilot device.
    import_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Product Key of the Windows autopilot device.
    product_key: Optional[str] = None
    # Serial number of the Windows autopilot device.
    serial_number: Optional[str] = None
    # Current state of the imported device.
    state: Optional[ImportedWindowsAutopilotDeviceIdentityState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ImportedWindowsAutopilotDeviceIdentity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ImportedWindowsAutopilotDeviceIdentity
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ImportedWindowsAutopilotDeviceIdentity()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .imported_windows_autopilot_device_identity_state import ImportedWindowsAutopilotDeviceIdentityState

        from .entity import Entity
        from .imported_windows_autopilot_device_identity_state import ImportedWindowsAutopilotDeviceIdentityState

        fields: dict[str, Callable[[Any], None]] = {
            "assignedUserPrincipalName": lambda n : setattr(self, 'assigned_user_principal_name', n.get_str_value()),
            "groupTag": lambda n : setattr(self, 'group_tag', n.get_str_value()),
            "hardwareIdentifier": lambda n : setattr(self, 'hardware_identifier', n.get_bytes_value()),
            "importId": lambda n : setattr(self, 'import_id', n.get_str_value()),
            "productKey": lambda n : setattr(self, 'product_key', n.get_str_value()),
            "serialNumber": lambda n : setattr(self, 'serial_number', n.get_str_value()),
            "state": lambda n : setattr(self, 'state', n.get_object_value(ImportedWindowsAutopilotDeviceIdentityState)),
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
        writer.write_str_value("assignedUserPrincipalName", self.assigned_user_principal_name)
        writer.write_str_value("groupTag", self.group_tag)
        writer.write_bytes_value("hardwareIdentifier", self.hardware_identifier)
        writer.write_str_value("importId", self.import_id)
        writer.write_str_value("productKey", self.product_key)
        writer.write_str_value("serialNumber", self.serial_number)
        writer.write_object_value("state", self.state)
    

