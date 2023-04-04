from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import event_propagation_status

class EventPropagationResult(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new eventPropagationResult and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The name of the specific location in the workload associated with the event.
        self._location: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The name of the workload associated with the event.
        self._service_name: Optional[str] = None
        # Indicates the status of the event creation request. The possible values are: none, inProcessing, failed, success, unknownFutureValue.
        self._status: Optional[event_propagation_status.EventPropagationStatus] = None
        # Additional information about the status of the event creation request.
        self._status_information: Optional[str] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EventPropagationResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EventPropagationResult
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EventPropagationResult()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import event_propagation_status

        fields: Dict[str, Callable[[Any], None]] = {
            "location": lambda n : setattr(self, 'location', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "serviceName": lambda n : setattr(self, 'service_name', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(event_propagation_status.EventPropagationStatus)),
            "statusInformation": lambda n : setattr(self, 'status_information', n.get_str_value()),
        }
        return fields
    
    @property
    def location(self,) -> Optional[str]:
        """
        Gets the location property value. The name of the specific location in the workload associated with the event.
        Returns: Optional[str]
        """
        return self._location
    
    @location.setter
    def location(self,value: Optional[str] = None) -> None:
        """
        Sets the location property value. The name of the specific location in the workload associated with the event.
        Args:
            value: Value to set for the location property.
        """
        self._location = value
    
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
            value: Value to set for the odata_type property.
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
        writer.write_str_value("location", self.location)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("serviceName", self.service_name)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("statusInformation", self.status_information)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def service_name(self,) -> Optional[str]:
        """
        Gets the serviceName property value. The name of the workload associated with the event.
        Returns: Optional[str]
        """
        return self._service_name
    
    @service_name.setter
    def service_name(self,value: Optional[str] = None) -> None:
        """
        Sets the serviceName property value. The name of the workload associated with the event.
        Args:
            value: Value to set for the service_name property.
        """
        self._service_name = value
    
    @property
    def status(self,) -> Optional[event_propagation_status.EventPropagationStatus]:
        """
        Gets the status property value. Indicates the status of the event creation request. The possible values are: none, inProcessing, failed, success, unknownFutureValue.
        Returns: Optional[event_propagation_status.EventPropagationStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[event_propagation_status.EventPropagationStatus] = None) -> None:
        """
        Sets the status property value. Indicates the status of the event creation request. The possible values are: none, inProcessing, failed, success, unknownFutureValue.
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    
    @property
    def status_information(self,) -> Optional[str]:
        """
        Gets the statusInformation property value. Additional information about the status of the event creation request.
        Returns: Optional[str]
        """
        return self._status_information
    
    @status_information.setter
    def status_information(self,value: Optional[str] = None) -> None:
        """
        Sets the statusInformation property value. Additional information about the status of the event creation request.
        Args:
            value: Value to set for the status_information property.
        """
        self._status_information = value
    

