from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from ..identity_set import IdentitySet
    from .action_after_retention_period import ActionAfterRetentionPeriod
    from .behavior_during_retention_period import BehaviorDuringRetentionPeriod
    from .default_record_behavior import DefaultRecordBehavior
    from .disposition_review_stage import DispositionReviewStage
    from .file_plan_descriptor import FilePlanDescriptor
    from .retention_duration import RetentionDuration
    from .retention_event_type import RetentionEventType
    from .retention_trigger import RetentionTrigger

from ..entity import Entity

@dataclass
class RetentionLabel(Entity):
    # Specifies the action to take on the labeled document after the period specified by the retentionDuration property expires. The possible values are: none, delete, startDispositionReview, unknownFutureValue.
    action_after_retention_period: Optional[ActionAfterRetentionPeriod] = None
    # Specifies how the behavior of a document with this label should be during the retention period. The possible values are: doNotRetain, retain, retainAsRecord, retainAsRegulatoryRecord, unknownFutureValue.
    behavior_during_retention_period: Optional[BehaviorDuringRetentionPeriod] = None
    # Represents the user who created the retentionLabel.
    created_by: Optional[IdentitySet] = None
    # Represents the date and time in which the retentionLabel is created.
    created_date_time: Optional[datetime.datetime] = None
    # Specifies the locked or unlocked state of a record label when it is created.The possible values are: startLocked, startUnlocked, unknownFutureValue.
    default_record_behavior: Optional[DefaultRecordBehavior] = None
    # Provides label information for the admin. Optional.
    description_for_admins: Optional[str] = None
    # Provides the label information for the user. Optional.
    description_for_users: Optional[str] = None
    # Represents out-of-the-box values that provide more options to improve the manageability and organization of the content you need to label.
    descriptors: Optional[FilePlanDescriptor] = None
    # Unique string that defines a label name.
    display_name: Optional[str] = None
    # When action at the end of retention is chosen as 'dispositionReview', dispositionReviewStages specifies a sequential set of stages with at least one reviewer in each stage.
    disposition_review_stages: Optional[List[DispositionReviewStage]] = None
    # Specifies whether the label is currently being used.
    is_in_use: Optional[bool] = None
    # Specifies the replacement label to be applied automatically after the retention period of the current label ends.
    label_to_be_applied: Optional[str] = None
    # The user who last modified the retentionLabel.
    last_modified_by: Optional[IdentitySet] = None
    # The latest date time when the retentionLabel was modified.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Specifies the number of days to retain the content.
    retention_duration: Optional[RetentionDuration] = None
    # Represents the type associated with a retention event.
    retention_event_type: Optional[RetentionEventType] = None
    # Specifies whether the retention duration is calculated from the content creation date, labeled date, or last modification date. The possible values are: dateLabeled, dateCreated, dateModified, dateOfEvent, unknownFutureValue.
    retention_trigger: Optional[RetentionTrigger] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RetentionLabel:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RetentionLabel
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RetentionLabel()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from ..identity_set import IdentitySet
        from .action_after_retention_period import ActionAfterRetentionPeriod
        from .behavior_during_retention_period import BehaviorDuringRetentionPeriod
        from .default_record_behavior import DefaultRecordBehavior
        from .disposition_review_stage import DispositionReviewStage
        from .file_plan_descriptor import FilePlanDescriptor
        from .retention_duration import RetentionDuration
        from .retention_event_type import RetentionEventType
        from .retention_trigger import RetentionTrigger

        from ..entity import Entity
        from ..identity_set import IdentitySet
        from .action_after_retention_period import ActionAfterRetentionPeriod
        from .behavior_during_retention_period import BehaviorDuringRetentionPeriod
        from .default_record_behavior import DefaultRecordBehavior
        from .disposition_review_stage import DispositionReviewStage
        from .file_plan_descriptor import FilePlanDescriptor
        from .retention_duration import RetentionDuration
        from .retention_event_type import RetentionEventType
        from .retention_trigger import RetentionTrigger

        fields: Dict[str, Callable[[Any], None]] = {
            "actionAfterRetentionPeriod": lambda n : setattr(self, 'action_after_retention_period', n.get_enum_value(ActionAfterRetentionPeriod)),
            "behaviorDuringRetentionPeriod": lambda n : setattr(self, 'behavior_during_retention_period', n.get_enum_value(BehaviorDuringRetentionPeriod)),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(IdentitySet)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "defaultRecordBehavior": lambda n : setattr(self, 'default_record_behavior', n.get_enum_value(DefaultRecordBehavior)),
            "descriptionForAdmins": lambda n : setattr(self, 'description_for_admins', n.get_str_value()),
            "descriptionForUsers": lambda n : setattr(self, 'description_for_users', n.get_str_value()),
            "descriptors": lambda n : setattr(self, 'descriptors', n.get_object_value(FilePlanDescriptor)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "dispositionReviewStages": lambda n : setattr(self, 'disposition_review_stages', n.get_collection_of_object_values(DispositionReviewStage)),
            "isInUse": lambda n : setattr(self, 'is_in_use', n.get_bool_value()),
            "labelToBeApplied": lambda n : setattr(self, 'label_to_be_applied', n.get_str_value()),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(IdentitySet)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "retentionDuration": lambda n : setattr(self, 'retention_duration', n.get_object_value(RetentionDuration)),
            "retentionEventType": lambda n : setattr(self, 'retention_event_type', n.get_object_value(RetentionEventType)),
            "retentionTrigger": lambda n : setattr(self, 'retention_trigger', n.get_enum_value(RetentionTrigger)),
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
        writer.write_enum_value("actionAfterRetentionPeriod", self.action_after_retention_period)
        writer.write_enum_value("behaviorDuringRetentionPeriod", self.behavior_during_retention_period)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_enum_value("defaultRecordBehavior", self.default_record_behavior)
        writer.write_str_value("descriptionForAdmins", self.description_for_admins)
        writer.write_str_value("descriptionForUsers", self.description_for_users)
        writer.write_object_value("descriptors", self.descriptors)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("dispositionReviewStages", self.disposition_review_stages)
        writer.write_bool_value("isInUse", self.is_in_use)
        writer.write_str_value("labelToBeApplied", self.label_to_be_applied)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_object_value("retentionDuration", self.retention_duration)
        writer.write_object_value("retentionEventType", self.retention_event_type)
        writer.write_enum_value("retentionTrigger", self.retention_trigger)
    

