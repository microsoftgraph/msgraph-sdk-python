from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

domain_dns_record = lazy_import('msgraph.generated.models.domain_dns_record')

class DomainDnsMxRecord(domain_dns_record.DomainDnsRecord):
    def __init__(self,) -> None:
        """
        Instantiates a new DomainDnsMxRecord and sets the default values.
        """
        super().__init__()
        # Value used when configuring the answer/destination/value of the MX record at the DNS host.
        self._mail_exchange: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Value used when configuring the Preference/Priority property of the MX record at the DNS host.
        self._preference: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DomainDnsMxRecord:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DomainDnsMxRecord
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DomainDnsMxRecord()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "mail_exchange": lambda n : setattr(self, 'mail_exchange', n.get_str_value()),
            "preference": lambda n : setattr(self, 'preference', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def mail_exchange(self,) -> Optional[str]:
        """
        Gets the mailExchange property value. Value used when configuring the answer/destination/value of the MX record at the DNS host.
        Returns: Optional[str]
        """
        return self._mail_exchange
    
    @mail_exchange.setter
    def mail_exchange(self,value: Optional[str] = None) -> None:
        """
        Sets the mailExchange property value. Value used when configuring the answer/destination/value of the MX record at the DNS host.
        Args:
            value: Value to set for the mailExchange property.
        """
        self._mail_exchange = value
    
    @property
    def preference(self,) -> Optional[int]:
        """
        Gets the preference property value. Value used when configuring the Preference/Priority property of the MX record at the DNS host.
        Returns: Optional[int]
        """
        return self._preference
    
    @preference.setter
    def preference(self,value: Optional[int] = None) -> None:
        """
        Sets the preference property value. Value used when configuring the Preference/Priority property of the MX record at the DNS host.
        Args:
            value: Value to set for the preference property.
        """
        self._preference = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("mailExchange", self.mail_exchange)
        writer.write_int_value("preference", self.preference)
    

