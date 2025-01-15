from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ...entity import Entity
    from .azure_usage import AzureUsage
    from .billing_reconciliation import BillingReconciliation
    from .manifest import Manifest
    from .operation import Operation

from ...entity import Entity

@dataclass
class Billing(Entity, Parsable):
    # Represents metadata for the exported data.
    manifests: Optional[list[Manifest]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Represents an operation to export the billing data of a partner.
    operations: Optional[list[Operation]] = None
    # The reconciliation property
    reconciliation: Optional[BillingReconciliation] = None
    # The usage property
    usage: Optional[AzureUsage] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Billing:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Billing
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Billing()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ...entity import Entity
        from .azure_usage import AzureUsage
        from .billing_reconciliation import BillingReconciliation
        from .manifest import Manifest
        from .operation import Operation

        from ...entity import Entity
        from .azure_usage import AzureUsage
        from .billing_reconciliation import BillingReconciliation
        from .manifest import Manifest
        from .operation import Operation

        fields: dict[str, Callable[[Any], None]] = {
            "manifests": lambda n : setattr(self, 'manifests', n.get_collection_of_object_values(Manifest)),
            "operations": lambda n : setattr(self, 'operations', n.get_collection_of_object_values(Operation)),
            "reconciliation": lambda n : setattr(self, 'reconciliation', n.get_object_value(BillingReconciliation)),
            "usage": lambda n : setattr(self, 'usage', n.get_object_value(AzureUsage)),
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
        writer.write_collection_of_object_values("manifests", self.manifests)
        writer.write_collection_of_object_values("operations", self.operations)
        writer.write_object_value("reconciliation", self.reconciliation)
        writer.write_object_value("usage", self.usage)
    

