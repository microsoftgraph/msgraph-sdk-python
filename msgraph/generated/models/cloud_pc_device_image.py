from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_pc_device_image_error_code import CloudPcDeviceImageErrorCode
    from .cloud_pc_device_image_os_status import CloudPcDeviceImageOsStatus
    from .cloud_pc_device_image_status import CloudPcDeviceImageStatus
    from .entity import Entity

from .entity import Entity

@dataclass
class CloudPcDeviceImage(Entity):
    # The displayName property
    display_name: Optional[str] = None
    # The errorCode property
    error_code: Optional[CloudPcDeviceImageErrorCode] = None
    # The expirationDate property
    expiration_date: Optional[datetime.date] = None
    # The lastModifiedDateTime property
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The operatingSystem property
    operating_system: Optional[str] = None
    # The osBuildNumber property
    os_build_number: Optional[str] = None
    # The osStatus property
    os_status: Optional[CloudPcDeviceImageOsStatus] = None
    # The sourceImageResourceId property
    source_image_resource_id: Optional[str] = None
    # The status property
    status: Optional[CloudPcDeviceImageStatus] = None
    # The version property
    version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CloudPcDeviceImage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcDeviceImage
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return CloudPcDeviceImage()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_pc_device_image_error_code import CloudPcDeviceImageErrorCode
        from .cloud_pc_device_image_os_status import CloudPcDeviceImageOsStatus
        from .cloud_pc_device_image_status import CloudPcDeviceImageStatus
        from .entity import Entity

        from .cloud_pc_device_image_error_code import CloudPcDeviceImageErrorCode
        from .cloud_pc_device_image_os_status import CloudPcDeviceImageOsStatus
        from .cloud_pc_device_image_status import CloudPcDeviceImageStatus
        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "errorCode": lambda n : setattr(self, 'error_code', n.get_enum_value(CloudPcDeviceImageErrorCode)),
            "expirationDate": lambda n : setattr(self, 'expiration_date', n.get_date_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "operatingSystem": lambda n : setattr(self, 'operating_system', n.get_str_value()),
            "osBuildNumber": lambda n : setattr(self, 'os_build_number', n.get_str_value()),
            "osStatus": lambda n : setattr(self, 'os_status', n.get_enum_value(CloudPcDeviceImageOsStatus)),
            "sourceImageResourceId": lambda n : setattr(self, 'source_image_resource_id', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(CloudPcDeviceImageStatus)),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("errorCode", self.error_code)
        writer.write_date_value("expirationDate", self.expiration_date)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("operatingSystem", self.operating_system)
        writer.write_str_value("osBuildNumber", self.os_build_number)
        writer.write_enum_value("osStatus", self.os_status)
        writer.write_str_value("sourceImageResourceId", self.source_image_resource_id)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("version", self.version)
    

