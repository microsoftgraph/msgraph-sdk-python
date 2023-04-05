from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import event_status_type
    from .. import public_error

class RetentionEventStatus(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new retentionEventStatus and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The error if the status is not successful.
        self._error: Optional[public_error.PublicError] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The status of the distribution. The possible values are: pending, error, success, notAvaliable.
        self._status: Optional[event_status_type.EventStatusType] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RetentionEventStatus:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RetentionEventStatus
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RetentionEventStatus()
    
    @property
    def error(self,) -> Optional[public_error.PublicError]:
        """
        Gets the error property value. The error if the status is not successful.
        Returns: Optional[public_error.PublicError]
        """
        return self._error
    
    @error.setter
    def error(self,value: Optional[public_error.PublicError] = None) -> None:
        """
        Sets the error property value. The error if the status is not successful.
        Args:
            value: Value to set for the error property.
        """
        self._error = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import event_status_type
        from .. import public_error

        fields: Dict[str, Callable[[Any], None]] = {
            "error": lambda n : setattr(self, 'error', n.get_object_value(public_error.PublicError)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(event_status_type.EventStatusType)),
        }
        return fields
    
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
        writer.write_object_value("error", self.error)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def status(self,) -> Optional[event_status_type.EventStatusType]:
        """
        Gets the status property value. The status of the distribution. The possible values are: pending, error, success, notAvaliable.
        Returns: Optional[event_status_type.EventStatusType]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[event_status_type.EventStatusType] = None) -> None:
        """
        Sets the status property value. The status of the distribution. The possible values are: pending, error, success, notAvaliable.
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    

