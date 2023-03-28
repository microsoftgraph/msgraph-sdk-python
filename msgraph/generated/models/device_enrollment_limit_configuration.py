from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_enrollment_configuration = lazy_import('msgraph.generated.models.device_enrollment_configuration')

class DeviceEnrollmentLimitConfiguration(device_enrollment_configuration.DeviceEnrollmentConfiguration):
    def __init__(self,) -> None:
        """
        Instantiates a new DeviceEnrollmentLimitConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.deviceEnrollmentLimitConfiguration"
        # The maximum number of devices that a user can enroll
        self._limit: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceEnrollmentLimitConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceEnrollmentLimitConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceEnrollmentLimitConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "limit": lambda n : setattr(self, 'limit', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def limit(self,) -> Optional[int]:
        """
        Gets the limit property value. The maximum number of devices that a user can enroll
        Returns: Optional[int]
        """
        return self._limit
    
    @limit.setter
    def limit(self,value: Optional[int] = None) -> None:
        """
        Sets the limit property value. The maximum number of devices that a user can enroll
        Args:
            value: Value to set for the limit property.
        """
        self._limit = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_int_value("limit", self.limit)
    

