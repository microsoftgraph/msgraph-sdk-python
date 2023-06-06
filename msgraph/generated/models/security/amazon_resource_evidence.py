from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import alert_evidence

from . import alert_evidence

@dataclass
class AmazonResourceEvidence(alert_evidence.AlertEvidence):
    # The unique identifier for the Amazon account.
    amazon_account_id: Optional[str] = None
    # The Amazon resource identifier (ARN) for the cloud resource.
    amazon_resource_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The name of the resource.
    resource_name: Optional[str] = None
    # The type of the resource.
    resource_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AmazonResourceEvidence:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AmazonResourceEvidence
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AmazonResourceEvidence()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import alert_evidence

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
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("amazonAccountId", self.amazon_account_id)
        writer.write_str_value("amazonResourceId", self.amazon_resource_id)
        writer.write_str_value("resourceName", self.resource_name)
        writer.write_str_value("resourceType", self.resource_type)
    

