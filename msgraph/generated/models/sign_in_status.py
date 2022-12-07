from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class SignInStatus(AdditionalDataHolder, Parsable):
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
    def additional_details(self,) -> Optional[str]:
        """
        Gets the additionalDetails property value. Provides additional details on the sign-in activity
        Returns: Optional[str]
        """
        return self._additional_details
    
    @additional_details.setter
    def additional_details(self,value: Optional[str] = None) -> None:
        """
        Sets the additionalDetails property value. Provides additional details on the sign-in activity
        Args:
            value: Value to set for the additionalDetails property.
        """
        self._additional_details = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new signInStatus and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Provides additional details on the sign-in activity
        self._additional_details: Optional[str] = None
        # Provides the 5-6 digit error code that's generated during a sign-in failure. Check out the list of error codes and messages.
        self._error_code: Optional[int] = None
        # Provides the error message or the reason for failure for the corresponding sign-in activity. Check out the list of error codes and messages.
        self._failure_reason: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SignInStatus:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SignInStatus
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SignInStatus()
    
    @property
    def error_code(self,) -> Optional[int]:
        """
        Gets the errorCode property value. Provides the 5-6 digit error code that's generated during a sign-in failure. Check out the list of error codes and messages.
        Returns: Optional[int]
        """
        return self._error_code
    
    @error_code.setter
    def error_code(self,value: Optional[int] = None) -> None:
        """
        Sets the errorCode property value. Provides the 5-6 digit error code that's generated during a sign-in failure. Check out the list of error codes and messages.
        Args:
            value: Value to set for the errorCode property.
        """
        self._error_code = value
    
    @property
    def failure_reason(self,) -> Optional[str]:
        """
        Gets the failureReason property value. Provides the error message or the reason for failure for the corresponding sign-in activity. Check out the list of error codes and messages.
        Returns: Optional[str]
        """
        return self._failure_reason
    
    @failure_reason.setter
    def failure_reason(self,value: Optional[str] = None) -> None:
        """
        Sets the failureReason property value. Provides the error message or the reason for failure for the corresponding sign-in activity. Check out the list of error codes and messages.
        Args:
            value: Value to set for the failureReason property.
        """
        self._failure_reason = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "additional_details": lambda n : setattr(self, 'additional_details', n.get_str_value()),
            "error_code": lambda n : setattr(self, 'error_code', n.get_int_value()),
            "failure_reason": lambda n : setattr(self, 'failure_reason', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_str_value("additionalDetails", self.additional_details)
        writer.write_int_value("errorCode", self.error_code)
        writer.write_str_value("failureReason", self.failure_reason)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

