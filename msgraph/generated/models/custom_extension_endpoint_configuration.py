from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .http_request_endpoint import HttpRequestEndpoint
    from .logic_app_trigger_endpoint_configuration import LogicAppTriggerEndpointConfiguration

@dataclass
class CustomExtensionEndpointConfiguration(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CustomExtensionEndpointConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CustomExtensionEndpointConfiguration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.httpRequestEndpoint".casefold():
            from .http_request_endpoint import HttpRequestEndpoint

            return HttpRequestEndpoint()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.logicAppTriggerEndpointConfiguration".casefold():
            from .logic_app_trigger_endpoint_configuration import LogicAppTriggerEndpointConfiguration

            return LogicAppTriggerEndpointConfiguration()
        return CustomExtensionEndpointConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .http_request_endpoint import HttpRequestEndpoint
        from .logic_app_trigger_endpoint_configuration import LogicAppTriggerEndpointConfiguration

        from .http_request_endpoint import HttpRequestEndpoint
        from .logic_app_trigger_endpoint_configuration import LogicAppTriggerEndpointConfiguration

        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

