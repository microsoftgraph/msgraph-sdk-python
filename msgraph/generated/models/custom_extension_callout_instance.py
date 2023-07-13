from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .custom_extension_callout_instance_status import CustomExtensionCalloutInstanceStatus

@dataclass
class CustomExtensionCalloutInstance(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The customExtensionId property
    custom_extension_id: Optional[str] = None
    # The detail property
    detail: Optional[str] = None
    # The externalCorrelationId property
    external_correlation_id: Optional[str] = None
    # The id property
    id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The status property
    status: Optional[CustomExtensionCalloutInstanceStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CustomExtensionCalloutInstance:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CustomExtensionCalloutInstance
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return CustomExtensionCalloutInstance()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .custom_extension_callout_instance_status import CustomExtensionCalloutInstanceStatus

        from .custom_extension_callout_instance_status import CustomExtensionCalloutInstanceStatus

        fields: Dict[str, Callable[[Any], None]] = {
            "customExtensionId": lambda n : setattr(self, 'custom_extension_id', n.get_str_value()),
            "detail": lambda n : setattr(self, 'detail', n.get_str_value()),
            "externalCorrelationId": lambda n : setattr(self, 'external_correlation_id', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(CustomExtensionCalloutInstanceStatus)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("customExtensionId", self.custom_extension_id)
        writer.write_str_value("detail", self.detail)
        writer.write_str_value("externalCorrelationId", self.external_correlation_id)
        writer.write_str_value("id", self.id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    

