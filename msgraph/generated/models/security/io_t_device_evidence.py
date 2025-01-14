from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .alert_evidence import AlertEvidence
    from .azure_resource_evidence import AzureResourceEvidence
    from .io_t_device_importance_type import IoTDeviceImportanceType
    from .ip_evidence import IpEvidence
    from .nic_evidence import NicEvidence
    from .url_evidence import UrlEvidence

from .alert_evidence import AlertEvidence

@dataclass
class IoTDeviceEvidence(AlertEvidence, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.ioTDeviceEvidence"
    # The device ID.
    device_id: Optional[str] = None
    # The friendly name of the device.
    device_name: Optional[str] = None
    # The URL to the device page in the IoT Defender portal.
    device_page_link: Optional[str] = None
    # The device subtype.
    device_sub_type: Optional[str] = None
    # The type of the device. For example, 'temperature sensor,' 'freezer,' 'wind turbine,' and so on.
    device_type: Optional[str] = None
    # The importance level for the IoT device. Possible values are low, normal, high, and unknownFutureValue.
    importance: Optional[IoTDeviceImportanceType] = None
    # The azureResourceEvidence entity that represents the IoT Hub that the device belongs to.
    io_t_hub: Optional[AzureResourceEvidence] = None
    # The ID of the Azure Security Center for the IoT agent that is running on the device.
    io_t_security_agent_id: Optional[str] = None
    # The current IP address of the device.
    ip_address: Optional[IpEvidence] = None
    # Indicates whether the device classified as an authorized device.
    is_authorized: Optional[bool] = None
    # Indicates whether the device classified as a programming device.
    is_programming: Optional[bool] = None
    # Indicates whether the device classified as a scanner.
    is_scanner: Optional[bool] = None
    # The MAC address of the device.
    mac_address: Optional[str] = None
    # The manufacturer of the device.
    manufacturer: Optional[str] = None
    # The model of the device.
    model: Optional[str] = None
    # The current network interface controllers on the device.
    nics: Optional[list[NicEvidence]] = None
    # The operating system the device is running.
    operating_system: Optional[str] = None
    # The owners for the device.
    owners: Optional[list[str]] = None
    # The list of protocols that the device supports.
    protocols: Optional[list[str]] = None
    # The Purdue Layer of the device.
    purdue_layer: Optional[str] = None
    # The sensor that monitors the device.
    sensor: Optional[str] = None
    # The serial number of the device.
    serial_number: Optional[str] = None
    # The site location of the device.
    site: Optional[str] = None
    # The source (microsoft/vendor) of the device entity.
    source: Optional[str] = None
    # A URL reference to the source item where the device is managed.
    source_ref: Optional[UrlEvidence] = None
    # The zone location of the device within a site.
    zone: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IoTDeviceEvidence:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IoTDeviceEvidence
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return IoTDeviceEvidence()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .alert_evidence import AlertEvidence
        from .azure_resource_evidence import AzureResourceEvidence
        from .io_t_device_importance_type import IoTDeviceImportanceType
        from .ip_evidence import IpEvidence
        from .nic_evidence import NicEvidence
        from .url_evidence import UrlEvidence

        from .alert_evidence import AlertEvidence
        from .azure_resource_evidence import AzureResourceEvidence
        from .io_t_device_importance_type import IoTDeviceImportanceType
        from .ip_evidence import IpEvidence
        from .nic_evidence import NicEvidence
        from .url_evidence import UrlEvidence

        fields: dict[str, Callable[[Any], None]] = {
            "deviceId": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "deviceName": lambda n : setattr(self, 'device_name', n.get_str_value()),
            "devicePageLink": lambda n : setattr(self, 'device_page_link', n.get_str_value()),
            "deviceSubType": lambda n : setattr(self, 'device_sub_type', n.get_str_value()),
            "deviceType": lambda n : setattr(self, 'device_type', n.get_str_value()),
            "importance": lambda n : setattr(self, 'importance', n.get_enum_value(IoTDeviceImportanceType)),
            "ioTHub": lambda n : setattr(self, 'io_t_hub', n.get_object_value(AzureResourceEvidence)),
            "ioTSecurityAgentId": lambda n : setattr(self, 'io_t_security_agent_id', n.get_str_value()),
            "ipAddress": lambda n : setattr(self, 'ip_address', n.get_object_value(IpEvidence)),
            "isAuthorized": lambda n : setattr(self, 'is_authorized', n.get_bool_value()),
            "isProgramming": lambda n : setattr(self, 'is_programming', n.get_bool_value()),
            "isScanner": lambda n : setattr(self, 'is_scanner', n.get_bool_value()),
            "macAddress": lambda n : setattr(self, 'mac_address', n.get_str_value()),
            "manufacturer": lambda n : setattr(self, 'manufacturer', n.get_str_value()),
            "model": lambda n : setattr(self, 'model', n.get_str_value()),
            "nics": lambda n : setattr(self, 'nics', n.get_collection_of_object_values(NicEvidence)),
            "operatingSystem": lambda n : setattr(self, 'operating_system', n.get_str_value()),
            "owners": lambda n : setattr(self, 'owners', n.get_collection_of_primitive_values(str)),
            "protocols": lambda n : setattr(self, 'protocols', n.get_collection_of_primitive_values(str)),
            "purdueLayer": lambda n : setattr(self, 'purdue_layer', n.get_str_value()),
            "sensor": lambda n : setattr(self, 'sensor', n.get_str_value()),
            "serialNumber": lambda n : setattr(self, 'serial_number', n.get_str_value()),
            "site": lambda n : setattr(self, 'site', n.get_str_value()),
            "source": lambda n : setattr(self, 'source', n.get_str_value()),
            "sourceRef": lambda n : setattr(self, 'source_ref', n.get_object_value(UrlEvidence)),
            "zone": lambda n : setattr(self, 'zone', n.get_str_value()),
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
        writer.write_str_value("deviceId", self.device_id)
        writer.write_str_value("deviceName", self.device_name)
        writer.write_str_value("devicePageLink", self.device_page_link)
        writer.write_str_value("deviceSubType", self.device_sub_type)
        writer.write_str_value("deviceType", self.device_type)
        writer.write_enum_value("importance", self.importance)
        writer.write_object_value("ioTHub", self.io_t_hub)
        writer.write_str_value("ioTSecurityAgentId", self.io_t_security_agent_id)
        writer.write_object_value("ipAddress", self.ip_address)
        writer.write_bool_value("isAuthorized", self.is_authorized)
        writer.write_bool_value("isProgramming", self.is_programming)
        writer.write_bool_value("isScanner", self.is_scanner)
        writer.write_str_value("macAddress", self.mac_address)
        writer.write_str_value("manufacturer", self.manufacturer)
        writer.write_str_value("model", self.model)
        writer.write_collection_of_object_values("nics", self.nics)
        writer.write_str_value("operatingSystem", self.operating_system)
        writer.write_collection_of_primitive_values("owners", self.owners)
        writer.write_collection_of_primitive_values("protocols", self.protocols)
        writer.write_str_value("purdueLayer", self.purdue_layer)
        writer.write_str_value("sensor", self.sensor)
        writer.write_str_value("serialNumber", self.serial_number)
        writer.write_str_value("site", self.site)
        writer.write_str_value("source", self.source)
        writer.write_object_value("sourceRef", self.source_ref)
        writer.write_str_value("zone", self.zone)
    

