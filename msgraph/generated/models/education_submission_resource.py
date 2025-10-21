from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .education_resource import EducationResource
    from .entity import Entity

from .entity import Entity

@dataclass
class EducationSubmissionResource(Entity, Parsable):
    # Pointer to the assignment from which the resource was copied. If the value is null, the student uploaded the resource.
    assignment_resource_url: Optional[str] = None
    # A collection of submission resources that depend on the parent educationSubmissionResource.
    dependent_resources: Optional[list[EducationSubmissionResource]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Resource object.
    resource: Optional[EducationResource] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EducationSubmissionResource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EducationSubmissionResource
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EducationSubmissionResource()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .education_resource import EducationResource
        from .entity import Entity

        from .education_resource import EducationResource
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "assignmentResourceUrl": lambda n : setattr(self, 'assignment_resource_url', n.get_str_value()),
            "dependentResources": lambda n : setattr(self, 'dependent_resources', n.get_collection_of_object_values(EducationSubmissionResource)),
            "resource": lambda n : setattr(self, 'resource', n.get_object_value(EducationResource)),
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
        writer.write_str_value("assignmentResourceUrl", self.assignment_resource_url)
        writer.write_collection_of_object_values("dependentResources", self.dependent_resources)
        writer.write_object_value("resource", self.resource)
    

