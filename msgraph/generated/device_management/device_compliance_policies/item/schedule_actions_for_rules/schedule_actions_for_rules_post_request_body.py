from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models import device_compliance_scheduled_action_for_rule

class ScheduleActionsForRulesPostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new scheduleActionsForRulesPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The deviceComplianceScheduledActionForRules property
        self._device_compliance_scheduled_action_for_rules: Optional[List[device_compliance_scheduled_action_for_rule.DeviceComplianceScheduledActionForRule]] = None
    
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ScheduleActionsForRulesPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ScheduleActionsForRulesPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ScheduleActionsForRulesPostRequestBody()
    
    @property
    def device_compliance_scheduled_action_for_rules(self,) -> Optional[List[device_compliance_scheduled_action_for_rule.DeviceComplianceScheduledActionForRule]]:
        """
        Gets the deviceComplianceScheduledActionForRules property value. The deviceComplianceScheduledActionForRules property
        Returns: Optional[List[device_compliance_scheduled_action_for_rule.DeviceComplianceScheduledActionForRule]]
        """
        return self._device_compliance_scheduled_action_for_rules
    
    @device_compliance_scheduled_action_for_rules.setter
    def device_compliance_scheduled_action_for_rules(self,value: Optional[List[device_compliance_scheduled_action_for_rule.DeviceComplianceScheduledActionForRule]] = None) -> None:
        """
        Sets the deviceComplianceScheduledActionForRules property value. The deviceComplianceScheduledActionForRules property
        Args:
            value: Value to set for the device_compliance_scheduled_action_for_rules property.
        """
        self._device_compliance_scheduled_action_for_rules = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .....models import device_compliance_scheduled_action_for_rule

        fields: Dict[str, Callable[[Any], None]] = {
            "deviceComplianceScheduledActionForRules": lambda n : setattr(self, 'device_compliance_scheduled_action_for_rules', n.get_collection_of_object_values(device_compliance_scheduled_action_for_rule.DeviceComplianceScheduledActionForRule)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_object_values("deviceComplianceScheduledActionForRules", self.device_compliance_scheduled_action_for_rules)
        writer.write_additional_data_value(self.additional_data)
    

