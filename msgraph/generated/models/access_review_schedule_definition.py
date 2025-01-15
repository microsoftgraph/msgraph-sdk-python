from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_review_instance import AccessReviewInstance
    from .access_review_notification_recipient_item import AccessReviewNotificationRecipientItem
    from .access_review_reviewer_scope import AccessReviewReviewerScope
    from .access_review_schedule_settings import AccessReviewScheduleSettings
    from .access_review_scope import AccessReviewScope
    from .access_review_stage_settings import AccessReviewStageSettings
    from .entity import Entity
    from .user_identity import UserIdentity

from .entity import Entity

@dataclass
class AccessReviewScheduleDefinition(Entity, Parsable):
    # Defines the list of additional users or group members to be notified of the access review progress.
    additional_notification_recipients: Optional[list[AccessReviewNotificationRecipientItem]] = None
    # User who created this review. Read-only.
    created_by: Optional[UserIdentity] = None
    # Timestamp when the access review series was created. Supports $select. Read-only.
    created_date_time: Optional[datetime.datetime] = None
    # Description provided by review creators to provide more context of the review to admins. Supports $select.
    description_for_admins: Optional[str] = None
    # Description provided  by review creators to provide more context of the review to reviewers. Reviewers see this description in the email sent to them requesting their review. Email notifications support up to 256 characters. Supports $select.
    description_for_reviewers: Optional[str] = None
    # Name of the access review series. Supports $select and $orderby. Required on create.
    display_name: Optional[str] = None
    # This collection of reviewer scopes is used to define the list of fallback reviewers. These fallback reviewers are notified to take action if no users are found from the list of reviewers specified. This could occur when either the group owner is specified as the reviewer but the group owner doesn't exist, or manager is specified as reviewer but a user's manager doesn't exist. See accessReviewReviewerScope. Replaces backupReviewers. Supports $select. NOTE: The value of this property will be ignored if fallback reviewers are assigned through the stageSettings property.
    fallback_reviewers: Optional[list[AccessReviewReviewerScope]] = None
    # This property is required when scoping a review to guest users' access across all Microsoft 365 groups and determines which Microsoft 365 groups are reviewed. Each group becomes a unique accessReviewInstance of the access review series.  For supported scopes, see accessReviewScope. Supports $select. For examples of options for configuring instanceEnumerationScope, see Configure the scope of your access review definition using the Microsoft Graph API.
    instance_enumeration_scope: Optional[AccessReviewScope] = None
    # If the accessReviewScheduleDefinition is a recurring access review, instances represent each recurrence. A review that doesn't recur will have exactly one instance. Instances also represent each unique resource under review in the accessReviewScheduleDefinition. If a review has multiple resources and multiple instances, each resource has a unique instance for each recurrence.
    instances: Optional[list[AccessReviewInstance]] = None
    # Timestamp when the access review series was last modified. Supports $select. Read-only.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # This collection of access review scopes is used to define who are the reviewers. The reviewers property is only updatable if individual users are assigned as reviewers. Required on create. Supports $select. For examples of options for assigning reviewers, see Assign reviewers to your access review definition using the Microsoft Graph API. NOTE: The value of this property will be ignored if reviewers are assigned through the stageSettings property.
    reviewers: Optional[list[AccessReviewReviewerScope]] = None
    # Defines the entities whose access is reviewed. For supported scopes, see accessReviewScope. Required on create. Supports $select and $filter (contains only). For examples of options for configuring scope, see Configure the scope of your access review definition using the Microsoft Graph API.
    scope: Optional[AccessReviewScope] = None
    # The settings for an access review series, see type definition below. Supports $select. Required on create.
    settings: Optional[AccessReviewScheduleSettings] = None
    # Required only for a multi-stage access review to define the stages and their settings. You can break down each review instance into up to three sequential stages, where each stage can have a different set of reviewers, fallback reviewers, and settings. Stages are created sequentially based on the dependsOn property. Optional.  When this property is defined, its settings are used instead of the corresponding settings in the accessReviewScheduleDefinition object and its settings, reviewers, and fallbackReviewers properties.
    stage_settings: Optional[list[AccessReviewStageSettings]] = None
    # This read-only field specifies the status of an access review. The typical states include Initializing, NotStarted, Starting, InProgress, Completing, Completed, AutoReviewing, and AutoReviewed.  Supports $select, $orderby, and $filter (eq only). Read-only.
    status: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AccessReviewScheduleDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AccessReviewScheduleDefinition
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AccessReviewScheduleDefinition()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .access_review_instance import AccessReviewInstance
        from .access_review_notification_recipient_item import AccessReviewNotificationRecipientItem
        from .access_review_reviewer_scope import AccessReviewReviewerScope
        from .access_review_schedule_settings import AccessReviewScheduleSettings
        from .access_review_scope import AccessReviewScope
        from .access_review_stage_settings import AccessReviewStageSettings
        from .entity import Entity
        from .user_identity import UserIdentity

        from .access_review_instance import AccessReviewInstance
        from .access_review_notification_recipient_item import AccessReviewNotificationRecipientItem
        from .access_review_reviewer_scope import AccessReviewReviewerScope
        from .access_review_schedule_settings import AccessReviewScheduleSettings
        from .access_review_scope import AccessReviewScope
        from .access_review_stage_settings import AccessReviewStageSettings
        from .entity import Entity
        from .user_identity import UserIdentity

        fields: dict[str, Callable[[Any], None]] = {
            "additionalNotificationRecipients": lambda n : setattr(self, 'additional_notification_recipients', n.get_collection_of_object_values(AccessReviewNotificationRecipientItem)),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(UserIdentity)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "descriptionForAdmins": lambda n : setattr(self, 'description_for_admins', n.get_str_value()),
            "descriptionForReviewers": lambda n : setattr(self, 'description_for_reviewers', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "fallbackReviewers": lambda n : setattr(self, 'fallback_reviewers', n.get_collection_of_object_values(AccessReviewReviewerScope)),
            "instanceEnumerationScope": lambda n : setattr(self, 'instance_enumeration_scope', n.get_object_value(AccessReviewScope)),
            "instances": lambda n : setattr(self, 'instances', n.get_collection_of_object_values(AccessReviewInstance)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "reviewers": lambda n : setattr(self, 'reviewers', n.get_collection_of_object_values(AccessReviewReviewerScope)),
            "scope": lambda n : setattr(self, 'scope', n.get_object_value(AccessReviewScope)),
            "settings": lambda n : setattr(self, 'settings', n.get_object_value(AccessReviewScheduleSettings)),
            "stageSettings": lambda n : setattr(self, 'stage_settings', n.get_collection_of_object_values(AccessReviewStageSettings)),
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
        writer.write_collection_of_object_values("additionalNotificationRecipients", self.additional_notification_recipients)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("descriptionForAdmins", self.description_for_admins)
        writer.write_str_value("descriptionForReviewers", self.description_for_reviewers)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("fallbackReviewers", self.fallback_reviewers)
        writer.write_object_value("instanceEnumerationScope", self.instance_enumeration_scope)
        writer.write_collection_of_object_values("instances", self.instances)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_collection_of_object_values("reviewers", self.reviewers)
        writer.write_object_value("scope", self.scope)
        writer.write_object_value("settings", self.settings)
        writer.write_collection_of_object_values("stageSettings", self.stage_settings)
        writer.write_str_value("status", self.status)
    

