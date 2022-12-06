from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

mobile_app_assignment_settings = lazy_import('msgraph.generated.models.mobile_app_assignment_settings')

class MicrosoftStoreForBusinessAppAssignmentSettings(mobile_app_assignment_settings.MobileAppAssignmentSettings):
    def __init__(self,) -> None:
        """
        Instantiates a new MicrosoftStoreForBusinessAppAssignmentSettings and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.microsoftStoreForBusinessAppAssignmentSettings"
        # Whether or not to use device execution context for Microsoft Store for Business mobile app.
        self._use_device_context: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MicrosoftStoreForBusinessAppAssignmentSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MicrosoftStoreForBusinessAppAssignmentSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MicrosoftStoreForBusinessAppAssignmentSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "use_device_context": lambda n : setattr(self, 'use_device_context', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("useDeviceContext", self.use_device_context)
    
    @property
    def use_device_context(self,) -> Optional[bool]:
        """
        Gets the useDeviceContext property value. Whether or not to use device execution context for Microsoft Store for Business mobile app.
        Returns: Optional[bool]
        """
        return self._use_device_context
    
    @use_device_context.setter
    def use_device_context(self,value: Optional[bool] = None) -> None:
        """
        Sets the useDeviceContext property value. Whether or not to use device execution context for Microsoft Store for Business mobile app.
        Args:
            value: Value to set for the useDeviceContext property.
        """
        self._use_device_context = value
    

