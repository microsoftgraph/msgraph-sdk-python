from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
message_rule_actions = lazy_import('msgraph.generated.models.message_rule_actions')
message_rule_predicates = lazy_import('msgraph.generated.models.message_rule_predicates')

class MessageRule(entity.Entity):
    """
    Provides operations to manage the admin singleton.
    """
    @property
    def actions(self,) -> Optional[message_rule_actions.MessageRuleActions]:
        """
        Gets the actions property value. Actions to be taken on a message when the corresponding conditions are fulfilled.
        Returns: Optional[message_rule_actions.MessageRuleActions]
        """
        return self._actions
    
    @actions.setter
    def actions(self,value: Optional[message_rule_actions.MessageRuleActions] = None) -> None:
        """
        Sets the actions property value. Actions to be taken on a message when the corresponding conditions are fulfilled.
        Args:
            value: Value to set for the actions property.
        """
        self._actions = value
    
    @property
    def conditions(self,) -> Optional[message_rule_predicates.MessageRulePredicates]:
        """
        Gets the conditions property value. Conditions that when fulfilled, will trigger the corresponding actions for that rule.
        Returns: Optional[message_rule_predicates.MessageRulePredicates]
        """
        return self._conditions
    
    @conditions.setter
    def conditions(self,value: Optional[message_rule_predicates.MessageRulePredicates] = None) -> None:
        """
        Sets the conditions property value. Conditions that when fulfilled, will trigger the corresponding actions for that rule.
        Args:
            value: Value to set for the conditions property.
        """
        self._conditions = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new messageRule and sets the default values.
        """
        super().__init__()
        # Actions to be taken on a message when the corresponding conditions are fulfilled.
        self._actions: Optional[message_rule_actions.MessageRuleActions] = None
        # Conditions that when fulfilled, will trigger the corresponding actions for that rule.
        self._conditions: Optional[message_rule_predicates.MessageRulePredicates] = None
        # The display name of the rule.
        self._display_name: Optional[str] = None
        # Exception conditions for the rule.
        self._exceptions: Optional[message_rule_predicates.MessageRulePredicates] = None
        # Indicates whether the rule is in an error condition. Read-only.
        self._has_error: Optional[bool] = None
        # Indicates whether the rule is enabled to be applied to messages.
        self._is_enabled: Optional[bool] = None
        # Indicates if the rule is read-only and cannot be modified or deleted by the rules REST API.
        self._is_read_only: Optional[bool] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Indicates the order in which the rule is executed, among other rules.
        self._sequence: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MessageRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MessageRule
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MessageRule()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name of the rule.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name of the rule.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def exceptions(self,) -> Optional[message_rule_predicates.MessageRulePredicates]:
        """
        Gets the exceptions property value. Exception conditions for the rule.
        Returns: Optional[message_rule_predicates.MessageRulePredicates]
        """
        return self._exceptions
    
    @exceptions.setter
    def exceptions(self,value: Optional[message_rule_predicates.MessageRulePredicates] = None) -> None:
        """
        Sets the exceptions property value. Exception conditions for the rule.
        Args:
            value: Value to set for the exceptions property.
        """
        self._exceptions = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "actions": lambda n : setattr(self, 'actions', n.get_object_value(message_rule_actions.MessageRuleActions)),
            "conditions": lambda n : setattr(self, 'conditions', n.get_object_value(message_rule_predicates.MessageRulePredicates)),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "exceptions": lambda n : setattr(self, 'exceptions', n.get_object_value(message_rule_predicates.MessageRulePredicates)),
            "has_error": lambda n : setattr(self, 'has_error', n.get_bool_value()),
            "is_enabled": lambda n : setattr(self, 'is_enabled', n.get_bool_value()),
            "is_read_only": lambda n : setattr(self, 'is_read_only', n.get_bool_value()),
            "sequence": lambda n : setattr(self, 'sequence', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def has_error(self,) -> Optional[bool]:
        """
        Gets the hasError property value. Indicates whether the rule is in an error condition. Read-only.
        Returns: Optional[bool]
        """
        return self._has_error
    
    @has_error.setter
    def has_error(self,value: Optional[bool] = None) -> None:
        """
        Sets the hasError property value. Indicates whether the rule is in an error condition. Read-only.
        Args:
            value: Value to set for the hasError property.
        """
        self._has_error = value
    
    @property
    def is_enabled(self,) -> Optional[bool]:
        """
        Gets the isEnabled property value. Indicates whether the rule is enabled to be applied to messages.
        Returns: Optional[bool]
        """
        return self._is_enabled
    
    @is_enabled.setter
    def is_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isEnabled property value. Indicates whether the rule is enabled to be applied to messages.
        Args:
            value: Value to set for the isEnabled property.
        """
        self._is_enabled = value
    
    @property
    def is_read_only(self,) -> Optional[bool]:
        """
        Gets the isReadOnly property value. Indicates if the rule is read-only and cannot be modified or deleted by the rules REST API.
        Returns: Optional[bool]
        """
        return self._is_read_only
    
    @is_read_only.setter
    def is_read_only(self,value: Optional[bool] = None) -> None:
        """
        Sets the isReadOnly property value. Indicates if the rule is read-only and cannot be modified or deleted by the rules REST API.
        Args:
            value: Value to set for the isReadOnly property.
        """
        self._is_read_only = value
    
    @property
    def sequence(self,) -> Optional[int]:
        """
        Gets the sequence property value. Indicates the order in which the rule is executed, among other rules.
        Returns: Optional[int]
        """
        return self._sequence
    
    @sequence.setter
    def sequence(self,value: Optional[int] = None) -> None:
        """
        Sets the sequence property value. Indicates the order in which the rule is executed, among other rules.
        Args:
            value: Value to set for the sequence property.
        """
        self._sequence = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("actions", self.actions)
        writer.write_object_value("conditions", self.conditions)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("exceptions", self.exceptions)
        writer.write_bool_value("hasError", self.has_error)
        writer.write_bool_value("isEnabled", self.is_enabled)
        writer.write_bool_value("isReadOnly", self.is_read_only)
        writer.write_int_value("sequence", self.sequence)
    

