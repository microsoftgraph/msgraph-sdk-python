from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

conditional_access_policy_detail = lazy_import('msgraph.generated.models.conditional_access_policy_detail')
entity = lazy_import('msgraph.generated.models.entity')
template_scenarios = lazy_import('msgraph.generated.models.template_scenarios')

class ConditionalAccessTemplate(entity.Entity):
    """
    Provides operations to manage the admin singleton.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new conditionalAccessTemplate and sets the default values.
        """
        super().__init__()
        # The user-friendly name of the template.
        self._description: Optional[str] = None
        # The details property
        self._details: Optional[conditional_access_policy_detail.ConditionalAccessPolicyDetail] = None
        # The user-friendly name of the template.
        self._name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The scenarios property
        self._scenarios: Optional[template_scenarios.TemplateScenarios] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ConditionalAccessTemplate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ConditionalAccessTemplate
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ConditionalAccessTemplate()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The user-friendly name of the template.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The user-friendly name of the template.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def details(self,) -> Optional[conditional_access_policy_detail.ConditionalAccessPolicyDetail]:
        """
        Gets the details property value. The details property
        Returns: Optional[conditional_access_policy_detail.ConditionalAccessPolicyDetail]
        """
        return self._details
    
    @details.setter
    def details(self,value: Optional[conditional_access_policy_detail.ConditionalAccessPolicyDetail] = None) -> None:
        """
        Sets the details property value. The details property
        Args:
            value: Value to set for the details property.
        """
        self._details = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "details": lambda n : setattr(self, 'details', n.get_object_value(conditional_access_policy_detail.ConditionalAccessPolicyDetail)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "scenarios": lambda n : setattr(self, 'scenarios', n.get_enum_value(template_scenarios.TemplateScenarios)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. The user-friendly name of the template.
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. The user-friendly name of the template.
        Args:
            value: Value to set for the name property.
        """
        self._name = value
    
    @property
    def scenarios(self,) -> Optional[template_scenarios.TemplateScenarios]:
        """
        Gets the scenarios property value. The scenarios property
        Returns: Optional[template_scenarios.TemplateScenarios]
        """
        return self._scenarios
    
    @scenarios.setter
    def scenarios(self,value: Optional[template_scenarios.TemplateScenarios] = None) -> None:
        """
        Sets the scenarios property value. The scenarios property
        Args:
            value: Value to set for the scenarios property.
        """
        self._scenarios = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("description", self.description)
        writer.write_object_value("details", self.details)
        writer.write_str_value("name", self.name)
        writer.write_enum_value("scenarios", self.scenarios)
    

