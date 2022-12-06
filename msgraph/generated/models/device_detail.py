from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class DeviceDetail(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def browser(self,) -> Optional[str]:
        """
        Gets the browser property value. Indicates the browser information of the used for signing in.
        Returns: Optional[str]
        """
        return self._browser
    
    @browser.setter
    def browser(self,value: Optional[str] = None) -> None:
        """
        Sets the browser property value. Indicates the browser information of the used for signing in.
        Args:
            value: Value to set for the browser property.
        """
        self._browser = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new deviceDetail and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Indicates the browser information of the used for signing in.
        self._browser: Optional[str] = None
        # Refers to the UniqueID of the device used for signing in.
        self._device_id: Optional[str] = None
        # Refers to the name of the device used for signing in.
        self._display_name: Optional[str] = None
        # Indicates whether the device is compliant.
        self._is_compliant: Optional[bool] = None
        # Indicates whether the device is managed.
        self._is_managed: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Indicates the operating system name and version used for signing in.
        self._operating_system: Optional[str] = None
        # Provides information about whether the signed-in device is Workplace Joined, AzureAD Joined, Domain Joined.
        self._trust_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceDetail
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceDetail()
    
    @property
    def device_id(self,) -> Optional[str]:
        """
        Gets the deviceId property value. Refers to the UniqueID of the device used for signing in.
        Returns: Optional[str]
        """
        return self._device_id
    
    @device_id.setter
    def device_id(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceId property value. Refers to the UniqueID of the device used for signing in.
        Args:
            value: Value to set for the deviceId property.
        """
        self._device_id = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Refers to the name of the device used for signing in.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Refers to the name of the device used for signing in.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "browser": lambda n : setattr(self, 'browser', n.get_str_value()),
            "device_id": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "is_compliant": lambda n : setattr(self, 'is_compliant', n.get_bool_value()),
            "is_managed": lambda n : setattr(self, 'is_managed', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "operating_system": lambda n : setattr(self, 'operating_system', n.get_str_value()),
            "trust_type": lambda n : setattr(self, 'trust_type', n.get_str_value()),
        }
        return fields
    
    @property
    def is_compliant(self,) -> Optional[bool]:
        """
        Gets the isCompliant property value. Indicates whether the device is compliant.
        Returns: Optional[bool]
        """
        return self._is_compliant
    
    @is_compliant.setter
    def is_compliant(self,value: Optional[bool] = None) -> None:
        """
        Sets the isCompliant property value. Indicates whether the device is compliant.
        Args:
            value: Value to set for the isCompliant property.
        """
        self._is_compliant = value
    
    @property
    def is_managed(self,) -> Optional[bool]:
        """
        Gets the isManaged property value. Indicates whether the device is managed.
        Returns: Optional[bool]
        """
        return self._is_managed
    
    @is_managed.setter
    def is_managed(self,value: Optional[bool] = None) -> None:
        """
        Sets the isManaged property value. Indicates whether the device is managed.
        Args:
            value: Value to set for the isManaged property.
        """
        self._is_managed = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def operating_system(self,) -> Optional[str]:
        """
        Gets the operatingSystem property value. Indicates the operating system name and version used for signing in.
        Returns: Optional[str]
        """
        return self._operating_system
    
    @operating_system.setter
    def operating_system(self,value: Optional[str] = None) -> None:
        """
        Sets the operatingSystem property value. Indicates the operating system name and version used for signing in.
        Args:
            value: Value to set for the operatingSystem property.
        """
        self._operating_system = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("browser", self.browser)
        writer.write_str_value("deviceId", self.device_id)
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("isCompliant", self.is_compliant)
        writer.write_bool_value("isManaged", self.is_managed)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("operatingSystem", self.operating_system)
        writer.write_str_value("trustType", self.trust_type)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def trust_type(self,) -> Optional[str]:
        """
        Gets the trustType property value. Provides information about whether the signed-in device is Workplace Joined, AzureAD Joined, Domain Joined.
        Returns: Optional[str]
        """
        return self._trust_type
    
    @trust_type.setter
    def trust_type(self,value: Optional[str] = None) -> None:
        """
        Sets the trustType property value. Provides information about whether the signed-in device is Workplace Joined, AzureAD Joined, Domain Joined.
        Args:
            value: Value to set for the trustType property.
        """
        self._trust_type = value
    

