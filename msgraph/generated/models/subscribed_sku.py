from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .entity import Entity
    from .license_units_detail import LicenseUnitsDetail
    from .service_plan_info import ServicePlanInfo

from .entity import Entity

@dataclass
class SubscribedSku(Entity):
    # The unique ID of the account this SKU belongs to.
    account_id: Optional[str] = None
    # The name of the account this SKU belongs to.
    account_name: Optional[str] = None
    # The target class for this SKU. Only SKUs with target class User are assignable. Possible values are: 'User', 'Company'.
    applies_to: Optional[str] = None
    # Enabled indicates that the prepaidUnits property has at least one unit that is enabled. LockedOut indicates that the customer canceled their subscription. Possible values are: Enabled, Warning, Suspended, Deleted, LockedOut.
    capability_status: Optional[str] = None
    # The number of licenses that have been assigned.
    consumed_units: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Information about the number and status of prepaid licenses.
    prepaid_units: Optional[LicenseUnitsDetail] = None
    # Information about the service plans that are available with the SKU. Not nullable.
    service_plans: Optional[List[ServicePlanInfo]] = None
    # The unique identifier (GUID) for the service SKU.
    sku_id: Optional[UUID] = None
    # The SKU part number; for example: 'AAD_PREMIUM' or 'RMSBASIC'. To get a list of commercial subscriptions that an organization has acquired, see List subscribedSkus.
    sku_part_number: Optional[str] = None
    # The subscriptionIds property
    subscription_ids: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SubscribedSku:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SubscribedSku
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return SubscribedSku()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .license_units_detail import LicenseUnitsDetail
        from .service_plan_info import ServicePlanInfo

        from .entity import Entity
        from .license_units_detail import LicenseUnitsDetail
        from .service_plan_info import ServicePlanInfo

        fields: Dict[str, Callable[[Any], None]] = {
            "account_id": lambda n : setattr(self, 'account_id', n.get_str_value()),
            "account_name": lambda n : setattr(self, 'account_name', n.get_str_value()),
            "applies_to": lambda n : setattr(self, 'applies_to', n.get_str_value()),
            "capability_status": lambda n : setattr(self, 'capability_status', n.get_str_value()),
            "consumed_units": lambda n : setattr(self, 'consumed_units', n.get_int_value()),
            "prepaid_units": lambda n : setattr(self, 'prepaid_units', n.get_object_value(LicenseUnitsDetail)),
            "service_plans": lambda n : setattr(self, 'service_plans', n.get_collection_of_object_values(ServicePlanInfo)),
            "sku_id": lambda n : setattr(self, 'sku_id', n.get_uuid_value()),
            "sku_part_number": lambda n : setattr(self, 'sku_part_number', n.get_str_value()),
            "subscription_ids": lambda n : setattr(self, 'subscription_ids', n.get_collection_of_primitive_values(str)),
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
        writer.write_str_value("account_id", self.account_id)
        writer.write_str_value("account_name", self.account_name)
        writer.write_str_value("applies_to", self.applies_to)
        writer.write_str_value("capability_status", self.capability_status)
        writer.write_int_value("consumed_units", self.consumed_units)
        writer.write_object_value("prepaid_units", self.prepaid_units)
        writer.write_collection_of_object_values("service_plans", self.service_plans)
        writer.write_uuid_value("sku_id", self.sku_id)
        writer.write_str_value("sku_part_number", self.sku_part_number)
        writer.write_collection_of_primitive_values("subscription_ids", self.subscription_ids)
    

