from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import education_resource, entity

from . import entity

class EducationSubmissionResource(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new educationSubmissionResource and sets the default values.
        """
        super().__init__()
        # Pointer to the assignment from which this resource was copied. If this is null, the student uploaded the resource.
        self._assignment_resource_url: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Resource object.
        self._resource: Optional[education_resource.EducationResource] = None
    
    @property
    def assignment_resource_url(self,) -> Optional[str]:
        """
        Gets the assignmentResourceUrl property value. Pointer to the assignment from which this resource was copied. If this is null, the student uploaded the resource.
        Returns: Optional[str]
        """
        return self._assignment_resource_url
    
    @assignment_resource_url.setter
    def assignment_resource_url(self,value: Optional[str] = None) -> None:
        """
        Sets the assignmentResourceUrl property value. Pointer to the assignment from which this resource was copied. If this is null, the student uploaded the resource.
        Args:
            value: Value to set for the assignment_resource_url property.
        """
        self._assignment_resource_url = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EducationSubmissionResource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EducationSubmissionResource
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EducationSubmissionResource()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import education_resource, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "assignmentResourceUrl": lambda n : setattr(self, 'assignment_resource_url', n.get_str_value()),
            "resource": lambda n : setattr(self, 'resource', n.get_object_value(education_resource.EducationResource)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def resource(self,) -> Optional[education_resource.EducationResource]:
        """
        Gets the resource property value. Resource object.
        Returns: Optional[education_resource.EducationResource]
        """
        return self._resource
    
    @resource.setter
    def resource(self,value: Optional[education_resource.EducationResource] = None) -> None:
        """
        Sets the resource property value. Resource object.
        Args:
            value: Value to set for the resource property.
        """
        self._resource = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("assignmentResourceUrl", self.assignment_resource_url)
        writer.write_object_value("resource", self.resource)
    

