from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .entity import Entity
    from .service_plan_info import ServicePlanInfo

from .entity import Entity

@dataclass
class LicenseDetails(Entity):
    # The OdataType property
    odata_type: Optional[str] = None
    # Information about the service plans assigned with the license. Read-only. Not nullable.
    service_plans: Optional[List[ServicePlanInfo]] = None
    # Unique identifier (GUID) for the service SKU. Equal to the skuId property on the related subscribedSku object. Read-only.
    sku_id: Optional[UUID] = None
    # Unique SKU display name. Equal to the skuPartNumber on the related subscribedSku object; for example, AAD_Premium. Read-only.
    sku_part_number: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LicenseDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LicenseDetails
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LicenseDetails()
    
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
            "servicePlans": lambda n : setattr(self, 'service_plans', n.get_collection_of_object_values(ServicePlanInfo)),
            "skuId": lambda n : setattr(self, 'sku_id', n.get_uuid_value()),
            "skuPartNumber": lambda n : setattr(self, 'sku_part_number', n.get_str_value()),
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
        writer.write_collection_of_object_values("servicePlans", self.service_plans)
        writer.write_uuid_value("skuId", self.sku_id)
        writer.write_str_value("skuPartNumber", self.sku_part_number)
    

