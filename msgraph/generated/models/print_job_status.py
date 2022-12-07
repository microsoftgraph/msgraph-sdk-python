from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

print_job_processing_state = lazy_import('msgraph.generated.models.print_job_processing_state')
print_job_state_detail = lazy_import('msgraph.generated.models.print_job_state_detail')

class PrintJobStatus(AdditionalDataHolder, Parsable):
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
        Instantiates a new printJobStatus and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # A human-readable description of the print job's current processing state. Read-only.
        self._description: Optional[str] = None
        # Additional details for print job state. Valid values are described in the following table. Read-only.
        self._details: Optional[List[print_job_state_detail.PrintJobStateDetail]] = None
        # True if the job was acknowledged by a printer; false otherwise. Read-only.
        self._is_acquired_by_printer: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The state property
        self._state: Optional[print_job_processing_state.PrintJobProcessingState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PrintJobStatus:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PrintJobStatus
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PrintJobStatus()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. A human-readable description of the print job's current processing state. Read-only.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. A human-readable description of the print job's current processing state. Read-only.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def details(self,) -> Optional[List[print_job_state_detail.PrintJobStateDetail]]:
        """
        Gets the details property value. Additional details for print job state. Valid values are described in the following table. Read-only.
        Returns: Optional[List[print_job_state_detail.PrintJobStateDetail]]
        """
        return self._details
    
    @details.setter
    def details(self,value: Optional[List[print_job_state_detail.PrintJobStateDetail]] = None) -> None:
        """
        Sets the details property value. Additional details for print job state. Valid values are described in the following table. Read-only.
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
            "details": lambda n : setattr(self, 'details', n.get_collection_of_enum_values(print_job_state_detail.PrintJobStateDetail)),
            "is_acquired_by_printer": lambda n : setattr(self, 'is_acquired_by_printer', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(print_job_processing_state.PrintJobProcessingState)),
        }
        return fields
    
    @property
    def is_acquired_by_printer(self,) -> Optional[bool]:
        """
        Gets the isAcquiredByPrinter property value. True if the job was acknowledged by a printer; false otherwise. Read-only.
        Returns: Optional[bool]
        """
        return self._is_acquired_by_printer
    
    @is_acquired_by_printer.setter
    def is_acquired_by_printer(self,value: Optional[bool] = None) -> None:
        """
        Sets the isAcquiredByPrinter property value. True if the job was acknowledged by a printer; false otherwise. Read-only.
        Args:
            value: Value to set for the isAcquiredByPrinter property.
        """
        self._is_acquired_by_printer = value
    
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("description", self.description)
        writer.write_enum_value("details", self.details)
        writer.write_bool_value("isAcquiredByPrinter", self.is_acquired_by_printer)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("state", self.state)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def state(self,) -> Optional[print_job_processing_state.PrintJobProcessingState]:
        """
        Gets the state property value. The state property
        Returns: Optional[print_job_processing_state.PrintJobProcessingState]
        """
        return self._state
    
    @state.setter
    def state(self,value: Optional[print_job_processing_state.PrintJobProcessingState] = None) -> None:
        """
        Sets the state property value. The state property
        Args:
            value: Value to set for the state property.
        """
        self._state = value
    

