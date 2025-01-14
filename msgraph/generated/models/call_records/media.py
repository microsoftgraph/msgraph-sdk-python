from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_info import DeviceInfo
    from .media_stream import MediaStream
    from .network_info import NetworkInfo

@dataclass
class Media(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Device information associated with the callee endpoint of this media.
    callee_device: Optional[DeviceInfo] = None
    # Network information associated with the callee endpoint of this media.
    callee_network: Optional[NetworkInfo] = None
    # Device information associated with the caller endpoint of this media.
    caller_device: Optional[DeviceInfo] = None
    # Network information associated with the caller endpoint of this media.
    caller_network: Optional[NetworkInfo] = None
    # How the media was identified during media negotiation stage.
    label: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Network streams associated with this media.
    streams: Optional[list[MediaStream]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Media:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Media
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Media()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_info import DeviceInfo
        from .media_stream import MediaStream
        from .network_info import NetworkInfo

        from .device_info import DeviceInfo
        from .media_stream import MediaStream
        from .network_info import NetworkInfo

        fields: dict[str, Callable[[Any], None]] = {
            "calleeDevice": lambda n : setattr(self, 'callee_device', n.get_object_value(DeviceInfo)),
            "calleeNetwork": lambda n : setattr(self, 'callee_network', n.get_object_value(NetworkInfo)),
            "callerDevice": lambda n : setattr(self, 'caller_device', n.get_object_value(DeviceInfo)),
            "callerNetwork": lambda n : setattr(self, 'caller_network', n.get_object_value(NetworkInfo)),
            "label": lambda n : setattr(self, 'label', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "streams": lambda n : setattr(self, 'streams', n.get_collection_of_object_values(MediaStream)),
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
        writer.write_object_value("calleeDevice", self.callee_device)
        writer.write_object_value("calleeNetwork", self.callee_network)
        writer.write_object_value("callerDevice", self.caller_device)
        writer.write_object_value("callerNetwork", self.caller_network)
        writer.write_str_value("label", self.label)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("streams", self.streams)
        writer.write_additional_data_value(self.additional_data)
    

