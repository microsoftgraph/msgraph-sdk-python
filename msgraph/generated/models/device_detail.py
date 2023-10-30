from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class DeviceDetail(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Indicates the browser information of the used for signing in.
    browser: Optional[str] = None
    # Refers to the UniqueID of the device used for signing in.
    device_id: Optional[str] = None
    # Refers to the name of the device used for signing in.
    display_name: Optional[str] = None
    # Indicates whether the device is compliant.
    is_compliant: Optional[bool] = None
    # Indicates whether the device is managed.
    is_managed: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates the operating system name and version used for signing in.
    operating_system: Optional[str] = None
    # Provides information about whether the signed-in device is Workplace Joined, AzureAD Joined, Domain Joined.
    trust_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceDetail
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DeviceDetail()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "browser": lambda n : setattr(self, 'browser', n.get_str_value()),
            "deviceId": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "isCompliant": lambda n : setattr(self, 'is_compliant', n.get_bool_value()),
            "isManaged": lambda n : setattr(self, 'is_managed', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "operatingSystem": lambda n : setattr(self, 'operating_system', n.get_str_value()),
            "trustType": lambda n : setattr(self, 'trust_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("browser", self.browser)
        writer.write_str_value("deviceId", self.device_id)
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("isCompliant", self.is_compliant)
        writer.write_bool_value("isManaged", self.is_managed)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("operatingSystem", self.operating_system)
        writer.write_str_value("trustType", self.trust_type)
        writer.write_additional_data_value(self.additional_data)
    

