from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

error_details = lazy_import('msgraph.generated.models.o_data_errors.error_details')
inner_error = lazy_import('msgraph.generated.models.o_data_errors.inner_error')

class MainError(AdditionalDataHolder, Parsable):
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
    
    @property
    def code(self,) -> Optional[str]:
        """
        Gets the code property value. The code property
        Returns: Optional[str]
        """
        return self._code
    
    @code.setter
    def code(self,value: Optional[str] = None) -> None:
        """
        Sets the code property value. The code property
        Args:
            value: Value to set for the code property.
        """
        self._code = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new MainError and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The code property
        self._code: Optional[str] = None
        # The details property
        self._details: Optional[List[error_details.ErrorDetails]] = None
        # The innererror property
        self._innererror: Optional[inner_error.InnerError] = None
        # The message property
        self._message: Optional[str] = None
        # The target property
        self._target: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MainError:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MainError
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MainError()
    
    @property
    def details(self,) -> Optional[List[error_details.ErrorDetails]]:
        """
        Gets the details property value. The details property
        Returns: Optional[List[error_details.ErrorDetails]]
        """
        return self._details
    
    @details.setter
    def details(self,value: Optional[List[error_details.ErrorDetails]] = None) -> None:
        """
        Sets the details property value. The details property
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
            "code": lambda n : setattr(self, 'code', n.get_str_value()),
            "details": lambda n : setattr(self, 'details', n.get_collection_of_object_values(error_details.ErrorDetails)),
            "innererror": lambda n : setattr(self, 'innererror', n.get_object_value(inner_error.InnerError)),
            "message": lambda n : setattr(self, 'message', n.get_str_value()),
            "target": lambda n : setattr(self, 'target', n.get_str_value()),
        }
        return fields
    
    @property
    def innererror(self,) -> Optional[inner_error.InnerError]:
        """
        Gets the innererror property value. The innererror property
        Returns: Optional[inner_error.InnerError]
        """
        return self._innererror
    
    @innererror.setter
    def innererror(self,value: Optional[inner_error.InnerError] = None) -> None:
        """
        Sets the innererror property value. The innererror property
        Args:
            value: Value to set for the innererror property.
        """
        self._innererror = value
    
    @property
    def message(self,) -> Optional[str]:
        """
        Gets the message property value. The message property
        Returns: Optional[str]
        """
        return self._message
    
    @message.setter
    def message(self,value: Optional[str] = None) -> None:
        """
        Sets the message property value. The message property
        Args:
            value: Value to set for the message property.
        """
        self._message = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("code", self.code)
        writer.write_collection_of_object_values("details", self.details)
        writer.write_object_value("innererror", self.innererror)
        writer.write_str_value("message", self.message)
        writer.write_str_value("target", self.target)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def target(self,) -> Optional[str]:
        """
        Gets the target property value. The target property
        Returns: Optional[str]
        """
        return self._target
    
    @target.setter
    def target(self,value: Optional[str] = None) -> None:
        """
        Sets the target property value. The target property
        Args:
            value: Value to set for the target property.
        """
        self._target = value
    

