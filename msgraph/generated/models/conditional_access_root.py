from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import authentication_context_class_reference, authentication_strength_root, conditional_access_policy, conditional_access_template, entity, named_location

from . import entity

@dataclass
class ConditionalAccessRoot(entity.Entity):
    # Read-only. Nullable. Returns a collection of the specified authentication context class references.
    authentication_context_class_references: Optional[List[authentication_context_class_reference.AuthenticationContextClassReference]] = None
    # The authenticationStrength property
    authentication_strength: Optional[authentication_strength_root.AuthenticationStrengthRoot] = None
    # Read-only. Nullable. Returns a collection of the specified named locations.
    named_locations: Optional[List[named_location.NamedLocation]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Read-only. Nullable. Returns a collection of the specified Conditional Access (CA) policies.
    policies: Optional[List[conditional_access_policy.ConditionalAccessPolicy]] = None
    # Read-only. Nullable. Returns a collection of the specified Conditional Access templates.
    templates: Optional[List[conditional_access_template.ConditionalAccessTemplate]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ConditionalAccessRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ConditionalAccessRoot
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ConditionalAccessRoot()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import authentication_context_class_reference, authentication_strength_root, conditional_access_policy, conditional_access_template, entity, named_location

        fields: Dict[str, Callable[[Any], None]] = {
            "authenticationContextClassReferences": lambda n : setattr(self, 'authentication_context_class_references', n.get_collection_of_object_values(authentication_context_class_reference.AuthenticationContextClassReference)),
            "authenticationStrength": lambda n : setattr(self, 'authentication_strength', n.get_object_value(authentication_strength_root.AuthenticationStrengthRoot)),
            "namedLocations": lambda n : setattr(self, 'named_locations', n.get_collection_of_object_values(named_location.NamedLocation)),
            "policies": lambda n : setattr(self, 'policies', n.get_collection_of_object_values(conditional_access_policy.ConditionalAccessPolicy)),
            "templates": lambda n : setattr(self, 'templates', n.get_collection_of_object_values(conditional_access_template.ConditionalAccessTemplate)),
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
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("authenticationContextClassReferences", self.authentication_context_class_references)
        writer.write_object_value("authenticationStrength", self.authentication_strength)
        writer.write_collection_of_object_values("namedLocations", self.named_locations)
        writer.write_collection_of_object_values("policies", self.policies)
        writer.write_collection_of_object_values("templates", self.templates)
    

