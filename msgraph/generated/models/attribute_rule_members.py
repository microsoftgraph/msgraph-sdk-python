from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

subject_set = lazy_import('msgraph.generated.models.subject_set')

class AttributeRuleMembers(subject_set.SubjectSet):
    def __init__(self,) -> None:
        """
        Instantiates a new AttributeRuleMembers and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.attributeRuleMembers"
        # A description of the membership rule.
        self._description: Optional[str] = None
        # Determines the allowed target users for this policy. For more information about the syntax of the membership rule, see Membership Rules syntax.
        self._membership_rule: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AttributeRuleMembers:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AttributeRuleMembers
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AttributeRuleMembers()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. A description of the membership rule.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. A description of the membership rule.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "membership_rule": lambda n : setattr(self, 'membership_rule', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def membership_rule(self,) -> Optional[str]:
        """
        Gets the membershipRule property value. Determines the allowed target users for this policy. For more information about the syntax of the membership rule, see Membership Rules syntax.
        Returns: Optional[str]
        """
        return self._membership_rule
    
    @membership_rule.setter
    def membership_rule(self,value: Optional[str] = None) -> None:
        """
        Sets the membershipRule property value. Determines the allowed target users for this policy. For more information about the syntax of the membership rule, see Membership Rules syntax.
        Args:
            value: Value to set for the membershipRule property.
        """
        self._membership_rule = value
    
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
        writer.write_str_value("membershipRule", self.membership_rule)
    

