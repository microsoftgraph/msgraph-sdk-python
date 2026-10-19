from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .billing_metrics_initial import BillingMetricsInitial
    from .billing_metrics_recent import BillingMetricsRecent
    from .entity import Entity

from .entity import Entity

@dataclass
class BillingMetrics(Entity, Parsable):
    # The initial property
    initial: Optional[BillingMetricsInitial] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The recent property
    recent: Optional[BillingMetricsRecent] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BillingMetrics:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BillingMetrics
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return BillingMetrics()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .billing_metrics_initial import BillingMetricsInitial
        from .billing_metrics_recent import BillingMetricsRecent
        from .entity import Entity

        from .billing_metrics_initial import BillingMetricsInitial
        from .billing_metrics_recent import BillingMetricsRecent
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "initial": lambda n : setattr(self, 'initial', n.get_object_value(BillingMetricsInitial)),
            "recent": lambda n : setattr(self, 'recent', n.get_object_value(BillingMetricsRecent)),
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
        writer.write_object_value("initial", self.initial)
        writer.write_object_value("recent", self.recent)
    

