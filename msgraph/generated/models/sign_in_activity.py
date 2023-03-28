from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class SignInActivity(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new signInActivity and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The lastNonInteractiveSignInDateTime property
        self._last_non_interactive_sign_in_date_time: Optional[datetime] = None
        # The lastNonInteractiveSignInRequestId property
        self._last_non_interactive_sign_in_request_id: Optional[str] = None
        # The lastSignInDateTime property
        self._last_sign_in_date_time: Optional[datetime] = None
        # The lastSignInRequestId property
        self._last_sign_in_request_id: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SignInActivity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SignInActivity
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SignInActivity()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "lastNonInteractiveSignInDateTime": lambda n : setattr(self, 'last_non_interactive_sign_in_date_time', n.get_datetime_value()),
            "lastNonInteractiveSignInRequestId": lambda n : setattr(self, 'last_non_interactive_sign_in_request_id', n.get_str_value()),
            "lastSignInDateTime": lambda n : setattr(self, 'last_sign_in_date_time', n.get_datetime_value()),
            "lastSignInRequestId": lambda n : setattr(self, 'last_sign_in_request_id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def last_non_interactive_sign_in_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastNonInteractiveSignInDateTime property value. The lastNonInteractiveSignInDateTime property
        Returns: Optional[datetime]
        """
        return self._last_non_interactive_sign_in_date_time
    
    @last_non_interactive_sign_in_date_time.setter
    def last_non_interactive_sign_in_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastNonInteractiveSignInDateTime property value. The lastNonInteractiveSignInDateTime property
        Args:
            value: Value to set for the last_non_interactive_sign_in_date_time property.
        """
        self._last_non_interactive_sign_in_date_time = value
    
    @property
    def last_non_interactive_sign_in_request_id(self,) -> Optional[str]:
        """
        Gets the lastNonInteractiveSignInRequestId property value. The lastNonInteractiveSignInRequestId property
        Returns: Optional[str]
        """
        return self._last_non_interactive_sign_in_request_id
    
    @last_non_interactive_sign_in_request_id.setter
    def last_non_interactive_sign_in_request_id(self,value: Optional[str] = None) -> None:
        """
        Sets the lastNonInteractiveSignInRequestId property value. The lastNonInteractiveSignInRequestId property
        Args:
            value: Value to set for the last_non_interactive_sign_in_request_id property.
        """
        self._last_non_interactive_sign_in_request_id = value
    
    @property
    def last_sign_in_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastSignInDateTime property value. The lastSignInDateTime property
        Returns: Optional[datetime]
        """
        return self._last_sign_in_date_time
    
    @last_sign_in_date_time.setter
    def last_sign_in_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastSignInDateTime property value. The lastSignInDateTime property
        Args:
            value: Value to set for the last_sign_in_date_time property.
        """
        self._last_sign_in_date_time = value
    
    @property
    def last_sign_in_request_id(self,) -> Optional[str]:
        """
        Gets the lastSignInRequestId property value. The lastSignInRequestId property
        Returns: Optional[str]
        """
        return self._last_sign_in_request_id
    
    @last_sign_in_request_id.setter
    def last_sign_in_request_id(self,value: Optional[str] = None) -> None:
        """
        Sets the lastSignInRequestId property value. The lastSignInRequestId property
        Args:
            value: Value to set for the last_sign_in_request_id property.
        """
        self._last_sign_in_request_id = value
    
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
        writer.write_datetime_value("lastNonInteractiveSignInDateTime", self.last_non_interactive_sign_in_date_time)
        writer.write_str_value("lastNonInteractiveSignInRequestId", self.last_non_interactive_sign_in_request_id)
        writer.write_datetime_value("lastSignInDateTime", self.last_sign_in_date_time)
        writer.write_str_value("lastSignInRequestId", self.last_sign_in_request_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

