from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, Union

from . import entity

class BookingCurrency(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new BookingCurrency and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.bookingCurrency"
        # The currency symbol. For example, the currency symbol for the US dollar and for the Australian dollar is $.
        self._symbol: Optional[str] = None

    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BookingCurrency:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: BookingCurrency
        """
        if not parse_node:
            raise Exception("parse_node cannot be undefined")
        return BookingCurrency()

    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "symbol": lambda n : setattr(self, 'symbol', n.get_str_value()),
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
        if not writer:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("symbol", self.symbol)

    @property
    def symbol(self,) -> Optional[str]:
        """
        Gets the symbol property value. The currency symbol. For example, the currency symbol for the US dollar and for the Australian dollar is $.
        Returns: Optional[str]
        """
        return self._symbol

    @symbol.setter
    def symbol(self,value: Optional[str] = None) -> None:
        """
        Sets the symbol property value. The currency symbol. For example, the currency symbol for the US dollar and for the Australian dollar is $.
        Args:
            value: Value to set for the symbol property.
        """
        self._symbol = value


