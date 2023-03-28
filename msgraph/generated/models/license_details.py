from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from . import entity, service_plan_info

from . import entity

class LicenseDetails(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new licenseDetails and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Information about the service plans assigned with the license. Read-only, Not nullable
        self._service_plans: Optional[List[service_plan_info.ServicePlanInfo]] = None
        # Unique identifier (GUID) for the service SKU. Equal to the skuId property on the related SubscribedSku object. Read-only
        self._sku_id: Optional[UUID] = None
        # Unique SKU display name. Equal to the skuPartNumber on the related SubscribedSku object; for example: 'AAD_Premium'. Read-only
        self._sku_part_number: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> LicenseDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: LicenseDetails
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return LicenseDetails()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, service_plan_info

        fields: Dict[str, Callable[[Any], None]] = {
            "servicePlans": lambda n : setattr(self, 'service_plans', n.get_collection_of_object_values(service_plan_info.ServicePlanInfo)),
            "skuId": lambda n : setattr(self, 'sku_id', n.get_uuid_value()),
            "skuPartNumber": lambda n : setattr(self, 'sku_part_number', n.get_str_value()),
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
        writer.write_collection_of_object_values("servicePlans", self.service_plans)
        writer.write_uuid_value("skuId", self.sku_id)
        writer.write_str_value("skuPartNumber", self.sku_part_number)
    
    @property
    def service_plans(self,) -> Optional[List[service_plan_info.ServicePlanInfo]]:
        """
        Gets the servicePlans property value. Information about the service plans assigned with the license. Read-only, Not nullable
        Returns: Optional[List[service_plan_info.ServicePlanInfo]]
        """
        return self._service_plans
    
    @service_plans.setter
    def service_plans(self,value: Optional[List[service_plan_info.ServicePlanInfo]] = None) -> None:
        """
        Sets the servicePlans property value. Information about the service plans assigned with the license. Read-only, Not nullable
        Args:
            value: Value to set for the service_plans property.
        """
        self._service_plans = value
    
    @property
    def sku_id(self,) -> Optional[UUID]:
        """
        Gets the skuId property value. Unique identifier (GUID) for the service SKU. Equal to the skuId property on the related SubscribedSku object. Read-only
        Returns: Optional[UUID]
        """
        return self._sku_id
    
    @sku_id.setter
    def sku_id(self,value: Optional[UUID] = None) -> None:
        """
        Sets the skuId property value. Unique identifier (GUID) for the service SKU. Equal to the skuId property on the related SubscribedSku object. Read-only
        Args:
            value: Value to set for the sku_id property.
        """
        self._sku_id = value
    
    @property
    def sku_part_number(self,) -> Optional[str]:
        """
        Gets the skuPartNumber property value. Unique SKU display name. Equal to the skuPartNumber on the related SubscribedSku object; for example: 'AAD_Premium'. Read-only
        Returns: Optional[str]
        """
        return self._sku_part_number
    
    @sku_part_number.setter
    def sku_part_number(self,value: Optional[str] = None) -> None:
        """
        Sets the skuPartNumber property value. Unique SKU display name. Equal to the skuPartNumber on the related SubscribedSku object; for example: 'AAD_Premium'. Read-only
        Args:
            value: Value to set for the sku_part_number property.
        """
        self._sku_part_number = value
    

