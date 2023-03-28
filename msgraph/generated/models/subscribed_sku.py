from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from . import entity, license_units_detail, service_plan_info

from . import entity

class SubscribedSku(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new SubscribedSku and sets the default values.
        """
        super().__init__()
        # For example, 'User' or 'Company'.
        self._applies_to: Optional[str] = None
        # Possible values are: Enabled, Warning, Suspended, Deleted, LockedOut. The capabilityStatus is Enabled if the prepaidUnits property has at least 1 unit that is enabled, and LockedOut if the customer cancelled their subscription.
        self._capability_status: Optional[str] = None
        # The number of licenses that have been assigned.
        self._consumed_units: Optional[int] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Information about the number and status of prepaid licenses.
        self._prepaid_units: Optional[license_units_detail.LicenseUnitsDetail] = None
        # Information about the service plans that are available with the SKU. Not nullable
        self._service_plans: Optional[List[service_plan_info.ServicePlanInfo]] = None
        # The unique identifier (GUID) for the service SKU.
        self._sku_id: Optional[UUID] = None
        # The SKU part number; for example: 'AAD_PREMIUM' or 'RMSBASIC'. To get a list of commercial subscriptions that an organization has acquired, see List subscribedSkus.
        self._sku_part_number: Optional[str] = None
    
    @property
    def applies_to(self,) -> Optional[str]:
        """
        Gets the appliesTo property value. For example, 'User' or 'Company'.
        Returns: Optional[str]
        """
        return self._applies_to
    
    @applies_to.setter
    def applies_to(self,value: Optional[str] = None) -> None:
        """
        Sets the appliesTo property value. For example, 'User' or 'Company'.
        Args:
            value: Value to set for the applies_to property.
        """
        self._applies_to = value
    
    @property
    def capability_status(self,) -> Optional[str]:
        """
        Gets the capabilityStatus property value. Possible values are: Enabled, Warning, Suspended, Deleted, LockedOut. The capabilityStatus is Enabled if the prepaidUnits property has at least 1 unit that is enabled, and LockedOut if the customer cancelled their subscription.
        Returns: Optional[str]
        """
        return self._capability_status
    
    @capability_status.setter
    def capability_status(self,value: Optional[str] = None) -> None:
        """
        Sets the capabilityStatus property value. Possible values are: Enabled, Warning, Suspended, Deleted, LockedOut. The capabilityStatus is Enabled if the prepaidUnits property has at least 1 unit that is enabled, and LockedOut if the customer cancelled their subscription.
        Args:
            value: Value to set for the capability_status property.
        """
        self._capability_status = value
    
    @property
    def consumed_units(self,) -> Optional[int]:
        """
        Gets the consumedUnits property value. The number of licenses that have been assigned.
        Returns: Optional[int]
        """
        return self._consumed_units
    
    @consumed_units.setter
    def consumed_units(self,value: Optional[int] = None) -> None:
        """
        Sets the consumedUnits property value. The number of licenses that have been assigned.
        Args:
            value: Value to set for the consumed_units property.
        """
        self._consumed_units = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SubscribedSku:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SubscribedSku
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SubscribedSku()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, license_units_detail, service_plan_info

        fields: Dict[str, Callable[[Any], None]] = {
            "appliesTo": lambda n : setattr(self, 'applies_to', n.get_str_value()),
            "capabilityStatus": lambda n : setattr(self, 'capability_status', n.get_str_value()),
            "consumedUnits": lambda n : setattr(self, 'consumed_units', n.get_int_value()),
            "prepaidUnits": lambda n : setattr(self, 'prepaid_units', n.get_object_value(license_units_detail.LicenseUnitsDetail)),
            "servicePlans": lambda n : setattr(self, 'service_plans', n.get_collection_of_object_values(service_plan_info.ServicePlanInfo)),
            "skuId": lambda n : setattr(self, 'sku_id', n.get_uuid_value()),
            "skuPartNumber": lambda n : setattr(self, 'sku_part_number', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def prepaid_units(self,) -> Optional[license_units_detail.LicenseUnitsDetail]:
        """
        Gets the prepaidUnits property value. Information about the number and status of prepaid licenses.
        Returns: Optional[license_units_detail.LicenseUnitsDetail]
        """
        return self._prepaid_units
    
    @prepaid_units.setter
    def prepaid_units(self,value: Optional[license_units_detail.LicenseUnitsDetail] = None) -> None:
        """
        Sets the prepaidUnits property value. Information about the number and status of prepaid licenses.
        Args:
            value: Value to set for the prepaid_units property.
        """
        self._prepaid_units = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("appliesTo", self.applies_to)
        writer.write_str_value("capabilityStatus", self.capability_status)
        writer.write_int_value("consumedUnits", self.consumed_units)
        writer.write_object_value("prepaidUnits", self.prepaid_units)
        writer.write_collection_of_object_values("servicePlans", self.service_plans)
        writer.write_uuid_value("skuId", self.sku_id)
        writer.write_str_value("skuPartNumber", self.sku_part_number)
    
    @property
    def service_plans(self,) -> Optional[List[service_plan_info.ServicePlanInfo]]:
        """
        Gets the servicePlans property value. Information about the service plans that are available with the SKU. Not nullable
        Returns: Optional[List[service_plan_info.ServicePlanInfo]]
        """
        return self._service_plans
    
    @service_plans.setter
    def service_plans(self,value: Optional[List[service_plan_info.ServicePlanInfo]] = None) -> None:
        """
        Sets the servicePlans property value. Information about the service plans that are available with the SKU. Not nullable
        Args:
            value: Value to set for the service_plans property.
        """
        self._service_plans = value
    
    @property
    def sku_id(self,) -> Optional[UUID]:
        """
        Gets the skuId property value. The unique identifier (GUID) for the service SKU.
        Returns: Optional[UUID]
        """
        return self._sku_id
    
    @sku_id.setter
    def sku_id(self,value: Optional[UUID] = None) -> None:
        """
        Sets the skuId property value. The unique identifier (GUID) for the service SKU.
        Args:
            value: Value to set for the sku_id property.
        """
        self._sku_id = value
    
    @property
    def sku_part_number(self,) -> Optional[str]:
        """
        Gets the skuPartNumber property value. The SKU part number; for example: 'AAD_PREMIUM' or 'RMSBASIC'. To get a list of commercial subscriptions that an organization has acquired, see List subscribedSkus.
        Returns: Optional[str]
        """
        return self._sku_part_number
    
    @sku_part_number.setter
    def sku_part_number(self,value: Optional[str] = None) -> None:
        """
        Sets the skuPartNumber property value. The SKU part number; for example: 'AAD_PREMIUM' or 'RMSBASIC'. To get a list of commercial subscriptions that an organization has acquired, see List subscribedSkus.
        Args:
            value: Value to set for the sku_part_number property.
        """
        self._sku_part_number = value
    

