from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

education_resource = lazy_import('msgraph.generated.models.education_resource')
entity = lazy_import('msgraph.generated.models.entity')

class EducationAssignmentResource(entity.Entity):
    """
    Provides operations to manage the collection of agreement entities.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new educationAssignmentResource and sets the default values.
        """
        super().__init__()
        # Indicates whether this resource should be copied to each student submission for modification and submission. Required
        self._distribute_for_student_work: Optional[bool] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Resource object that has been associated with this assignment.
        self._resource: Optional[education_resource.EducationResource] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EducationAssignmentResource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EducationAssignmentResource
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EducationAssignmentResource()
    
    @property
    def distribute_for_student_work(self,) -> Optional[bool]:
        """
        Gets the distributeForStudentWork property value. Indicates whether this resource should be copied to each student submission for modification and submission. Required
        Returns: Optional[bool]
        """
        return self._distribute_for_student_work
    
    @distribute_for_student_work.setter
    def distribute_for_student_work(self,value: Optional[bool] = None) -> None:
        """
        Sets the distributeForStudentWork property value. Indicates whether this resource should be copied to each student submission for modification and submission. Required
        Args:
            value: Value to set for the distributeForStudentWork property.
        """
        self._distribute_for_student_work = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "distribute_for_student_work": lambda n : setattr(self, 'distribute_for_student_work', n.get_bool_value()),
            "resource": lambda n : setattr(self, 'resource', n.get_object_value(education_resource.EducationResource)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def resource(self,) -> Optional[education_resource.EducationResource]:
        """
        Gets the resource property value. Resource object that has been associated with this assignment.
        Returns: Optional[education_resource.EducationResource]
        """
        return self._resource
    
    @resource.setter
    def resource(self,value: Optional[education_resource.EducationResource] = None) -> None:
        """
        Sets the resource property value. Resource object that has been associated with this assignment.
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
        writer.write_bool_value("distributeForStudentWork", self.distribute_for_student_work)
        writer.write_object_value("resource", self.resource)
    

