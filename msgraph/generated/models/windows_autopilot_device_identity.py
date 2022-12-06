from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

enrollment_state = lazy_import('msgraph.generated.models.enrollment_state')
entity = lazy_import('msgraph.generated.models.entity')

class WindowsAutopilotDeviceIdentity(entity.Entity):
    """
    The windowsAutopilotDeviceIdentity resource represents a Windows Autopilot Device.
    """
    @property
    def addressable_user_name(self,) -> Optional[str]:
        """
        Gets the addressableUserName property value. Addressable user name.
        Returns: Optional[str]
        """
        return self._addressable_user_name
    
    @addressable_user_name.setter
    def addressable_user_name(self,value: Optional[str] = None) -> None:
        """
        Sets the addressableUserName property value. Addressable user name.
        Args:
            value: Value to set for the addressableUserName property.
        """
        self._addressable_user_name = value
    
    @property
    def azure_active_directory_device_id(self,) -> Optional[str]:
        """
        Gets the azureActiveDirectoryDeviceId property value. AAD Device ID - to be deprecated
        Returns: Optional[str]
        """
        return self._azure_active_directory_device_id
    
    @azure_active_directory_device_id.setter
    def azure_active_directory_device_id(self,value: Optional[str] = None) -> None:
        """
        Sets the azureActiveDirectoryDeviceId property value. AAD Device ID - to be deprecated
        Args:
            value: Value to set for the azureActiveDirectoryDeviceId property.
        """
        self._azure_active_directory_device_id = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new windowsAutopilotDeviceIdentity and sets the default values.
        """
        super().__init__()
        # Addressable user name.
        self._addressable_user_name: Optional[str] = None
        # AAD Device ID - to be deprecated
        self._azure_active_directory_device_id: Optional[str] = None
        # Display Name
        self._display_name: Optional[str] = None
        # The enrollmentState property
        self._enrollment_state: Optional[enrollment_state.EnrollmentState] = None
        # Group Tag of the Windows autopilot device.
        self._group_tag: Optional[str] = None
        # Intune Last Contacted Date Time of the Windows autopilot device.
        self._last_contacted_date_time: Optional[datetime] = None
        # Managed Device ID
        self._managed_device_id: Optional[str] = None
        # Oem manufacturer of the Windows autopilot device.
        self._manufacturer: Optional[str] = None
        # Model name of the Windows autopilot device.
        self._model: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Product Key of the Windows autopilot device.
        self._product_key: Optional[str] = None
        # Purchase Order Identifier of the Windows autopilot device.
        self._purchase_order_identifier: Optional[str] = None
        # Resource Name.
        self._resource_name: Optional[str] = None
        # Serial number of the Windows autopilot device.
        self._serial_number: Optional[str] = None
        # SKU Number
        self._sku_number: Optional[str] = None
        # System Family
        self._system_family: Optional[str] = None
        # User Principal Name.
        self._user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsAutopilotDeviceIdentity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsAutopilotDeviceIdentity
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsAutopilotDeviceIdentity()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Display Name
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Display Name
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def enrollment_state(self,) -> Optional[enrollment_state.EnrollmentState]:
        """
        Gets the enrollmentState property value. The enrollmentState property
        Returns: Optional[enrollment_state.EnrollmentState]
        """
        return self._enrollment_state
    
    @enrollment_state.setter
    def enrollment_state(self,value: Optional[enrollment_state.EnrollmentState] = None) -> None:
        """
        Sets the enrollmentState property value. The enrollmentState property
        Args:
            value: Value to set for the enrollmentState property.
        """
        self._enrollment_state = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "addressable_user_name": lambda n : setattr(self, 'addressable_user_name', n.get_str_value()),
            "azure_active_directory_device_id": lambda n : setattr(self, 'azure_active_directory_device_id', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "enrollment_state": lambda n : setattr(self, 'enrollment_state', n.get_enum_value(enrollment_state.EnrollmentState)),
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
    def last_contacted_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastContactedDateTime property value. Intune Last Contacted Date Time of the Windows autopilot device.
        Returns: Optional[datetime]
        """
        return self._last_contacted_date_time
    
    @last_contacted_date_time.setter
    def last_contacted_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastContactedDateTime property value. Intune Last Contacted Date Time of the Windows autopilot device.
        Args:
            value: Value to set for the lastContactedDateTime property.
        """
        self._last_contacted_date_time = value
    
    @property
    def managed_device_id(self,) -> Optional[str]:
        """
        Gets the managedDeviceId property value. Managed Device ID
        Returns: Optional[str]
        """
        return self._managed_device_id
    
    @managed_device_id.setter
    def managed_device_id(self,value: Optional[str] = None) -> None:
        """
        Sets the managedDeviceId property value. Managed Device ID
        Args:
            value: Value to set for the managedDeviceId property.
        """
        self._managed_device_id = value
    
    @property
    def manufacturer(self,) -> Optional[str]:
        """
        Gets the manufacturer property value. Oem manufacturer of the Windows autopilot device.
        Returns: Optional[str]
        """
        return self._manufacturer
    
    @manufacturer.setter
    def manufacturer(self,value: Optional[str] = None) -> None:
        """
        Sets the manufacturer property value. Oem manufacturer of the Windows autopilot device.
        Args:
            value: Value to set for the manufacturer property.
        """
        self._manufacturer = value
    
    @property
    def model(self,) -> Optional[str]:
        """
        Gets the model property value. Model name of the Windows autopilot device.
        Returns: Optional[str]
        """
        return self._model
    
    @model.setter
    def model(self,value: Optional[str] = None) -> None:
        """
        Sets the model property value. Model name of the Windows autopilot device.
        Args:
            value: Value to set for the model property.
        """
        self._model = value
    
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
    
    @property
    def purchase_order_identifier(self,) -> Optional[str]:
        """
        Gets the purchaseOrderIdentifier property value. Purchase Order Identifier of the Windows autopilot device.
        Returns: Optional[str]
        """
        return self._purchase_order_identifier
    
    @purchase_order_identifier.setter
    def purchase_order_identifier(self,value: Optional[str] = None) -> None:
        """
        Sets the purchaseOrderIdentifier property value. Purchase Order Identifier of the Windows autopilot device.
        Args:
            value: Value to set for the purchaseOrderIdentifier property.
        """
        self._purchase_order_identifier = value
    
    @property
    def resource_name(self,) -> Optional[str]:
        """
        Gets the resourceName property value. Resource Name.
        Returns: Optional[str]
        """
        return self._resource_name
    
    @resource_name.setter
    def resource_name(self,value: Optional[str] = None) -> None:
        """
        Sets the resourceName property value. Resource Name.
        Args:
            value: Value to set for the resourceName property.
        """
        self._resource_name = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
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
    def sku_number(self,) -> Optional[str]:
        """
        Gets the skuNumber property value. SKU Number
        Returns: Optional[str]
        """
        return self._sku_number
    
    @sku_number.setter
    def sku_number(self,value: Optional[str] = None) -> None:
        """
        Sets the skuNumber property value. SKU Number
        Args:
            value: Value to set for the skuNumber property.
        """
        self._sku_number = value
    
    @property
    def system_family(self,) -> Optional[str]:
        """
        Gets the systemFamily property value. System Family
        Returns: Optional[str]
        """
        return self._system_family
    
    @system_family.setter
    def system_family(self,value: Optional[str] = None) -> None:
        """
        Sets the systemFamily property value. System Family
        Args:
            value: Value to set for the systemFamily property.
        """
        self._system_family = value
    
    @property
    def user_principal_name(self,) -> Optional[str]:
        """
        Gets the userPrincipalName property value. User Principal Name.
        Returns: Optional[str]
        """
        return self._user_principal_name
    
    @user_principal_name.setter
    def user_principal_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userPrincipalName property value. User Principal Name.
        Args:
            value: Value to set for the userPrincipalName property.
        """
        self._user_principal_name = value
    

