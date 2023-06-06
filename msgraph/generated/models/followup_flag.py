from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import date_time_time_zone, followup_flag_status

@dataclass
class FollowupFlag(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The date and time that the follow-up was finished.
    completed_date_time: Optional[date_time_time_zone.DateTimeTimeZone] = None
    # The date and time that the follow up is to be finished. Note: To set the due date, you must also specify the startDateTime; otherwise, you will get a 400 Bad Request response.
    due_date_time: Optional[date_time_time_zone.DateTimeTimeZone] = None
    # The status for follow-up for an item. Possible values are notFlagged, complete, and flagged.
    flag_status: Optional[followup_flag_status.FollowupFlagStatus] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The date and time that the follow-up is to begin.
    start_date_time: Optional[date_time_time_zone.DateTimeTimeZone] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> FollowupFlag:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: FollowupFlag
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return FollowupFlag()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import date_time_time_zone, followup_flag_status

        fields: Dict[str, Callable[[Any], None]] = {
            "completedDateTime": lambda n : setattr(self, 'completed_date_time', n.get_object_value(date_time_time_zone.DateTimeTimeZone)),
            "dueDateTime": lambda n : setattr(self, 'due_date_time', n.get_object_value(date_time_time_zone.DateTimeTimeZone)),
            "flagStatus": lambda n : setattr(self, 'flag_status', n.get_enum_value(followup_flag_status.FollowupFlagStatus)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_object_value(date_time_time_zone.DateTimeTimeZone)),
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
        writer.write_object_value("completedDateTime", self.completed_date_time)
        writer.write_object_value("dueDateTime", self.due_date_time)
        writer.write_enum_value("flagStatus", self.flag_status)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("startDateTime", self.start_date_time)
        writer.write_additional_data_value(self.additional_data)
    

