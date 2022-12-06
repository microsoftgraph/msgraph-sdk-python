from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

public_error_detail = lazy_import('msgraph.generated.models.public_error_detail')
public_inner_error = lazy_import('msgraph.generated.models.public_inner_error')

class PublicError(AdditionalDataHolder, Parsable):
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
        Gets the code property value. Represents the error code.
        Returns: Optional[str]
        """
        return self._code
    
    @code.setter
    def code(self,value: Optional[str] = None) -> None:
        """
        Sets the code property value. Represents the error code.
        Args:
            value: Value to set for the code property.
        """
        self._code = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new publicError and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Represents the error code.
        self._code: Optional[str] = None
        # Details of the error.
        self._details: Optional[List[public_error_detail.PublicErrorDetail]] = None
        # Details of the inner error.
        self._inner_error: Optional[public_inner_error.PublicInnerError] = None
        # A non-localized message for the developer.
        self._message: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The target of the error.
        self._target: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PublicError:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PublicError
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PublicError()
    
    @property
    def details(self,) -> Optional[List[public_error_detail.PublicErrorDetail]]:
        """
        Gets the details property value. Details of the error.
        Returns: Optional[List[public_error_detail.PublicErrorDetail]]
        """
        return self._details
    
    @details.setter
    def details(self,value: Optional[List[public_error_detail.PublicErrorDetail]] = None) -> None:
        """
        Sets the details property value. Details of the error.
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
            "details": lambda n : setattr(self, 'details', n.get_collection_of_object_values(public_error_detail.PublicErrorDetail)),
            "inner_error": lambda n : setattr(self, 'inner_error', n.get_object_value(public_inner_error.PublicInnerError)),
            "message": lambda n : setattr(self, 'message', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "target": lambda n : setattr(self, 'target', n.get_str_value()),
        }
        return fields
    
    @property
    def inner_error(self,) -> Optional[public_inner_error.PublicInnerError]:
        """
        Gets the innerError property value. Details of the inner error.
        Returns: Optional[public_inner_error.PublicInnerError]
        """
        return self._inner_error
    
    @inner_error.setter
    def inner_error(self,value: Optional[public_inner_error.PublicInnerError] = None) -> None:
        """
        Sets the innerError property value. Details of the inner error.
        Args:
            value: Value to set for the innerError property.
        """
        self._inner_error = value
    
    @property
    def message(self,) -> Optional[str]:
        """
        Gets the message property value. A non-localized message for the developer.
        Returns: Optional[str]
        """
        return self._message
    
    @message.setter
    def message(self,value: Optional[str] = None) -> None:
        """
        Sets the message property value. A non-localized message for the developer.
        Args:
            value: Value to set for the message property.
        """
        self._message = value
    
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
        writer.write_str_value("code", self.code)
        writer.write_collection_of_object_values("details", self.details)
        writer.write_object_value("innerError", self.inner_error)
        writer.write_str_value("message", self.message)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("target", self.target)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def target(self,) -> Optional[str]:
        """
        Gets the target property value. The target of the error.
        Returns: Optional[str]
        """
        return self._target
    
    @target.setter
    def target(self,value: Optional[str] = None) -> None:
        """
        Sets the target property value. The target of the error.
        Args:
            value: Value to set for the target property.
        """
        self._target = value
    

