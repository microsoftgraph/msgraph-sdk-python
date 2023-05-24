from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .......models import synchronization_job_application_parameters

class ProvisionOnDemandPostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new provisionOnDemandPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The parameters property
        self._parameters: Optional[List[synchronization_job_application_parameters.SynchronizationJobApplicationParameters]] = None
    
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
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ProvisionOnDemandPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ProvisionOnDemandPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ProvisionOnDemandPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .......models import synchronization_job_application_parameters

        fields: Dict[str, Callable[[Any], None]] = {
            "parameters": lambda n : setattr(self, 'parameters', n.get_collection_of_object_values(synchronization_job_application_parameters.SynchronizationJobApplicationParameters)),
        }
        return fields
    
    @property
    def parameters(self,) -> Optional[List[synchronization_job_application_parameters.SynchronizationJobApplicationParameters]]:
        """
        Gets the parameters property value. The parameters property
        Returns: Optional[List[synchronization_job_application_parameters.SynchronizationJobApplicationParameters]]
        """
        return self._parameters
    
    @parameters.setter
    def parameters(self,value: Optional[List[synchronization_job_application_parameters.SynchronizationJobApplicationParameters]] = None) -> None:
        """
        Sets the parameters property value. The parameters property
        Args:
            value: Value to set for the parameters property.
        """
        self._parameters = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_object_values("parameters", self.parameters)
        writer.write_additional_data_value(self.additional_data)
    

