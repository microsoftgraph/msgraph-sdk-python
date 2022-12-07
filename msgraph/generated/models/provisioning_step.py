from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

details_info = lazy_import('msgraph.generated.models.details_info')
provisioning_result = lazy_import('msgraph.generated.models.provisioning_result')
provisioning_step_type = lazy_import('msgraph.generated.models.provisioning_step_type')

class ProvisioningStep(AdditionalDataHolder, Parsable):
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
        Instantiates a new provisioningStep and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Summary of what occurred during the step.
        self._description: Optional[str] = None
        # Details of what occurred during the step.
        self._details: Optional[details_info.DetailsInfo] = None
        # Name of the step.
        self._name: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Type of step. Possible values are: import, scoping, matching, processing, referenceResolution, export, unknownFutureValue.
        self._provisioning_step_type: Optional[provisioning_step_type.ProvisioningStepType] = None
        # Status of the step. Possible values are: success, warning,  failure, skipped, unknownFutureValue.
        self._status: Optional[provisioning_result.ProvisioningResult] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ProvisioningStep:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ProvisioningStep
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ProvisioningStep()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Summary of what occurred during the step.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Summary of what occurred during the step.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def details(self,) -> Optional[details_info.DetailsInfo]:
        """
        Gets the details property value. Details of what occurred during the step.
        Returns: Optional[details_info.DetailsInfo]
        """
        return self._details
    
    @details.setter
    def details(self,value: Optional[details_info.DetailsInfo] = None) -> None:
        """
        Sets the details property value. Details of what occurred during the step.
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
            "details": lambda n : setattr(self, 'details', n.get_object_value(details_info.DetailsInfo)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "provisioning_step_type": lambda n : setattr(self, 'provisioning_step_type', n.get_enum_value(provisioning_step_type.ProvisioningStepType)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(provisioning_result.ProvisioningResult)),
        }
        return fields
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. Name of the step.
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. Name of the step.
        Args:
            value: Value to set for the name property.
        """
        self._name = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def provisioning_step_type(self,) -> Optional[provisioning_step_type.ProvisioningStepType]:
        """
        Gets the provisioningStepType property value. Type of step. Possible values are: import, scoping, matching, processing, referenceResolution, export, unknownFutureValue.
        Returns: Optional[provisioning_step_type.ProvisioningStepType]
        """
        return self._provisioning_step_type
    
    @provisioning_step_type.setter
    def provisioning_step_type(self,value: Optional[provisioning_step_type.ProvisioningStepType] = None) -> None:
        """
        Sets the provisioningStepType property value. Type of step. Possible values are: import, scoping, matching, processing, referenceResolution, export, unknownFutureValue.
        Args:
            value: Value to set for the provisioningStepType property.
        """
        self._provisioning_step_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("description", self.description)
        writer.write_object_value("details", self.details)
        writer.write_str_value("name", self.name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("provisioningStepType", self.provisioning_step_type)
        writer.write_enum_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def status(self,) -> Optional[provisioning_result.ProvisioningResult]:
        """
        Gets the status property value. Status of the step. Possible values are: success, warning,  failure, skipped, unknownFutureValue.
        Returns: Optional[provisioning_result.ProvisioningResult]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[provisioning_result.ProvisioningResult] = None) -> None:
        """
        Sets the status property value. Status of the step. Possible values are: success, warning,  failure, skipped, unknownFutureValue.
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    

