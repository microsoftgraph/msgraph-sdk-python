from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

alert_feedback = lazy_import('msgraph.generated.models.alert_feedback')
alert_status = lazy_import('msgraph.generated.models.alert_status')

class AlertHistoryState(AdditionalDataHolder, Parsable):
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
    def app_id(self,) -> Optional[str]:
        """
        Gets the appId property value. The appId property
        Returns: Optional[str]
        """
        return self._app_id
    
    @app_id.setter
    def app_id(self,value: Optional[str] = None) -> None:
        """
        Sets the appId property value. The appId property
        Args:
            value: Value to set for the appId property.
        """
        self._app_id = value
    
    @property
    def assigned_to(self,) -> Optional[str]:
        """
        Gets the assignedTo property value. The assignedTo property
        Returns: Optional[str]
        """
        return self._assigned_to
    
    @assigned_to.setter
    def assigned_to(self,value: Optional[str] = None) -> None:
        """
        Sets the assignedTo property value. The assignedTo property
        Args:
            value: Value to set for the assignedTo property.
        """
        self._assigned_to = value
    
    @property
    def comments(self,) -> Optional[List[str]]:
        """
        Gets the comments property value. The comments property
        Returns: Optional[List[str]]
        """
        return self._comments
    
    @comments.setter
    def comments(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the comments property value. The comments property
        Args:
            value: Value to set for the comments property.
        """
        self._comments = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new alertHistoryState and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The appId property
        self._app_id: Optional[str] = None
        # The assignedTo property
        self._assigned_to: Optional[str] = None
        # The comments property
        self._comments: Optional[List[str]] = None
        # The feedback property
        self._feedback: Optional[alert_feedback.AlertFeedback] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The status property
        self._status: Optional[alert_status.AlertStatus] = None
        # The updatedDateTime property
        self._updated_date_time: Optional[datetime] = None
        # The user property
        self._user: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AlertHistoryState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AlertHistoryState
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AlertHistoryState()
    
    @property
    def feedback(self,) -> Optional[alert_feedback.AlertFeedback]:
        """
        Gets the feedback property value. The feedback property
        Returns: Optional[alert_feedback.AlertFeedback]
        """
        return self._feedback
    
    @feedback.setter
    def feedback(self,value: Optional[alert_feedback.AlertFeedback] = None) -> None:
        """
        Sets the feedback property value. The feedback property
        Args:
            value: Value to set for the feedback property.
        """
        self._feedback = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "app_id": lambda n : setattr(self, 'app_id', n.get_str_value()),
            "assigned_to": lambda n : setattr(self, 'assigned_to', n.get_str_value()),
            "comments": lambda n : setattr(self, 'comments', n.get_collection_of_primitive_values(str)),
            "feedback": lambda n : setattr(self, 'feedback', n.get_enum_value(alert_feedback.AlertFeedback)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(alert_status.AlertStatus)),
            "updated_date_time": lambda n : setattr(self, 'updated_date_time', n.get_datetime_value()),
            "user": lambda n : setattr(self, 'user', n.get_str_value()),
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
        writer.write_str_value("appId", self.app_id)
        writer.write_str_value("assignedTo", self.assigned_to)
        writer.write_collection_of_primitive_values("comments", self.comments)
        writer.write_enum_value("feedback", self.feedback)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("status", self.status)
        writer.write_datetime_value("updatedDateTime", self.updated_date_time)
        writer.write_str_value("user", self.user)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def status(self,) -> Optional[alert_status.AlertStatus]:
        """
        Gets the status property value. The status property
        Returns: Optional[alert_status.AlertStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[alert_status.AlertStatus] = None) -> None:
        """
        Sets the status property value. The status property
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    
    @property
    def updated_date_time(self,) -> Optional[datetime]:
        """
        Gets the updatedDateTime property value. The updatedDateTime property
        Returns: Optional[datetime]
        """
        return self._updated_date_time
    
    @updated_date_time.setter
    def updated_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the updatedDateTime property value. The updatedDateTime property
        Args:
            value: Value to set for the updatedDateTime property.
        """
        self._updated_date_time = value
    
    @property
    def user(self,) -> Optional[str]:
        """
        Gets the user property value. The user property
        Returns: Optional[str]
        """
        return self._user
    
    @user.setter
    def user(self,value: Optional[str] = None) -> None:
        """
        Sets the user property value. The user property
        Args:
            value: Value to set for the user property.
        """
        self._user = value
    

