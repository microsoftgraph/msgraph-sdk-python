from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

update_windows_device_account_action_parameter = lazy_import('msgraph.generated.models.update_windows_device_account_action_parameter')

class UpdateWindowsDeviceAccountPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the updateWindowsDeviceAccount method.
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
        Instantiates a new updateWindowsDeviceAccountPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The updateWindowsDeviceAccountActionParameter property
        self._update_windows_device_account_action_parameter: Optional[update_windows_device_account_action_parameter.UpdateWindowsDeviceAccountActionParameter] = None
    
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
        fields = {
            "update_windows_device_account_action_parameter": lambda n : setattr(self, 'update_windows_device_account_action_parameter', n.get_object_value(update_windows_device_account_action_parameter.UpdateWindowsDeviceAccountActionParameter)),
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
    
    @property
    def update_windows_device_account_action_parameter(self,) -> Optional[update_windows_device_account_action_parameter.UpdateWindowsDeviceAccountActionParameter]:
        """
        Gets the updateWindowsDeviceAccountActionParameter property value. The updateWindowsDeviceAccountActionParameter property
        Returns: Optional[update_windows_device_account_action_parameter.UpdateWindowsDeviceAccountActionParameter]
        """
        return self._update_windows_device_account_action_parameter
    
    @update_windows_device_account_action_parameter.setter
    def update_windows_device_account_action_parameter(self,value: Optional[update_windows_device_account_action_parameter.UpdateWindowsDeviceAccountActionParameter] = None) -> None:
        """
        Sets the updateWindowsDeviceAccountActionParameter property value. The updateWindowsDeviceAccountActionParameter property
        Args:
            value: Value to set for the updateWindowsDeviceAccountActionParameter property.
        """
        self._update_windows_device_account_action_parameter = value
    

