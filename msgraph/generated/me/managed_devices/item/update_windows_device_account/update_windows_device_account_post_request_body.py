from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models import update_windows_device_account_action_parameter

@dataclass
class UpdateWindowsDeviceAccountPostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The updateWindowsDeviceAccountActionParameter property
    update_windows_device_account_action_parameter: Optional[update_windows_device_account_action_parameter.UpdateWindowsDeviceAccountActionParameter] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UpdateWindowsDeviceAccountPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UpdateWindowsDeviceAccountPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UpdateWindowsDeviceAccountPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .....models import update_windows_device_account_action_parameter

        fields: Dict[str, Callable[[Any], None]] = {
            "updateWindowsDeviceAccountActionParameter": lambda n : setattr(self, 'update_windows_device_account_action_parameter', n.get_object_value(update_windows_device_account_action_parameter.UpdateWindowsDeviceAccountActionParameter)),
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
        writer.write_object_value("updateWindowsDeviceAccountActionParameter", self.update_windows_device_account_action_parameter)
        writer.write_additional_data_value(self.additional_data)
    

