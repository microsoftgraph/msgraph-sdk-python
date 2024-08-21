from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .mailbox_protection_rule import MailboxProtectionRule
    from .mailbox_protection_unit import MailboxProtectionUnit
    from .protection_policy_base import ProtectionPolicyBase

from .protection_policy_base import ProtectionPolicyBase

@dataclass
class ExchangeProtectionPolicy(ProtectionPolicyBase):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.exchangeProtectionPolicy"
    # The rules associated with the Exchange protection policy.
    mailbox_inclusion_rules: Optional[List[MailboxProtectionRule]] = None
    # The protection units (mailboxes) that are  protected under the Exchange protection policy.
    mailbox_protection_units: Optional[List[MailboxProtectionUnit]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ExchangeProtectionPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ExchangeProtectionPolicy
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ExchangeProtectionPolicy()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .mailbox_protection_rule import MailboxProtectionRule
        from .mailbox_protection_unit import MailboxProtectionUnit
        from .protection_policy_base import ProtectionPolicyBase

        from .mailbox_protection_rule import MailboxProtectionRule
        from .mailbox_protection_unit import MailboxProtectionUnit
        from .protection_policy_base import ProtectionPolicyBase

        fields: Dict[str, Callable[[Any], None]] = {
            "mailboxInclusionRules": lambda n : setattr(self, 'mailbox_inclusion_rules', n.get_collection_of_object_values(MailboxProtectionRule)),
            "mailboxProtectionUnits": lambda n : setattr(self, 'mailbox_protection_units', n.get_collection_of_object_values(MailboxProtectionUnit)),
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
        writer.write_collection_of_object_values("mailboxInclusionRules", self.mailbox_inclusion_rules)
        writer.write_collection_of_object_values("mailboxProtectionUnits", self.mailbox_protection_units)
    

