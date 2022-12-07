from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class CheckinPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the checkin method.
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
    def check_in_as(self,) -> Optional[str]:
        """
        Gets the checkInAs property value. The checkInAs property
        Returns: Optional[str]
        """
        return self._check_in_as
    
    @check_in_as.setter
    def check_in_as(self,value: Optional[str] = None) -> None:
        """
        Sets the checkInAs property value. The checkInAs property
        Args:
            value: Value to set for the checkInAs property.
        """
        self._check_in_as = value
    
    @property
    def comment(self,) -> Optional[str]:
        """
        Gets the comment property value. The comment property
        Returns: Optional[str]
        """
        return self._comment
    
    @comment.setter
    def comment(self,value: Optional[str] = None) -> None:
        """
        Sets the comment property value. The comment property
        Args:
            value: Value to set for the comment property.
        """
        self._comment = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new checkinPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The checkInAs property
        self._check_in_as: Optional[str] = None
        # The comment property
        self._comment: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CheckinPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CheckinPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CheckinPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "check_in_as": lambda n : setattr(self, 'check_in_as', n.get_str_value()),
            "comment": lambda n : setattr(self, 'comment', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("checkInAs", self.check_in_as)
        writer.write_str_value("comment", self.comment)
        writer.write_additional_data_value(self.additional_data)
    

