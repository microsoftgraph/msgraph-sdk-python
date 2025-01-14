from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class DeviceDetail(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Indicates the browser information of the used in the sign-in. Populated for devices registered in Microsoft Entra.
    browser: Optional[str] = None
    # Refers to the unique ID of the device used in the sign-in. Populated for devices registered in Microsoft Entra.
    device_id: Optional[str] = None
    # Refers to the name of the device used in the sign-in. Populated for devices registered in Microsoft Entra.
    display_name: Optional[str] = None
    # Indicates whether the device is compliant or not.
    is_compliant: Optional[bool] = None
    # Indicates if the device is managed or not.
    is_managed: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates the OS name and version used in the sign-in.
    operating_system: Optional[str] = None
    # Indicates information on whether the device used in the sign-in is workplace-joined, Microsoft Entra-joined, domain-joined.
    trust_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceDetail
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceDetail()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
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
        if writer is None:
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
    

