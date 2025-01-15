from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authentication_context_class_reference import AuthenticationContextClassReference
    from .authentication_strength_root import AuthenticationStrengthRoot
    from .conditional_access_policy import ConditionalAccessPolicy
    from .conditional_access_template import ConditionalAccessTemplate
    from .entity import Entity
    from .named_location import NamedLocation

from .entity import Entity

@dataclass
class ConditionalAccessRoot(Entity, Parsable):
    # Read-only. Nullable. Returns a collection of the specified authentication context class references.
    authentication_context_class_references: Optional[list[AuthenticationContextClassReference]] = None
    # The authenticationStrength property
    authentication_strength: Optional[AuthenticationStrengthRoot] = None
    # Read-only. Nullable. Returns a collection of the specified named locations.
    named_locations: Optional[list[NamedLocation]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Read-only. Nullable. Returns a collection of the specified Conditional Access (CA) policies.
    policies: Optional[list[ConditionalAccessPolicy]] = None
    # Read-only. Nullable. Returns a collection of the specified Conditional Access templates.
    templates: Optional[list[ConditionalAccessTemplate]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ConditionalAccessRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ConditionalAccessRoot
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ConditionalAccessRoot()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .authentication_context_class_reference import AuthenticationContextClassReference
        from .authentication_strength_root import AuthenticationStrengthRoot
        from .conditional_access_policy import ConditionalAccessPolicy
        from .conditional_access_template import ConditionalAccessTemplate
        from .entity import Entity
        from .named_location import NamedLocation

        from .authentication_context_class_reference import AuthenticationContextClassReference
        from .authentication_strength_root import AuthenticationStrengthRoot
        from .conditional_access_policy import ConditionalAccessPolicy
        from .conditional_access_template import ConditionalAccessTemplate
        from .entity import Entity
        from .named_location import NamedLocation

        fields: dict[str, Callable[[Any], None]] = {
            "authenticationContextClassReferences": lambda n : setattr(self, 'authentication_context_class_references', n.get_collection_of_object_values(AuthenticationContextClassReference)),
            "authenticationStrength": lambda n : setattr(self, 'authentication_strength', n.get_object_value(AuthenticationStrengthRoot)),
            "namedLocations": lambda n : setattr(self, 'named_locations', n.get_collection_of_object_values(NamedLocation)),
            "policies": lambda n : setattr(self, 'policies', n.get_collection_of_object_values(ConditionalAccessPolicy)),
            "templates": lambda n : setattr(self, 'templates', n.get_collection_of_object_values(ConditionalAccessTemplate)),
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
        writer.write_collection_of_object_values("authenticationContextClassReferences", self.authentication_context_class_references)
        writer.write_object_value("authenticationStrength", self.authentication_strength)
        writer.write_collection_of_object_values("namedLocations", self.named_locations)
        writer.write_collection_of_object_values("policies", self.policies)
        writer.write_collection_of_object_values("templates", self.templates)
    

