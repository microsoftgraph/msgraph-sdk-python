from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .alert_evidence import AlertEvidence

from .alert_evidence import AlertEvidence

@dataclass
class AmazonResourceEvidence(AlertEvidence):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.amazonResourceEvidence"
    # The unique identifier for the Amazon account.
    amazon_account_id: Optional[str] = None
    # The Amazon resource identifier (ARN) for the cloud resource.
    amazon_resource_id: Optional[str] = None
    # The name of the resource.
    resource_name: Optional[str] = None
    # The type of the resource.
    resource_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AmazonResourceEvidence:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AmazonResourceEvidence
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AmazonResourceEvidence()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .alert_evidence import AlertEvidence

        from .alert_evidence import AlertEvidence

        fields: Dict[str, Callable[[Any], None]] = {
            "amazonAccountId": lambda n : setattr(self, 'amazon_account_id', n.get_str_value()),
            "amazonResourceId": lambda n : setattr(self, 'amazon_resource_id', n.get_str_value()),
            "resourceName": lambda n : setattr(self, 'resource_name', n.get_str_value()),
            "resourceType": lambda n : setattr(self, 'resource_type', n.get_str_value()),
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
        writer.write_str_value("amazonAccountId", self.amazon_account_id)
        writer.write_str_value("amazonResourceId", self.amazon_resource_id)
        writer.write_str_value("resourceName", self.resource_name)
        writer.write_str_value("resourceType", self.resource_type)
    

