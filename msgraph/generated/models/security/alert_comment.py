from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class AlertComment(AdditionalDataHolder, Parsable):
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
    def comment(self,) -> Optional[str]:
        """
        Gets the comment property value. The comment text.
        Returns: Optional[str]
        """
        return self._comment
    
    @comment.setter
    def comment(self,value: Optional[str] = None) -> None:
        """
        Sets the comment property value. The comment text.
        Args:
            value: Value to set for the comment property.
        """
        self._comment = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new alertComment and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The comment text.
        self._comment: Optional[str] = None
        # The person or app name that submitted the comment.
        self._created_by_display_name: Optional[str] = None
        # The time when the comment was submitted.
        self._created_date_time: Optional[datetime] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @property
    def created_by_display_name(self,) -> Optional[str]:
        """
        Gets the createdByDisplayName property value. The person or app name that submitted the comment.
        Returns: Optional[str]
        """
        return self._created_by_display_name
    
    @created_by_display_name.setter
    def created_by_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the createdByDisplayName property value. The person or app name that submitted the comment.
        Args:
            value: Value to set for the createdByDisplayName property.
        """
        self._created_by_display_name = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The time when the comment was submitted.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The time when the comment was submitted.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AlertComment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AlertComment
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AlertComment()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "comment": lambda n : setattr(self, 'comment', n.get_str_value()),
            "created_by_display_name": lambda n : setattr(self, 'created_by_display_name', n.get_str_value()),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
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
        writer.write_str_value("comment", self.comment)
        writer.write_str_value("createdByDisplayName", self.created_by_display_name)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

