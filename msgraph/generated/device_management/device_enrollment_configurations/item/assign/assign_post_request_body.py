from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

enrollment_configuration_assignment = lazy_import('msgraph.generated.models.enrollment_configuration_assignment')

class AssignPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the assign method.
    """
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new assignPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The enrollmentConfigurationAssignments property
        self._enrollment_configuration_assignments: Optional[List[enrollment_configuration_assignment.EnrollmentConfigurationAssignment]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AssignPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AssignPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AssignPostRequestBody()
    
    @property
    def enrollment_configuration_assignments(self,) -> Optional[List[enrollment_configuration_assignment.EnrollmentConfigurationAssignment]]:
        """
        Gets the enrollmentConfigurationAssignments property value. The enrollmentConfigurationAssignments property
        Returns: Optional[List[enrollment_configuration_assignment.EnrollmentConfigurationAssignment]]
        """
        return self._enrollment_configuration_assignments
    
    @enrollment_configuration_assignments.setter
    def enrollment_configuration_assignments(self,value: Optional[List[enrollment_configuration_assignment.EnrollmentConfigurationAssignment]] = None) -> None:
        """
        Sets the enrollmentConfigurationAssignments property value. The enrollmentConfigurationAssignments property
        Args:
            value: Value to set for the enrollmentConfigurationAssignments property.
        """
        self._enrollment_configuration_assignments = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "enrollment_configuration_assignments": lambda n : setattr(self, 'enrollment_configuration_assignments', n.get_collection_of_object_values(enrollment_configuration_assignment.EnrollmentConfigurationAssignment)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_object_values("enrollmentConfigurationAssignments", self.enrollment_configuration_assignments)
        writer.write_additional_data_value(self.additional_data)
    

