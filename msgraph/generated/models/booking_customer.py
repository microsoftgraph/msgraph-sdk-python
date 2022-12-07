from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

booking_customer_base = lazy_import('msgraph.generated.models.booking_customer_base')
phone = lazy_import('msgraph.generated.models.phone')
physical_address = lazy_import('msgraph.generated.models.physical_address')

class BookingCustomer(booking_customer_base.BookingCustomerBase):
    @property
    def addresses(self,) -> Optional[List[physical_address.PhysicalAddress]]:
        """
        Gets the addresses property value. Addresses associated with the customer. The attribute type of physicalAddress is not supported in v1.0. Internally we map the addresses to the type others.
        Returns: Optional[List[physical_address.PhysicalAddress]]
        """
        return self._addresses
    
    @addresses.setter
    def addresses(self,value: Optional[List[physical_address.PhysicalAddress]] = None) -> None:
        """
        Sets the addresses property value. Addresses associated with the customer. The attribute type of physicalAddress is not supported in v1.0. Internally we map the addresses to the type others.
        Args:
            value: Value to set for the addresses property.
        """
        self._addresses = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new BookingCustomer and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.bookingCustomer"
        # Addresses associated with the customer. The attribute type of physicalAddress is not supported in v1.0. Internally we map the addresses to the type others.
        self._addresses: Optional[List[physical_address.PhysicalAddress]] = None
        # The name of the customer.
        self._display_name: Optional[str] = None
        # The SMTP address of the customer.
        self._email_address: Optional[str] = None
        # Phone numbers associated with the customer, including home, business and mobile numbers.
        self._phones: Optional[List[phone.Phone]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BookingCustomer:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: BookingCustomer
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return BookingCustomer()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The name of the customer.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The name of the customer.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def email_address(self,) -> Optional[str]:
        """
        Gets the emailAddress property value. The SMTP address of the customer.
        Returns: Optional[str]
        """
        return self._email_address
    
    @email_address.setter
    def email_address(self,value: Optional[str] = None) -> None:
        """
        Sets the emailAddress property value. The SMTP address of the customer.
        Args:
            value: Value to set for the emailAddress property.
        """
        self._email_address = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "addresses": lambda n : setattr(self, 'addresses', n.get_collection_of_object_values(physical_address.PhysicalAddress)),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "email_address": lambda n : setattr(self, 'email_address', n.get_str_value()),
            "phones": lambda n : setattr(self, 'phones', n.get_collection_of_object_values(phone.Phone)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def phones(self,) -> Optional[List[phone.Phone]]:
        """
        Gets the phones property value. Phone numbers associated with the customer, including home, business and mobile numbers.
        Returns: Optional[List[phone.Phone]]
        """
        return self._phones
    
    @phones.setter
    def phones(self,value: Optional[List[phone.Phone]] = None) -> None:
        """
        Sets the phones property value. Phone numbers associated with the customer, including home, business and mobile numbers.
        Args:
            value: Value to set for the phones property.
        """
        self._phones = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("addresses", self.addresses)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("emailAddress", self.email_address)
        writer.write_collection_of_object_values("phones", self.phones)
    

