from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import conditional_access_policy_detail, entity, template_scenarios

from . import entity

@dataclass
class ConditionalAccessTemplate(entity.Entity):
    # The user-friendly name of the template.
    description: Optional[str] = None
    # The details property
    details: Optional[conditional_access_policy_detail.ConditionalAccessPolicyDetail] = None
    # The user-friendly name of the template.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The scenarios property
    scenarios: Optional[template_scenarios.TemplateScenarios] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ConditionalAccessTemplate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ConditionalAccessTemplate
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ConditionalAccessTemplate()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import conditional_access_policy_detail, entity, template_scenarios

        from . import conditional_access_policy_detail, entity, template_scenarios

        fields: Dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "details": lambda n : setattr(self, 'details', n.get_object_value(conditional_access_policy_detail.ConditionalAccessPolicyDetail)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "scenarios": lambda n : setattr(self, 'scenarios', n.get_enum_value(template_scenarios.TemplateScenarios)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("description", self.description)
        writer.write_object_value("details", self.details)
        writer.write_str_value("name", self.name)
        writer.write_enum_value("scenarios", self.scenarios)
    

