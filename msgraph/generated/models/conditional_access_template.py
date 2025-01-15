from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .conditional_access_policy_detail import ConditionalAccessPolicyDetail
    from .entity import Entity
    from .template_scenarios import TemplateScenarios

from .entity import Entity

@dataclass
class ConditionalAccessTemplate(Entity, Parsable):
    # The user-friendly name of the template.
    description: Optional[str] = None
    # The details property
    details: Optional[ConditionalAccessPolicyDetail] = None
    # The user-friendly name of the template.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The scenarios property
    scenarios: Optional[TemplateScenarios] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ConditionalAccessTemplate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ConditionalAccessTemplate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ConditionalAccessTemplate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .conditional_access_policy_detail import ConditionalAccessPolicyDetail
        from .entity import Entity
        from .template_scenarios import TemplateScenarios

        from .conditional_access_policy_detail import ConditionalAccessPolicyDetail
        from .entity import Entity
        from .template_scenarios import TemplateScenarios

        fields: dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "details": lambda n : setattr(self, 'details', n.get_object_value(ConditionalAccessPolicyDetail)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "scenarios": lambda n : setattr(self, 'scenarios', n.get_collection_of_enum_values(TemplateScenarios)),
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
        writer.write_str_value("description", self.description)
        writer.write_object_value("details", self.details)
        writer.write_str_value("name", self.name)
        writer.write_enum_value("scenarios", self.scenarios)
    

