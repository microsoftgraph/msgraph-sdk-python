from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models.device_management_exchange_connector_sync_type import DeviceManagementExchangeConnectorSyncType

@dataclass
class SyncPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The type of Exchange Connector sync requested.
    sync_type: Optional[DeviceManagementExchangeConnectorSyncType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SyncPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SyncPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SyncPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .....models.device_management_exchange_connector_sync_type import DeviceManagementExchangeConnectorSyncType

        from .....models.device_management_exchange_connector_sync_type import DeviceManagementExchangeConnectorSyncType

        fields: Dict[str, Callable[[Any], None]] = {
            "syncType": lambda n : setattr(self, 'sync_type', n.get_enum_value(DeviceManagementExchangeConnectorSyncType)),
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
        writer.write_enum_value("syncType", self.sync_type)
        writer.write_additional_data_value(self.additional_data)
    

