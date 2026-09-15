from __future__ import annotations
import datetime
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
class BillingMetricsBase(Entity, Parsable):
    # The foreignAssociatedTenantBillingManagementActiveCount property
    foreign_associated_tenant_billing_management_active_count: Optional[float] = None
    # The foreignAssociatedTenantCount property
    foreign_associated_tenant_count: Optional[float] = None
    # The foreignAssociatedTenantProvisioningActiveCount property
    foreign_associated_tenant_provisioning_active_count: Optional[float] = None
    # The localAssociatedTenantBillingManagementActiveCount property
    local_associated_tenant_billing_management_active_count: Optional[float] = None
    # The localAssociatedTenantCount property
    local_associated_tenant_count: Optional[float] = None
    # The localAssociatedTenantIds property
    local_associated_tenant_ids: Optional[list[str]] = None
    # The localAssociatedTenantProvisioningActiveCount property
    local_associated_tenant_provisioning_active_count: Optional[float] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The watermarkDateTime property
    watermark_date_time: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BillingMetricsBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BillingMetricsBase
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.billingMetricsInitial".casefold():
            from .billing_metrics_initial import BillingMetricsInitial

            return BillingMetricsInitial()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.billingMetricsRecent".casefold():
            from .billing_metrics_recent import BillingMetricsRecent

            return BillingMetricsRecent()
        return BillingMetricsBase()
    
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
            "foreignAssociatedTenantBillingManagementActiveCount": lambda n : setattr(self, 'foreign_associated_tenant_billing_management_active_count', n.get_float_value()),
            "foreignAssociatedTenantCount": lambda n : setattr(self, 'foreign_associated_tenant_count', n.get_float_value()),
            "foreignAssociatedTenantProvisioningActiveCount": lambda n : setattr(self, 'foreign_associated_tenant_provisioning_active_count', n.get_float_value()),
            "localAssociatedTenantBillingManagementActiveCount": lambda n : setattr(self, 'local_associated_tenant_billing_management_active_count', n.get_float_value()),
            "localAssociatedTenantCount": lambda n : setattr(self, 'local_associated_tenant_count', n.get_float_value()),
            "localAssociatedTenantIds": lambda n : setattr(self, 'local_associated_tenant_ids', n.get_collection_of_primitive_values(str)),
            "localAssociatedTenantProvisioningActiveCount": lambda n : setattr(self, 'local_associated_tenant_provisioning_active_count', n.get_float_value()),
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
        writer.write_float_value("foreignAssociatedTenantBillingManagementActiveCount", self.foreign_associated_tenant_billing_management_active_count)
        writer.write_float_value("foreignAssociatedTenantCount", self.foreign_associated_tenant_count)
        writer.write_float_value("foreignAssociatedTenantProvisioningActiveCount", self.foreign_associated_tenant_provisioning_active_count)
        writer.write_float_value("localAssociatedTenantBillingManagementActiveCount", self.local_associated_tenant_billing_management_active_count)
        writer.write_float_value("localAssociatedTenantCount", self.local_associated_tenant_count)
        writer.write_collection_of_primitive_values("localAssociatedTenantIds", self.local_associated_tenant_ids)
        writer.write_float_value("localAssociatedTenantProvisioningActiveCount", self.local_associated_tenant_provisioning_active_count)
        writer.write_datetime_value("watermarkDateTime", self.watermark_date_time)
    

