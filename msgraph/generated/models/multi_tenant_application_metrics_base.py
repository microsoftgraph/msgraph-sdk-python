from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .multi_tenant_application_metrics_initial import MultiTenantApplicationMetricsInitial
    from .multi_tenant_application_metrics_recent import MultiTenantApplicationMetricsRecent

from .entity import Entity

@dataclass
class MultiTenantApplicationMetricsBase(Entity, Parsable):
    # The inboundMonthlyTotalApplications property
    inbound_monthly_total_applications: Optional[float] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The outboundMonthlyTotalApplications property
    outbound_monthly_total_applications: Optional[float] = None
    # The watermarkDateTime property
    watermark_date_time: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MultiTenantApplicationMetricsBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MultiTenantApplicationMetricsBase
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.multiTenantApplicationMetricsInitial".casefold():
            from .multi_tenant_application_metrics_initial import MultiTenantApplicationMetricsInitial

            return MultiTenantApplicationMetricsInitial()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.multiTenantApplicationMetricsRecent".casefold():
            from .multi_tenant_application_metrics_recent import MultiTenantApplicationMetricsRecent

            return MultiTenantApplicationMetricsRecent()
        return MultiTenantApplicationMetricsBase()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .multi_tenant_application_metrics_initial import MultiTenantApplicationMetricsInitial
        from .multi_tenant_application_metrics_recent import MultiTenantApplicationMetricsRecent

        from .entity import Entity
        from .multi_tenant_application_metrics_initial import MultiTenantApplicationMetricsInitial
        from .multi_tenant_application_metrics_recent import MultiTenantApplicationMetricsRecent

        fields: dict[str, Callable[[Any], None]] = {
            "inboundMonthlyTotalApplications": lambda n : setattr(self, 'inbound_monthly_total_applications', n.get_float_value()),
            "outboundMonthlyTotalApplications": lambda n : setattr(self, 'outbound_monthly_total_applications', n.get_float_value()),
            "watermarkDateTime": lambda n : setattr(self, 'watermark_date_time', n.get_datetime_value()),
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
        writer.write_float_value("inboundMonthlyTotalApplications", self.inbound_monthly_total_applications)
        writer.write_float_value("outboundMonthlyTotalApplications", self.outbound_monthly_total_applications)
        writer.write_datetime_value("watermarkDateTime", self.watermark_date_time)
    

