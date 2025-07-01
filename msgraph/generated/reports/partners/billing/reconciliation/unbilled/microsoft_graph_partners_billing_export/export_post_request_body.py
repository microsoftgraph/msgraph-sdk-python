from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .......models.partners.billing.attribute_set import AttributeSet
    from .......models.partners.billing.billing_period import BillingPeriod

@dataclass
class ExportPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The attributeSet property
    attribute_set: Optional[AttributeSet] = None
    # The billingPeriod property
    billing_period: Optional[BillingPeriod] = None
    # The currencyCode property
    currency_code: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ExportPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ExportPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ExportPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .......models.partners.billing.attribute_set import AttributeSet
        from .......models.partners.billing.billing_period import BillingPeriod

        from .......models.partners.billing.attribute_set import AttributeSet
        from .......models.partners.billing.billing_period import BillingPeriod

        fields: dict[str, Callable[[Any], None]] = {
            "attributeSet": lambda n : setattr(self, 'attribute_set', n.get_enum_value(AttributeSet)),
            "billingPeriod": lambda n : setattr(self, 'billing_period', n.get_enum_value(BillingPeriod)),
            "currencyCode": lambda n : setattr(self, 'currency_code', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_enum_value("attributeSet", self.attribute_set)
        writer.write_enum_value("billingPeriod", self.billing_period)
        writer.write_str_value("currencyCode", self.currency_code)
        writer.write_additional_data_value(self.additional_data)
    

