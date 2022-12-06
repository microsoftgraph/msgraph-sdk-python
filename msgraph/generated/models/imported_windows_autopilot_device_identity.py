from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
imported_windows_autopilot_device_identity_state = lazy_import('msgraph.generated.models.imported_windows_autopilot_device_identity_state')

class ImportedWindowsAutopilotDeviceIdentity(entity.Entity):
    """
    Imported windows autopilot devices.
    """
    @property
    def assigned_user_principal_name(self,) -> Optional[str]:
        """
        Gets the assignedUserPrincipalName property value. UPN of the user the device will be assigned
        Returns: Optional[str]
        """
        return self._assigned_user_principal_name
    
    @assigned_user_principal_name.setter
    def assigned_user_principal_name(self,value: Optional[str] = None) -> None:
        """
        Sets the assignedUserPrincipalName property value. UPN of the user the device will be assigned
        Args:
            value: Value to set for the assignedUserPrincipalName property.
        """
        self._assigned_user_principal_name = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new importedWindowsAutopilotDeviceIdentity and sets the default values.
        """
        super().__init__()
        # UPN of the user the device will be assigned
        self._assigned_user_principal_name: Optional[str] = None
        # Group Tag of the Windows autopilot device.
        self._group_tag: Optional[str] = None
        # Hardware Blob of the Windows autopilot device.
        self._hardware_identifier: Optional[bytes] = None
        # The Import Id of the Windows autopilot device.
        self._import_id: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Product Key of the Windows autopilot device.
        self._product_key: Optional[str] = None
        # Serial number of the Windows autopilot device.
        self._serial_number: Optional[str] = None
        # Current state of the imported device.
        self._state: Optional[imported_windows_autopilot_device_identity_state.ImportedWindowsAutopilotDeviceIdentityState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ImportedWindowsAutopilotDeviceIdentity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ImportedWindowsAutopilotDeviceIdentity
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ImportedWindowsAutopilotDeviceIdentity()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "assigned_user_principal_name": lambda n : setattr(self, 'assigned_user_principal_name', n.get_str_value()),
            "group_tag": lambda n : setattr(self, 'group_tag', n.get_str_value()),
            "hardware_identifier": lambda n : setattr(self, 'hardware_identifier', n.get_bytes_value()),
            "import_id": lambda n : setattr(self, 'import_id', n.get_str_value()),
            "product_key": lambda n : setattr(self, 'product_key', n.get_str_value()),
            "serial_number": lambda n : setattr(self, 'serial_number', n.get_str_value()),
            "state": lambda n : setattr(self, 'state', n.get_object_value(imported_windows_autopilot_device_identity_state.ImportedWindowsAutopilotDeviceIdentityState)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def group_tag(self,) -> Optional[str]:
        """
        Gets the groupTag property value. Group Tag of the Windows autopilot device.
        Returns: Optional[str]
        """
        return self._group_tag
    
    @group_tag.setter
    def group_tag(self,value: Optional[str] = None) -> None:
        """
        Sets the groupTag property value. Group Tag of the Windows autopilot device.
        Args:
            value: Value to set for the groupTag property.
        """
        self._group_tag = value
    
    @property
    def hardware_identifier(self,) -> Optional[bytes]:
        """
        Gets the hardwareIdentifier property value. Hardware Blob of the Windows autopilot device.
        Returns: Optional[bytes]
        """
        return self._hardware_identifier
    
    @hardware_identifier.setter
    def hardware_identifier(self,value: Optional[bytes] = None) -> None:
        """
        Sets the hardwareIdentifier property value. Hardware Blob of the Windows autopilot device.
        Args:
            value: Value to set for the hardwareIdentifier property.
        """
        self._hardware_identifier = value
    
    @property
    def import_id(self,) -> Optional[str]:
        """
        Gets the importId property value. The Import Id of the Windows autopilot device.
        Returns: Optional[str]
        """
        return self._import_id
    
    @import_id.setter
    def import_id(self,value: Optional[str] = None) -> None:
        """
        Sets the importId property value. The Import Id of the Windows autopilot device.
        Args:
            value: Value to set for the importId property.
        """
        self._import_id = value
    
    @property
    def product_key(self,) -> Optional[str]:
        """
        Gets the productKey property value. Product Key of the Windows autopilot device.
        Returns: Optional[str]
        """
        return self._product_key
    
    @product_key.setter
    def product_key(self,value: Optional[str] = None) -> None:
        """
        Sets the productKey property value. Product Key of the Windows autopilot device.
        Args:
            value: Value to set for the productKey property.
        """
        self._product_key = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("assignedUserPrincipalName", self.assigned_user_principal_name)
        writer.write_str_value("groupTag", self.group_tag)
        writer.write_object_value("hardwareIdentifier", self.hardware_identifier)
        writer.write_str_value("importId", self.import_id)
        writer.write_str_value("productKey", self.product_key)
        writer.write_str_value("serialNumber", self.serial_number)
        writer.write_object_value("state", self.state)
    
    @property
    def serial_number(self,) -> Optional[str]:
        """
        Gets the serialNumber property value. Serial number of the Windows autopilot device.
        Returns: Optional[str]
        """
        return self._serial_number
    
    @serial_number.setter
    def serial_number(self,value: Optional[str] = None) -> None:
        """
        Sets the serialNumber property value. Serial number of the Windows autopilot device.
        Args:
            value: Value to set for the serialNumber property.
        """
        self._serial_number = value
    
    @property
    def state(self,) -> Optional[imported_windows_autopilot_device_identity_state.ImportedWindowsAutopilotDeviceIdentityState]:
        """
        Gets the state property value. Current state of the imported device.
        Returns: Optional[imported_windows_autopilot_device_identity_state.ImportedWindowsAutopilotDeviceIdentityState]
        """
        return self._state
    
    @state.setter
    def state(self,value: Optional[imported_windows_autopilot_device_identity_state.ImportedWindowsAutopilotDeviceIdentityState] = None) -> None:
        """
        Sets the state property value. Current state of the imported device.
        Args:
            value: Value to set for the state property.
        """
        self._state = value
    

