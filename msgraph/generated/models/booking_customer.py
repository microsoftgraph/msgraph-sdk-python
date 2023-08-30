from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .booking_customer_base import BookingCustomerBase
    from .phone import Phone
    from .physical_address import PhysicalAddress

from .booking_customer_base import BookingCustomerBase

@dataclass
class BookingCustomer(BookingCustomerBase):
    """
    Represents a customer of the business.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.bookingCustomer"
    # Addresses associated with the customer. The attribute type of physicalAddress is not supported in v1.0. Internally we map the addresses to the type others.
    addresses: Optional[List[PhysicalAddress]] = None
    # The name of the customer.
    display_name: Optional[str] = None
    # The SMTP address of the customer.
    email_address: Optional[str] = None
    # Phone numbers associated with the customer, including home, business and mobile numbers.
    phones: Optional[List[Phone]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BookingCustomer:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BookingCustomer
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return BookingCustomer()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .booking_customer_base import BookingCustomerBase
        from .phone import Phone
        from .physical_address import PhysicalAddress

        from .booking_customer_base import BookingCustomerBase
        from .phone import Phone
        from .physical_address import PhysicalAddress

        fields: Dict[str, Callable[[Any], None]] = {
            "addresses": lambda n : setattr(self, 'addresses', n.get_collection_of_object_values(PhysicalAddress)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "emailAddress": lambda n : setattr(self, 'email_address', n.get_str_value()),
            "phones": lambda n : setattr(self, 'phones', n.get_collection_of_object_values(Phone)),
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
        writer.write_collection_of_object_values("addresses", self.addresses)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("emailAddress", self.email_address)
        writer.write_collection_of_object_values("phones", self.phones)
    

