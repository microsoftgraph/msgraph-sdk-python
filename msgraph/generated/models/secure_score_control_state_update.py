from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class SecureScoreControlStateUpdate(AdditionalDataHolder, Parsable):
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
    def assigned_to(self,) -> Optional[str]:
        """
        Gets the assignedTo property value. Assigns the control to the user who will take the action.
        Returns: Optional[str]
        """
        return self._assigned_to
    
    @assigned_to.setter
    def assigned_to(self,value: Optional[str] = None) -> None:
        """
        Sets the assignedTo property value. Assigns the control to the user who will take the action.
        Args:
            value: Value to set for the assignedTo property.
        """
        self._assigned_to = value
    
    @property
    def comment(self,) -> Optional[str]:
        """
        Gets the comment property value. Provides optional comment about the control.
        Returns: Optional[str]
        """
        return self._comment
    
    @comment.setter
    def comment(self,value: Optional[str] = None) -> None:
        """
        Sets the comment property value. Provides optional comment about the control.
        Args:
            value: Value to set for the comment property.
        """
        self._comment = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new secureScoreControlStateUpdate and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Assigns the control to the user who will take the action.
        self._assigned_to: Optional[str] = None
        # Provides optional comment about the control.
        self._comment: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # State of the control, which can be modified via a PATCH command (for example, ignored, thirdParty).
        self._state: Optional[str] = None
        # ID of the user who updated tenant state.
        self._updated_by: Optional[str] = None
        # Time at which the control state was updated.
        self._updated_date_time: Optional[datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SecureScoreControlStateUpdate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SecureScoreControlStateUpdate
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SecureScoreControlStateUpdate()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "assigned_to": lambda n : setattr(self, 'assigned_to', n.get_str_value()),
            "comment": lambda n : setattr(self, 'comment', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "state": lambda n : setattr(self, 'state', n.get_str_value()),
            "updated_by": lambda n : setattr(self, 'updated_by', n.get_str_value()),
            "updated_date_time": lambda n : setattr(self, 'updated_date_time', n.get_datetime_value()),
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
        writer.write_str_value("assignedTo", self.assigned_to)
        writer.write_str_value("comment", self.comment)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("state", self.state)
        writer.write_str_value("updatedBy", self.updated_by)
        writer.write_datetime_value("updatedDateTime", self.updated_date_time)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def state(self,) -> Optional[str]:
        """
        Gets the state property value. State of the control, which can be modified via a PATCH command (for example, ignored, thirdParty).
        Returns: Optional[str]
        """
        return self._state
    
    @state.setter
    def state(self,value: Optional[str] = None) -> None:
        """
        Sets the state property value. State of the control, which can be modified via a PATCH command (for example, ignored, thirdParty).
        Args:
            value: Value to set for the state property.
        """
        self._state = value
    
    @property
    def updated_by(self,) -> Optional[str]:
        """
        Gets the updatedBy property value. ID of the user who updated tenant state.
        Returns: Optional[str]
        """
        return self._updated_by
    
    @updated_by.setter
    def updated_by(self,value: Optional[str] = None) -> None:
        """
        Sets the updatedBy property value. ID of the user who updated tenant state.
        Args:
            value: Value to set for the updatedBy property.
        """
        self._updated_by = value
    
    @property
    def updated_date_time(self,) -> Optional[datetime]:
        """
        Gets the updatedDateTime property value. Time at which the control state was updated.
        Returns: Optional[datetime]
        """
        return self._updated_date_time
    
    @updated_date_time.setter
    def updated_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the updatedDateTime property value. Time at which the control state was updated.
        Args:
            value: Value to set for the updatedDateTime property.
        """
        self._updated_date_time = value
    

