from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .b2b_registration_metrics import B2bRegistrationMetrics
    from .b2_b_sign_in_activity_metrics import B2BSignInActivityMetrics
    from .billing_metrics import BillingMetrics
    from .entity import Entity
    from .multi_tenant_application_metrics import MultiTenantApplicationMetrics

from .entity import Entity

@dataclass
class RelatedTenant(Entity, Parsable):
    # The appB2BSignInActivityMetrics property
    app_b2_b_sign_in_activity_metrics: Optional[B2BSignInActivityMetrics] = None
    # The b2BRegistrationMetrics property
    b2_b_registration_metrics: Optional[B2bRegistrationMetrics] = None
    # The b2BSignInActivityMetrics property
    b2_b_sign_in_activity_metrics: Optional[B2BSignInActivityMetrics] = None
    # The billingMetrics property
    billing_metrics: Optional[BillingMetrics] = None
    # The createdDateTime property
    created_date_time: Optional[datetime.datetime] = None
    # Indicates whether this tenant is a Microsoft infrastructure tenant.
    is_microsoft_infrastructure: Optional[bool] = None
    # The multiTenantApplicationMetrics property
    multi_tenant_application_metrics: Optional[MultiTenantApplicationMetrics] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RelatedTenant:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RelatedTenant
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RelatedTenant()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .b2b_registration_metrics import B2bRegistrationMetrics
        from .b2_b_sign_in_activity_metrics import B2BSignInActivityMetrics
        from .billing_metrics import BillingMetrics
        from .entity import Entity
        from .multi_tenant_application_metrics import MultiTenantApplicationMetrics

        from .b2b_registration_metrics import B2bRegistrationMetrics
        from .b2_b_sign_in_activity_metrics import B2BSignInActivityMetrics
        from .billing_metrics import BillingMetrics
        from .entity import Entity
        from .multi_tenant_application_metrics import MultiTenantApplicationMetrics

        fields: dict[str, Callable[[Any], None]] = {
            "appB2BSignInActivityMetrics": lambda n : setattr(self, 'app_b2_b_sign_in_activity_metrics', n.get_object_value(B2BSignInActivityMetrics)),
            "b2BRegistrationMetrics": lambda n : setattr(self, 'b2_b_registration_metrics', n.get_object_value(B2bRegistrationMetrics)),
            "b2BSignInActivityMetrics": lambda n : setattr(self, 'b2_b_sign_in_activity_metrics', n.get_object_value(B2BSignInActivityMetrics)),
            "billingMetrics": lambda n : setattr(self, 'billing_metrics', n.get_object_value(BillingMetrics)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "isMicrosoftInfrastructure": lambda n : setattr(self, 'is_microsoft_infrastructure', n.get_bool_value()),
            "multiTenantApplicationMetrics": lambda n : setattr(self, 'multi_tenant_application_metrics', n.get_object_value(MultiTenantApplicationMetrics)),
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
        writer.write_object_value("appB2BSignInActivityMetrics", self.app_b2_b_sign_in_activity_metrics)
        writer.write_object_value("b2BRegistrationMetrics", self.b2_b_registration_metrics)
        writer.write_object_value("b2BSignInActivityMetrics", self.b2_b_sign_in_activity_metrics)
        writer.write_object_value("billingMetrics", self.billing_metrics)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("multiTenantApplicationMetrics", self.multi_tenant_application_metrics)
    

