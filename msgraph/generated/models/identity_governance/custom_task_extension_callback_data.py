from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..custom_extension_data import CustomExtensionData
    from .custom_task_extension_operation_status import CustomTaskExtensionOperationStatus

from ..custom_extension_data import CustomExtensionData

@dataclass
class CustomTaskExtensionCallbackData(CustomExtensionData, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.identityGovernance.customTaskExtensionCallbackData"
    # Operation status that's provided by the Azure Logic App indicating whenever the Azure Logic App has run successfully or not. Supported values: completed, failed, unknownFutureValue.
    operation_status: Optional[CustomTaskExtensionOperationStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CustomTaskExtensionCallbackData:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CustomTaskExtensionCallbackData
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CustomTaskExtensionCallbackData()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..custom_extension_data import CustomExtensionData
        from .custom_task_extension_operation_status import CustomTaskExtensionOperationStatus

        from ..custom_extension_data import CustomExtensionData
        from .custom_task_extension_operation_status import CustomTaskExtensionOperationStatus

        fields: dict[str, Callable[[Any], None]] = {
            "operationStatus": lambda n : setattr(self, 'operation_status', n.get_enum_value(CustomTaskExtensionOperationStatus)),
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
        writer.write_enum_value("operationStatus", self.operation_status)
    

