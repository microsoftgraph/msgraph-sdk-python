from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .message_rule_actions import MessageRuleActions
    from .message_rule_predicates import MessageRulePredicates

from .entity import Entity

@dataclass
class MessageRule(Entity, Parsable):
    # Actions to be taken on a message when the corresponding conditions are fulfilled.
    actions: Optional[MessageRuleActions] = None
    # Conditions that when fulfilled trigger the corresponding actions for that rule.
    conditions: Optional[MessageRulePredicates] = None
    # The display name of the rule.
    display_name: Optional[str] = None
    # Exception conditions for the rule.
    exceptions: Optional[MessageRulePredicates] = None
    # Indicates whether the rule is in an error condition. Read-only.
    has_error: Optional[bool] = None
    # Indicates whether the rule is enabled to be applied to messages.
    is_enabled: Optional[bool] = None
    # Indicates if the rule is read-only and cannot be modified or deleted by the rules REST API.
    is_read_only: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates the order in which the rule is executed, among other rules.
    sequence: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MessageRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MessageRule
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MessageRule()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .message_rule_actions import MessageRuleActions
        from .message_rule_predicates import MessageRulePredicates

        from .entity import Entity
        from .message_rule_actions import MessageRuleActions
        from .message_rule_predicates import MessageRulePredicates

        fields: dict[str, Callable[[Any], None]] = {
            "actions": lambda n : setattr(self, 'actions', n.get_object_value(MessageRuleActions)),
            "conditions": lambda n : setattr(self, 'conditions', n.get_object_value(MessageRulePredicates)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "exceptions": lambda n : setattr(self, 'exceptions', n.get_object_value(MessageRulePredicates)),
            "hasError": lambda n : setattr(self, 'has_error', n.get_bool_value()),
            "isEnabled": lambda n : setattr(self, 'is_enabled', n.get_bool_value()),
            "isReadOnly": lambda n : setattr(self, 'is_read_only', n.get_bool_value()),
            "sequence": lambda n : setattr(self, 'sequence', n.get_int_value()),
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
        writer.write_object_value("actions", self.actions)
        writer.write_object_value("conditions", self.conditions)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("exceptions", self.exceptions)
        writer.write_bool_value("hasError", self.has_error)
        writer.write_bool_value("isEnabled", self.is_enabled)
        writer.write_bool_value("isReadOnly", self.is_read_only)
        writer.write_int_value("sequence", self.sequence)
    

