from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .click_source import ClickSource

@dataclass
class UserSimulationEventInfo(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Browser information from where the simulation event was initiated by a user in an attack simulation and training campaign.
    browser: Optional[str] = None
    # The clickSource property
    click_source: Optional[ClickSource] = None
    # Date and time of the simulation event by a user in an attack simulation and training campaign.
    event_date_time: Optional[datetime.datetime] = None
    # Name of the simulation event by a user in an attack simulation and training campaign.
    event_name: Optional[str] = None
    # IP address from where the simulation event was initiated by a user in an attack simulation and training campaign.
    ip_address: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The operating system, platform, and device details from where the simulation event was initiated by a user in an attack simulation and training campaign.
    os_platform_device_details: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserSimulationEventInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserSimulationEventInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UserSimulationEventInfo()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .click_source import ClickSource

        from .click_source import ClickSource

        fields: Dict[str, Callable[[Any], None]] = {
            "browser": lambda n : setattr(self, 'browser', n.get_str_value()),
            "clickSource": lambda n : setattr(self, 'click_source', n.get_enum_value(ClickSource)),
            "eventDateTime": lambda n : setattr(self, 'event_date_time', n.get_datetime_value()),
            "eventName": lambda n : setattr(self, 'event_name', n.get_str_value()),
            "ipAddress": lambda n : setattr(self, 'ip_address', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "osPlatformDeviceDetails": lambda n : setattr(self, 'os_platform_device_details', n.get_str_value()),
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
        writer.write_enum_value("clickSource", self.click_source)
        writer.write_datetime_value("eventDateTime", self.event_date_time)
        writer.write_str_value("eventName", self.event_name)
        writer.write_str_value("ipAddress", self.ip_address)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("osPlatformDeviceDetails", self.os_platform_device_details)
        writer.write_additional_data_value(self.additional_data)
    

