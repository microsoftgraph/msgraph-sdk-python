from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .custom_extension_endpoint_configuration import CustomExtensionEndpointConfiguration

from .custom_extension_endpoint_configuration import CustomExtensionEndpointConfiguration

@dataclass
class LogicAppTriggerEndpointConfiguration(CustomExtensionEndpointConfiguration, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.logicAppTriggerEndpointConfiguration"
    # The name of the logic app.
    logic_app_workflow_name: Optional[str] = None
    # The Azure resource group name for the logic app.
    resource_group_name: Optional[str] = None
    # Identifier of the Azure subscription for the logic app.
    subscription_id: Optional[str] = None
    # The URL to the logic app endpoint that will be triggered. Only required for app-only token scenarios where app is creating a customCalloutExtension without a signed-in user.
    url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LogicAppTriggerEndpointConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LogicAppTriggerEndpointConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LogicAppTriggerEndpointConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .custom_extension_endpoint_configuration import CustomExtensionEndpointConfiguration

        from .custom_extension_endpoint_configuration import CustomExtensionEndpointConfiguration

        fields: dict[str, Callable[[Any], None]] = {
            "logicAppWorkflowName": lambda n : setattr(self, 'logic_app_workflow_name', n.get_str_value()),
            "resourceGroupName": lambda n : setattr(self, 'resource_group_name', n.get_str_value()),
            "subscriptionId": lambda n : setattr(self, 'subscription_id', n.get_str_value()),
            "url": lambda n : setattr(self, 'url', n.get_str_value()),
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
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("logicAppWorkflowName", self.logic_app_workflow_name)
        writer.write_str_value("resourceGroupName", self.resource_group_name)
        writer.write_str_value("subscriptionId", self.subscription_id)
        writer.write_str_value("url", self.url)
    

