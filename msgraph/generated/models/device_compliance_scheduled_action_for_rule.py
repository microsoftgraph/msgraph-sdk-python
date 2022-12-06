from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_compliance_action_item = lazy_import('msgraph.generated.models.device_compliance_action_item')
entity = lazy_import('msgraph.generated.models.entity')

class DeviceComplianceScheduledActionForRule(entity.Entity):
    """
    Scheduled Action for Rule
    """
    def __init__(self,) -> None:
        """
        Instantiates a new deviceComplianceScheduledActionForRule and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Name of the rule which this scheduled action applies to. Currently scheduled actions are created per policy instead of per rule, thus RuleName is always set to default value PasswordRequired.
        self._rule_name: Optional[str] = None
        # The list of scheduled action configurations for this compliance policy. Compliance policy must have one and only one block scheduled action.
        self._scheduled_action_configurations: Optional[List[device_compliance_action_item.DeviceComplianceActionItem]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceComplianceScheduledActionForRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceComplianceScheduledActionForRule
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceComplianceScheduledActionForRule()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "rule_name": lambda n : setattr(self, 'rule_name', n.get_str_value()),
            "scheduled_action_configurations": lambda n : setattr(self, 'scheduled_action_configurations', n.get_collection_of_object_values(device_compliance_action_item.DeviceComplianceActionItem)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def rule_name(self,) -> Optional[str]:
        """
        Gets the ruleName property value. Name of the rule which this scheduled action applies to. Currently scheduled actions are created per policy instead of per rule, thus RuleName is always set to default value PasswordRequired.
        Returns: Optional[str]
        """
        return self._rule_name
    
    @rule_name.setter
    def rule_name(self,value: Optional[str] = None) -> None:
        """
        Sets the ruleName property value. Name of the rule which this scheduled action applies to. Currently scheduled actions are created per policy instead of per rule, thus RuleName is always set to default value PasswordRequired.
        Args:
            value: Value to set for the ruleName property.
        """
        self._rule_name = value
    
    @property
    def scheduled_action_configurations(self,) -> Optional[List[device_compliance_action_item.DeviceComplianceActionItem]]:
        """
        Gets the scheduledActionConfigurations property value. The list of scheduled action configurations for this compliance policy. Compliance policy must have one and only one block scheduled action.
        Returns: Optional[List[device_compliance_action_item.DeviceComplianceActionItem]]
        """
        return self._scheduled_action_configurations
    
    @scheduled_action_configurations.setter
    def scheduled_action_configurations(self,value: Optional[List[device_compliance_action_item.DeviceComplianceActionItem]] = None) -> None:
        """
        Sets the scheduledActionConfigurations property value. The list of scheduled action configurations for this compliance policy. Compliance policy must have one and only one block scheduled action.
        Args:
            value: Value to set for the scheduledActionConfigurations property.
        """
        self._scheduled_action_configurations = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("ruleName", self.rule_name)
        writer.write_collection_of_object_values("scheduledActionConfigurations", self.scheduled_action_configurations)
    

