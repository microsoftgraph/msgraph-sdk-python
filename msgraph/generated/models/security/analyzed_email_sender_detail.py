from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class AnalyzedEmailSenderDetail(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Display name of sender from address.
    display_name: Optional[str] = None
    # Date and time of creation of the sender domain.
    domain_creation_date_time: Optional[datetime.datetime] = None
    # Registered name of the domain.
    domain_name: Optional[str] = None
    # Owner of the domain.
    domain_owner: Optional[str] = None
    # The sender email address in the mail From header, also known as the envelope sender or the P1 sender.
    from_address: Optional[str] = None
    # The IPv4 address of the last detected mail server that relayed the message.
    ipv4: Optional[str] = None
    # Location of the domain.
    location: Optional[str] = None
    # The sender email address in the From header, which is visible to email recipients on their email clients. Also known as P2 sender.
    mail_from_address: Optional[str] = None
    # Domain name of sender mail from address.
    mail_from_domain_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AnalyzedEmailSenderDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AnalyzedEmailSenderDetail
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AnalyzedEmailSenderDetail()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "domainCreationDateTime": lambda n : setattr(self, 'domain_creation_date_time', n.get_datetime_value()),
            "domainName": lambda n : setattr(self, 'domain_name', n.get_str_value()),
            "domainOwner": lambda n : setattr(self, 'domain_owner', n.get_str_value()),
            "fromAddress": lambda n : setattr(self, 'from_address', n.get_str_value()),
            "ipv4": lambda n : setattr(self, 'ipv4', n.get_str_value()),
            "location": lambda n : setattr(self, 'location', n.get_str_value()),
            "mailFromAddress": lambda n : setattr(self, 'mail_from_address', n.get_str_value()),
            "mailFromDomainName": lambda n : setattr(self, 'mail_from_domain_name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("domainCreationDateTime", self.domain_creation_date_time)
        writer.write_str_value("domainName", self.domain_name)
        writer.write_str_value("domainOwner", self.domain_owner)
        writer.write_str_value("fromAddress", self.from_address)
        writer.write_str_value("ipv4", self.ipv4)
        writer.write_str_value("location", self.location)
        writer.write_str_value("mailFromAddress", self.mail_from_address)
        writer.write_str_value("mailFromDomainName", self.mail_from_domain_name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

