from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

reject_reason = lazy_import('msgraph.generated.models.reject_reason')

class RejectPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the reject method.
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
    
    @property
    def callback_uri(self,) -> Optional[str]:
        """
        Gets the callbackUri property value. The callbackUri property
        Returns: Optional[str]
        """
        return self._callback_uri
    
    @callback_uri.setter
    def callback_uri(self,value: Optional[str] = None) -> None:
        """
        Sets the callbackUri property value. The callbackUri property
        Args:
            value: Value to set for the callbackUri property.
        """
        self._callback_uri = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new rejectPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The callbackUri property
        self._callback_uri: Optional[str] = None
        # The reason property
        self._reason: Optional[reject_reason.RejectReason] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RejectPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RejectPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RejectPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "callback_uri": lambda n : setattr(self, 'callback_uri', n.get_str_value()),
            "reason": lambda n : setattr(self, 'reason', n.get_enum_value(reject_reason.RejectReason)),
        }
        return fields
    
    @property
    def reason(self,) -> Optional[reject_reason.RejectReason]:
        """
        Gets the reason property value. The reason property
        Returns: Optional[reject_reason.RejectReason]
        """
        return self._reason
    
    @reason.setter
    def reason(self,value: Optional[reject_reason.RejectReason] = None) -> None:
        """
        Sets the reason property value. The reason property
        Args:
            value: Value to set for the reason property.
        """
        self._reason = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("callbackUri", self.callback_uri)
        writer.write_enum_value("reason", self.reason)
        writer.write_additional_data_value(self.additional_data)
    

