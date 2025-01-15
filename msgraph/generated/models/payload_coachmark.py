from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .coachmark_location import CoachmarkLocation

@dataclass
class PayloadCoachmark(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The coachmark location.
    coachmark_location: Optional[CoachmarkLocation] = None
    # The description about the coachmark.
    description: Optional[str] = None
    # The coachmark indicator.
    indicator: Optional[str] = None
    # Indicates whether the coachmark is valid or not.
    is_valid: Optional[bool] = None
    # The coachmark language.
    language: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The coachmark order.
    order: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PayloadCoachmark:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PayloadCoachmark
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PayloadCoachmark()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .coachmark_location import CoachmarkLocation

        from .coachmark_location import CoachmarkLocation

        fields: dict[str, Callable[[Any], None]] = {
            "coachmarkLocation": lambda n : setattr(self, 'coachmark_location', n.get_object_value(CoachmarkLocation)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "indicator": lambda n : setattr(self, 'indicator', n.get_str_value()),
            "isValid": lambda n : setattr(self, 'is_valid', n.get_bool_value()),
            "language": lambda n : setattr(self, 'language', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "order": lambda n : setattr(self, 'order', n.get_str_value()),
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
        writer.write_object_value("coachmarkLocation", self.coachmark_location)
        writer.write_str_value("description", self.description)
        writer.write_str_value("indicator", self.indicator)
        writer.write_bool_value("isValid", self.is_valid)
        writer.write_str_value("language", self.language)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("order", self.order)
        writer.write_additional_data_value(self.additional_data)
    

