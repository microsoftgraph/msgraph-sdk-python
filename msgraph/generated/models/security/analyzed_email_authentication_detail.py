from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class AnalyzedEmailAuthenticationDetail(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # A value used by Microsoft 365 to combine email authentication such as SPF, DKIM, and DMARC, to determine whether the message is authentic.
    composite_authentication: Optional[str] = None
    # DomainKeys identified mail (DKIM). Indicates whether it was pass/fail/soft fail.
    dkim: Optional[str] = None
    # Domain-based Message Authentication. Indicates whether it was pass/fail/soft fail.
    dmarc: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Sender Policy Framework (SPF). Indicates whether it was pass/fail/soft fail.
    sender_policy_framework: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AnalyzedEmailAuthenticationDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AnalyzedEmailAuthenticationDetail
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AnalyzedEmailAuthenticationDetail()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "compositeAuthentication": lambda n : setattr(self, 'composite_authentication', n.get_str_value()),
            "dkim": lambda n : setattr(self, 'dkim', n.get_str_value()),
            "dmarc": lambda n : setattr(self, 'dmarc', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "senderPolicyFramework": lambda n : setattr(self, 'sender_policy_framework', n.get_str_value()),
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
        writer.write_str_value("compositeAuthentication", self.composite_authentication)
        writer.write_str_value("dkim", self.dkim)
        writer.write_str_value("dmarc", self.dmarc)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("senderPolicyFramework", self.sender_policy_framework)
        writer.write_additional_data_value(self.additional_data)
    

