from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import alert_feedback, alert_status

@dataclass
class AlertHistoryState(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The appId property
    app_id: Optional[str] = None
    # The assignedTo property
    assigned_to: Optional[str] = None
    # The comments property
    comments: Optional[List[str]] = None
    # The feedback property
    feedback: Optional[alert_feedback.AlertFeedback] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The status property
    status: Optional[alert_status.AlertStatus] = None
    # The updatedDateTime property
    updated_date_time: Optional[datetime] = None
    # The user property
    user: Optional[str] = None
    
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
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import alert_feedback, alert_status

        fields: Dict[str, Callable[[Any], None]] = {
            "appId": lambda n : setattr(self, 'app_id', n.get_str_value()),
            "assignedTo": lambda n : setattr(self, 'assigned_to', n.get_str_value()),
            "comments": lambda n : setattr(self, 'comments', n.get_collection_of_primitive_values(str)),
            "feedback": lambda n : setattr(self, 'feedback', n.get_enum_value(alert_feedback.AlertFeedback)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(alert_status.AlertStatus)),
            "updatedDateTime": lambda n : setattr(self, 'updated_date_time', n.get_datetime_value()),
            "user": lambda n : setattr(self, 'user', n.get_str_value()),
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
        writer.write_str_value("appId", self.app_id)
        writer.write_str_value("assignedTo", self.assigned_to)
        writer.write_collection_of_primitive_values("comments", self.comments)
        writer.write_enum_value("feedback", self.feedback)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("status", self.status)
        writer.write_datetime_value("updatedDateTime", self.updated_date_time)
        writer.write_str_value("user", self.user)
        writer.write_additional_data_value(self.additional_data)
    

