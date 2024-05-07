from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .service_plan_info import ServicePlanInfo

from .entity import Entity

@dataclass
class CompanySubscription(Entity):
    # The commerceSubscriptionId property
    commerce_subscription_id: Optional[str] = None
    # The createdDateTime property
    created_date_time: Optional[datetime.datetime] = None
    # The isTrial property
    is_trial: Optional[bool] = None
    # The nextLifecycleDateTime property
    next_lifecycle_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The ownerId property
    owner_id: Optional[str] = None
    # The ownerTenantId property
    owner_tenant_id: Optional[str] = None
    # The ownerType property
    owner_type: Optional[str] = None
    # The serviceStatus property
    service_status: Optional[List[ServicePlanInfo]] = None
    # The skuId property
    sku_id: Optional[str] = None
    # The skuPartNumber property
    sku_part_number: Optional[str] = None
    # The status property
    status: Optional[str] = None
    # The totalLicenses property
    total_licenses: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CompanySubscription:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CompanySubscription
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return CompanySubscription()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .service_plan_info import ServicePlanInfo

        from .entity import Entity
        from .service_plan_info import ServicePlanInfo

        fields: Dict[str, Callable[[Any], None]] = {
            "commerceSubscriptionId": lambda n : setattr(self, 'commerce_subscription_id', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "isTrial": lambda n : setattr(self, 'is_trial', n.get_bool_value()),
            "nextLifecycleDateTime": lambda n : setattr(self, 'next_lifecycle_date_time', n.get_datetime_value()),
            "ownerId": lambda n : setattr(self, 'owner_id', n.get_str_value()),
            "ownerTenantId": lambda n : setattr(self, 'owner_tenant_id', n.get_str_value()),
            "ownerType": lambda n : setattr(self, 'owner_type', n.get_str_value()),
            "serviceStatus": lambda n : setattr(self, 'service_status', n.get_collection_of_object_values(ServicePlanInfo)),
            "skuId": lambda n : setattr(self, 'sku_id', n.get_str_value()),
            "skuPartNumber": lambda n : setattr(self, 'sku_part_number', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
            "totalLicenses": lambda n : setattr(self, 'total_licenses', n.get_int_value()),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("commerceSubscriptionId", self.commerce_subscription_id)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_bool_value("isTrial", self.is_trial)
        writer.write_datetime_value("nextLifecycleDateTime", self.next_lifecycle_date_time)
        writer.write_str_value("ownerId", self.owner_id)
        writer.write_str_value("ownerTenantId", self.owner_tenant_id)
        writer.write_str_value("ownerType", self.owner_type)
        writer.write_collection_of_object_values("serviceStatus", self.service_status)
        writer.write_str_value("skuId", self.sku_id)
        writer.write_str_value("skuPartNumber", self.sku_part_number)
        writer.write_str_value("status", self.status)
        writer.write_int_value("totalLicenses", self.total_licenses)
    

