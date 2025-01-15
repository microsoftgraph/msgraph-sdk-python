from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .protection_rule_base import ProtectionRuleBase

from .protection_rule_base import ProtectionRuleBase

@dataclass
class MailboxProtectionRule(ProtectionRuleBase, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.mailboxProtectionRule"
    # Contains a mailbox expression. For examples, see mailboxExpression examples.
    mailbox_expression: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MailboxProtectionRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MailboxProtectionRule
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MailboxProtectionRule()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .protection_rule_base import ProtectionRuleBase

        from .protection_rule_base import ProtectionRuleBase

        fields: dict[str, Callable[[Any], None]] = {
            "mailboxExpression": lambda n : setattr(self, 'mailbox_expression', n.get_str_value()),
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
        writer.write_str_value("mailboxExpression", self.mailbox_expression)
    

