from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .network_adapter import NetworkAdapter

@dataclass
class SensorSettings(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Description of the sensor.
    description: Optional[str] = None
    # DNS names for the domain controller
    domain_controller_dns_names: Optional[list[str]] = None
    # Indicates whether to delay updates for the sensor.
    is_delayed_deployment_enabled: Optional[bool] = None
    # The networkAdapters property
    network_adapters: Optional[list[NetworkAdapter]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SensorSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SensorSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SensorSettings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .network_adapter import NetworkAdapter

        from .network_adapter import NetworkAdapter

        fields: dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "domainControllerDnsNames": lambda n : setattr(self, 'domain_controller_dns_names', n.get_collection_of_primitive_values(str)),
            "isDelayedDeploymentEnabled": lambda n : setattr(self, 'is_delayed_deployment_enabled', n.get_bool_value()),
            "networkAdapters": lambda n : setattr(self, 'network_adapters', n.get_collection_of_object_values(NetworkAdapter)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_str_value("description", self.description)
        writer.write_collection_of_primitive_values("domainControllerDnsNames", self.domain_controller_dns_names)
        writer.write_bool_value("isDelayedDeploymentEnabled", self.is_delayed_deployment_enabled)
        writer.write_collection_of_object_values("networkAdapters", self.network_adapters)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

