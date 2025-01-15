from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .identity import Identity

from .entity import Entity

@dataclass
class ApprovalStage(Entity, Parsable):
    # Indicates whether the stage is assigned to the calling user to review. Read-only.
    assigned_to_me: Optional[bool] = None
    # The label provided by the policy creator to identify an approval stage. Read-only.
    display_name: Optional[str] = None
    # The justification associated with the approval stage decision.
    justification: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The result of this approval record. Possible values include: NotReviewed, Approved, Denied.
    review_result: Optional[str] = None
    # The identifier of the reviewer. 00000000-0000-0000-0000-000000000000 if the assigned reviewer hasn't reviewed. Read-only.
    reviewed_by: Optional[Identity] = None
    # The date and time when a decision was recorded. The date and time information uses ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
    reviewed_date_time: Optional[datetime.datetime] = None
    # The stage status. Possible values: InProgress, Initializing, Completed, Expired. Read-only.
    status: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ApprovalStage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ApprovalStage
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ApprovalStage()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .identity import Identity

        from .entity import Entity
        from .identity import Identity

        fields: dict[str, Callable[[Any], None]] = {
            "assignedToMe": lambda n : setattr(self, 'assigned_to_me', n.get_bool_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "justification": lambda n : setattr(self, 'justification', n.get_str_value()),
            "reviewResult": lambda n : setattr(self, 'review_result', n.get_str_value()),
            "reviewedBy": lambda n : setattr(self, 'reviewed_by', n.get_object_value(Identity)),
            "reviewedDateTime": lambda n : setattr(self, 'reviewed_date_time', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_bool_value("assignedToMe", self.assigned_to_me)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("justification", self.justification)
        writer.write_str_value("reviewResult", self.review_result)
        writer.write_object_value("reviewedBy", self.reviewed_by)
        writer.write_datetime_value("reviewedDateTime", self.reviewed_date_time)
        writer.write_str_value("status", self.status)
    

