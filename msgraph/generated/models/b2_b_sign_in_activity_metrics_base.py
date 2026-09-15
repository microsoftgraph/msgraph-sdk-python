from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .b2_b_sign_in_activity_metrics_initial import B2BSignInActivityMetricsInitial
    from .b2_b_sign_in_activity_metrics_recent import B2BSignInActivityMetricsRecent
    from .entity import Entity

from .entity import Entity

@dataclass
class B2BSignInActivityMetricsBase(Entity, Parsable):
    # The inboundMonthlyTotalApplications property
    inbound_monthly_total_applications: Optional[float] = None
    # The inboundMonthlyTotalUsers property
    inbound_monthly_total_users: Optional[float] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The outboundMonthlyTotalApplications property
    outbound_monthly_total_applications: Optional[float] = None
    # The outboundMonthlyTotalUsers property
    outbound_monthly_total_users: Optional[float] = None
    # The watermarkDateTime property
    watermark_date_time: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> B2BSignInActivityMetricsBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: B2BSignInActivityMetricsBase
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.b2BSignInActivityMetricsInitial".casefold():
            from .b2_b_sign_in_activity_metrics_initial import B2BSignInActivityMetricsInitial

            return B2BSignInActivityMetricsInitial()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.b2BSignInActivityMetricsRecent".casefold():
            from .b2_b_sign_in_activity_metrics_recent import B2BSignInActivityMetricsRecent

            return B2BSignInActivityMetricsRecent()
        return B2BSignInActivityMetricsBase()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .b2_b_sign_in_activity_metrics_initial import B2BSignInActivityMetricsInitial
        from .b2_b_sign_in_activity_metrics_recent import B2BSignInActivityMetricsRecent
        from .entity import Entity

        from .b2_b_sign_in_activity_metrics_initial import B2BSignInActivityMetricsInitial
        from .b2_b_sign_in_activity_metrics_recent import B2BSignInActivityMetricsRecent
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "inboundMonthlyTotalApplications": lambda n : setattr(self, 'inbound_monthly_total_applications', n.get_float_value()),
            "inboundMonthlyTotalUsers": lambda n : setattr(self, 'inbound_monthly_total_users', n.get_float_value()),
            "outboundMonthlyTotalApplications": lambda n : setattr(self, 'outbound_monthly_total_applications', n.get_float_value()),
            "outboundMonthlyTotalUsers": lambda n : setattr(self, 'outbound_monthly_total_users', n.get_float_value()),
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
        writer.write_float_value("inboundMonthlyTotalUsers", self.inbound_monthly_total_users)
        writer.write_float_value("outboundMonthlyTotalApplications", self.outbound_monthly_total_applications)
        writer.write_float_value("outboundMonthlyTotalUsers", self.outbound_monthly_total_users)
        writer.write_datetime_value("watermarkDateTime", self.watermark_date_time)
    

