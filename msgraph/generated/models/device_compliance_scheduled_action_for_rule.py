from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_compliance_action_item import DeviceComplianceActionItem
    from .entity import Entity

from .entity import Entity

@dataclass
class DeviceComplianceScheduledActionForRule(Entity, Parsable):
    """
    Scheduled Action for Rule
    """
    # The OdataType property
    odata_type: Optional[str] = None
    # Name of the rule which this scheduled action applies to. Currently scheduled actions are created per policy instead of per rule, thus RuleName is always set to default value PasswordRequired.
    rule_name: Optional[str] = None
    # The list of scheduled action configurations for this compliance policy. Compliance policy must have one and only one block scheduled action.
    scheduled_action_configurations: Optional[list[DeviceComplianceActionItem]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceComplianceScheduledActionForRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceComplianceScheduledActionForRule
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceComplianceScheduledActionForRule()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_compliance_action_item import DeviceComplianceActionItem
        from .entity import Entity

        from .device_compliance_action_item import DeviceComplianceActionItem
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "ruleName": lambda n : setattr(self, 'rule_name', n.get_str_value()),
            "scheduledActionConfigurations": lambda n : setattr(self, 'scheduled_action_configurations', n.get_collection_of_object_values(DeviceComplianceActionItem)),
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
        writer.write_str_value("ruleName", self.rule_name)
        writer.write_collection_of_object_values("scheduledActionConfigurations", self.scheduled_action_configurations)
    

