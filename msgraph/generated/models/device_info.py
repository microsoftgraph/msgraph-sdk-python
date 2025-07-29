from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class DeviceInfo(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Unique identifier set by Azure Device Registration Service at the time of registration.
    device_id: Optional[str] = None
    # The display name for the device.
    display_name: Optional[str] = None
    # Enrollment profile applied to the device.
    enrollment_profile_name: Optional[str] = None
    # Extension attribute.
    extension_attribute1: Optional[str] = None
    # Extension attribute.
    extension_attribute10: Optional[str] = None
    # Extension attribute.
    extension_attribute11: Optional[str] = None
    # Extension attribute.
    extension_attribute12: Optional[str] = None
    # Extension attribute.
    extension_attribute13: Optional[str] = None
    # Extension attribute.
    extension_attribute14: Optional[str] = None
    # Extension attribute.
    extension_attribute15: Optional[str] = None
    # Extension attribute.
    extension_attribute2: Optional[str] = None
    # Extension attribute.
    extension_attribute3: Optional[str] = None
    # Extension attribute.
    extension_attribute4: Optional[str] = None
    # Extension attribute.
    extension_attribute5: Optional[str] = None
    # Extension attribute.
    extension_attribute6: Optional[str] = None
    # Extension attribute.
    extension_attribute7: Optional[str] = None
    # Extension attribute.
    extension_attribute8: Optional[str] = None
    # Extension attribute.
    extension_attribute9: Optional[str] = None
    # Indicates the device compliance status with Mobile Management Device (MDM) policies. Default is false.
    is_compliant: Optional[bool] = None
    # Manufacturer of the device.
    manufacturer: Optional[str] = None
    # Application identifier used to register device into MDM.
    mdm_app_id: Optional[str] = None
    # Model of the device.
    model: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The type of operating system on the device.
    operating_system: Optional[str] = None
    # The version of the operating system on the device.
    operating_system_version: Optional[str] = None
    # Ownership of the device. This property is set by Intune.
    ownership: Optional[str] = None
    # A collection of physical identifiers for the device.
    physical_ids: Optional[list[str]] = None
    # The profile type of the device.
    profile_type: Optional[str] = None
    # List of labels applied to the device by the system.
    system_labels: Optional[list[str]] = None
    # Type of trust for the joined device.
    trust_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceInfo()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "deviceId": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "enrollmentProfileName": lambda n : setattr(self, 'enrollment_profile_name', n.get_str_value()),
            "extensionAttribute1": lambda n : setattr(self, 'extension_attribute1', n.get_str_value()),
            "extensionAttribute10": lambda n : setattr(self, 'extension_attribute10', n.get_str_value()),
            "extensionAttribute11": lambda n : setattr(self, 'extension_attribute11', n.get_str_value()),
            "extensionAttribute12": lambda n : setattr(self, 'extension_attribute12', n.get_str_value()),
            "extensionAttribute13": lambda n : setattr(self, 'extension_attribute13', n.get_str_value()),
            "extensionAttribute14": lambda n : setattr(self, 'extension_attribute14', n.get_str_value()),
            "extensionAttribute15": lambda n : setattr(self, 'extension_attribute15', n.get_str_value()),
            "extensionAttribute2": lambda n : setattr(self, 'extension_attribute2', n.get_str_value()),
            "extensionAttribute3": lambda n : setattr(self, 'extension_attribute3', n.get_str_value()),
            "extensionAttribute4": lambda n : setattr(self, 'extension_attribute4', n.get_str_value()),
            "extensionAttribute5": lambda n : setattr(self, 'extension_attribute5', n.get_str_value()),
            "extensionAttribute6": lambda n : setattr(self, 'extension_attribute6', n.get_str_value()),
            "extensionAttribute7": lambda n : setattr(self, 'extension_attribute7', n.get_str_value()),
            "extensionAttribute8": lambda n : setattr(self, 'extension_attribute8', n.get_str_value()),
            "extensionAttribute9": lambda n : setattr(self, 'extension_attribute9', n.get_str_value()),
            "isCompliant": lambda n : setattr(self, 'is_compliant', n.get_bool_value()),
            "manufacturer": lambda n : setattr(self, 'manufacturer', n.get_str_value()),
            "mdmAppId": lambda n : setattr(self, 'mdm_app_id', n.get_str_value()),
            "model": lambda n : setattr(self, 'model', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "operatingSystem": lambda n : setattr(self, 'operating_system', n.get_str_value()),
            "operatingSystemVersion": lambda n : setattr(self, 'operating_system_version', n.get_str_value()),
            "ownership": lambda n : setattr(self, 'ownership', n.get_str_value()),
            "physicalIds": lambda n : setattr(self, 'physical_ids', n.get_collection_of_primitive_values(str)),
            "profileType": lambda n : setattr(self, 'profile_type', n.get_str_value()),
            "systemLabels": lambda n : setattr(self, 'system_labels', n.get_collection_of_primitive_values(str)),
            "trustType": lambda n : setattr(self, 'trust_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("deviceId", self.device_id)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("enrollmentProfileName", self.enrollment_profile_name)
        writer.write_str_value("extensionAttribute1", self.extension_attribute1)
        writer.write_str_value("extensionAttribute10", self.extension_attribute10)
        writer.write_str_value("extensionAttribute11", self.extension_attribute11)
        writer.write_str_value("extensionAttribute12", self.extension_attribute12)
        writer.write_str_value("extensionAttribute13", self.extension_attribute13)
        writer.write_str_value("extensionAttribute14", self.extension_attribute14)
        writer.write_str_value("extensionAttribute15", self.extension_attribute15)
        writer.write_str_value("extensionAttribute2", self.extension_attribute2)
        writer.write_str_value("extensionAttribute3", self.extension_attribute3)
        writer.write_str_value("extensionAttribute4", self.extension_attribute4)
        writer.write_str_value("extensionAttribute5", self.extension_attribute5)
        writer.write_str_value("extensionAttribute6", self.extension_attribute6)
        writer.write_str_value("extensionAttribute7", self.extension_attribute7)
        writer.write_str_value("extensionAttribute8", self.extension_attribute8)
        writer.write_str_value("extensionAttribute9", self.extension_attribute9)
        writer.write_bool_value("isCompliant", self.is_compliant)
        writer.write_str_value("manufacturer", self.manufacturer)
        writer.write_str_value("mdmAppId", self.mdm_app_id)
        writer.write_str_value("model", self.model)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("operatingSystem", self.operating_system)
        writer.write_str_value("operatingSystemVersion", self.operating_system_version)
        writer.write_str_value("ownership", self.ownership)
        writer.write_collection_of_primitive_values("physicalIds", self.physical_ids)
        writer.write_str_value("profileType", self.profile_type)
        writer.write_collection_of_primitive_values("systemLabels", self.system_labels)
        writer.write_str_value("trustType", self.trust_type)
        writer.write_additional_data_value(self.additional_data)
    

