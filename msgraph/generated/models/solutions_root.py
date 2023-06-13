from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import booking_business, booking_currency

@dataclass
class SolutionsRoot(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The bookingBusinesses property
    booking_businesses: Optional[List[booking_business.BookingBusiness]] = None
    # The bookingCurrencies property
    booking_currencies: Optional[List[booking_currency.BookingCurrency]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SolutionsRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SolutionsRoot
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SolutionsRoot()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import booking_business, booking_currency

        fields: Dict[str, Callable[[Any], None]] = {
            "bookingBusinesses": lambda n : setattr(self, 'booking_businesses', n.get_collection_of_object_values(booking_business.BookingBusiness)),
            "bookingCurrencies": lambda n : setattr(self, 'booking_currencies', n.get_collection_of_object_values(booking_currency.BookingCurrency)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_object_values("bookingBusinesses", self.booking_businesses)
        writer.write_collection_of_object_values("bookingCurrencies", self.booking_currencies)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

