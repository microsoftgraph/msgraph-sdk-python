from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_management_exchange_connector_sync_type = lazy_import('msgraph.generated.models.device_management_exchange_connector_sync_type')

class SyncPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the sync method.
    """
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new syncPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The type of Exchange Connector sync requested.
        self._sync_type: Optional[device_management_exchange_connector_sync_type.DeviceManagementExchangeConnectorSyncType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SyncPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SyncPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SyncPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "sync_type": lambda n : setattr(self, 'sync_type', n.get_enum_value(device_management_exchange_connector_sync_type.DeviceManagementExchangeConnectorSyncType)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_enum_value("syncType", self.sync_type)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def sync_type(self,) -> Optional[device_management_exchange_connector_sync_type.DeviceManagementExchangeConnectorSyncType]:
        """
        Gets the syncType property value. The type of Exchange Connector sync requested.
        Returns: Optional[device_management_exchange_connector_sync_type.DeviceManagementExchangeConnectorSyncType]
        """
        return self._sync_type
    
    @sync_type.setter
    def sync_type(self,value: Optional[device_management_exchange_connector_sync_type.DeviceManagementExchangeConnectorSyncType] = None) -> None:
        """
        Sets the syncType property value. The type of Exchange Connector sync requested.
        Args:
            value: Value to set for the syncType property.
        """
        self._sync_type = value
    

