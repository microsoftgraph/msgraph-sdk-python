from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import authentication_context_class_reference, authentication_strength_root, conditional_access_policy, conditional_access_template, entity, named_location

from . import entity

class ConditionalAccessRoot(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new ConditionalAccessRoot and sets the default values.
        """
        super().__init__()
        # Read-only. Nullable. Returns a collection of the specified authentication context class references.
        self._authentication_context_class_references: Optional[List[authentication_context_class_reference.AuthenticationContextClassReference]] = None
        # The authenticationStrength property
        self._authentication_strength: Optional[authentication_strength_root.AuthenticationStrengthRoot] = None
        # Read-only. Nullable. Returns a collection of the specified named locations.
        self._named_locations: Optional[List[named_location.NamedLocation]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Read-only. Nullable. Returns a collection of the specified Conditional Access (CA) policies.
        self._policies: Optional[List[conditional_access_policy.ConditionalAccessPolicy]] = None
        # Read-only. Nullable. Returns a collection of the specified Conditional Access templates.
        self._templates: Optional[List[conditional_access_template.ConditionalAccessTemplate]] = None
    
    @property
    def authentication_context_class_references(self,) -> Optional[List[authentication_context_class_reference.AuthenticationContextClassReference]]:
        """
        Gets the authenticationContextClassReferences property value. Read-only. Nullable. Returns a collection of the specified authentication context class references.
        Returns: Optional[List[authentication_context_class_reference.AuthenticationContextClassReference]]
        """
        return self._authentication_context_class_references
    
    @authentication_context_class_references.setter
    def authentication_context_class_references(self,value: Optional[List[authentication_context_class_reference.AuthenticationContextClassReference]] = None) -> None:
        """
        Sets the authenticationContextClassReferences property value. Read-only. Nullable. Returns a collection of the specified authentication context class references.
        Args:
            value: Value to set for the authentication_context_class_references property.
        """
        self._authentication_context_class_references = value
    
    @property
    def authentication_strength(self,) -> Optional[authentication_strength_root.AuthenticationStrengthRoot]:
        """
        Gets the authenticationStrength property value. The authenticationStrength property
        Returns: Optional[authentication_strength_root.AuthenticationStrengthRoot]
        """
        return self._authentication_strength
    
    @authentication_strength.setter
    def authentication_strength(self,value: Optional[authentication_strength_root.AuthenticationStrengthRoot] = None) -> None:
        """
        Sets the authenticationStrength property value. The authenticationStrength property
        Args:
            value: Value to set for the authentication_strength property.
        """
        self._authentication_strength = value
    
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
    
    @property
    def named_locations(self,) -> Optional[List[named_location.NamedLocation]]:
        """
        Gets the namedLocations property value. Read-only. Nullable. Returns a collection of the specified named locations.
        Returns: Optional[List[named_location.NamedLocation]]
        """
        return self._named_locations
    
    @named_locations.setter
    def named_locations(self,value: Optional[List[named_location.NamedLocation]] = None) -> None:
        """
        Sets the namedLocations property value. Read-only. Nullable. Returns a collection of the specified named locations.
        Args:
            value: Value to set for the named_locations property.
        """
        self._named_locations = value
    
    @property
    def policies(self,) -> Optional[List[conditional_access_policy.ConditionalAccessPolicy]]:
        """
        Gets the policies property value. Read-only. Nullable. Returns a collection of the specified Conditional Access (CA) policies.
        Returns: Optional[List[conditional_access_policy.ConditionalAccessPolicy]]
        """
        return self._policies
    
    @policies.setter
    def policies(self,value: Optional[List[conditional_access_policy.ConditionalAccessPolicy]] = None) -> None:
        """
        Sets the policies property value. Read-only. Nullable. Returns a collection of the specified Conditional Access (CA) policies.
        Args:
            value: Value to set for the policies property.
        """
        self._policies = value
    
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
    
    @property
    def templates(self,) -> Optional[List[conditional_access_template.ConditionalAccessTemplate]]:
        """
        Gets the templates property value. Read-only. Nullable. Returns a collection of the specified Conditional Access templates.
        Returns: Optional[List[conditional_access_template.ConditionalAccessTemplate]]
        """
        return self._templates
    
    @templates.setter
    def templates(self,value: Optional[List[conditional_access_template.ConditionalAccessTemplate]] = None) -> None:
        """
        Sets the templates property value. Read-only. Nullable. Returns a collection of the specified Conditional Access templates.
        Args:
            value: Value to set for the templates property.
        """
        self._templates = value
    

