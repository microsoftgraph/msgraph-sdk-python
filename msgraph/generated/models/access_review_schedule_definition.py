from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import access_review_instance, access_review_notification_recipient_item, access_review_reviewer_scope, access_review_schedule_settings, access_review_scope, access_review_stage_settings, entity, user_identity

from . import entity

@dataclass
class AccessReviewScheduleDefinition(entity.Entity):
    # Defines the list of additional users or group members to be notified of the access review progress.
    additional_notification_recipients: Optional[List[access_review_notification_recipient_item.AccessReviewNotificationRecipientItem]] = None
    # User who created this review. Read-only.
    created_by: Optional[user_identity.UserIdentity] = None
    # Timestamp when the access review series was created. Supports $select. Read-only.
    created_date_time: Optional[datetime] = None
    # Description provided by review creators to provide more context of the review to admins. Supports $select.
    description_for_admins: Optional[str] = None
    # Description provided  by review creators to provide more context of the review to reviewers. Reviewers will see this description in the email sent to them requesting their review. Email notifications support up to 256 characters. Supports $select.
    description_for_reviewers: Optional[str] = None
    # Name of the access review series. Supports $select and $orderBy. Required on create.
    display_name: Optional[str] = None
    # This collection of reviewer scopes is used to define the list of fallback reviewers. These fallback reviewers will be notified to take action if no users are found from the list of reviewers specified. This could occur when either the group owner is specified as the reviewer but the group owner does not exist, or manager is specified as reviewer but a user's manager does not exist. See accessReviewReviewerScope. Replaces backupReviewers. Supports $select. NOTE: The value of this property will be ignored if fallback reviewers are assigned through the stageSettings property.
    fallback_reviewers: Optional[List[access_review_reviewer_scope.AccessReviewReviewerScope]] = None
    # This property is required when scoping a review to guest users' access across all Microsoft 365 groups and determines which Microsoft 365 groups are reviewed. Each group will become a unique accessReviewInstance of the access review series.  For supported scopes, see accessReviewScope. Supports $select. For examples of options for configuring instanceEnumerationScope, see Configure the scope of your access review definition using the Microsoft Graph API.
    instance_enumeration_scope: Optional[access_review_scope.AccessReviewScope] = None
    # If the accessReviewScheduleDefinition is a recurring access review, instances represent each recurrence. A review that does not recur will have exactly one instance. Instances also represent each unique resource under review in the accessReviewScheduleDefinition. If a review has multiple resources and multiple instances, each resource will have a unique instance for each recurrence.
    instances: Optional[List[access_review_instance.AccessReviewInstance]] = None
    # Timestamp when the access review series was last modified. Supports $select. Read-only.
    last_modified_date_time: Optional[datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # This collection of access review scopes is used to define who are the reviewers. The reviewers property is only updatable if individual users are assigned as reviewers. Required on create. Supports $select. For examples of options for assigning reviewers, see Assign reviewers to your access review definition using the Microsoft Graph API. NOTE: The value of this property will be ignored if reviewers are assigned through the stageSettings property.
    reviewers: Optional[List[access_review_reviewer_scope.AccessReviewReviewerScope]] = None
    # Defines the entities whose access is reviewed. For supported scopes, see accessReviewScope. Required on create. Supports $select and $filter (contains only). For examples of options for configuring scope, see Configure the scope of your access review definition using the Microsoft Graph API.
    scope: Optional[access_review_scope.AccessReviewScope] = None
    # The settings for an access review series, see type definition below. Supports $select. Required on create.
    settings: Optional[access_review_schedule_settings.AccessReviewScheduleSettings] = None
    # Required only for a multi-stage access review to define the stages and their settings. You can break down each review instance into up to three sequential stages, where each stage can have a different set of reviewers, fallback reviewers, and settings. Stages will be created sequentially based on the dependsOn property. Optional.  When this property is defined, its settings are used instead of the corresponding settings in the accessReviewScheduleDefinition object and its settings, reviewers, and fallbackReviewers properties.
    stage_settings: Optional[List[access_review_stage_settings.AccessReviewStageSettings]] = None
    # This read-only field specifies the status of an access review. The typical states include Initializing, NotStarted, Starting, InProgress, Completing, Completed, AutoReviewing, and AutoReviewed.  Supports $select, $orderby, and $filter (eq only). Read-only.
    status: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessReviewScheduleDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessReviewScheduleDefinition
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AccessReviewScheduleDefinition()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import access_review_instance, access_review_notification_recipient_item, access_review_reviewer_scope, access_review_schedule_settings, access_review_scope, access_review_stage_settings, entity, user_identity

        fields: Dict[str, Callable[[Any], None]] = {
            "additionalNotificationRecipients": lambda n : setattr(self, 'additional_notification_recipients', n.get_collection_of_object_values(access_review_notification_recipient_item.AccessReviewNotificationRecipientItem)),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(user_identity.UserIdentity)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "descriptionForAdmins": lambda n : setattr(self, 'description_for_admins', n.get_str_value()),
            "descriptionForReviewers": lambda n : setattr(self, 'description_for_reviewers', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "fallbackReviewers": lambda n : setattr(self, 'fallback_reviewers', n.get_collection_of_object_values(access_review_reviewer_scope.AccessReviewReviewerScope)),
            "instances": lambda n : setattr(self, 'instances', n.get_collection_of_object_values(access_review_instance.AccessReviewInstance)),
            "instanceEnumerationScope": lambda n : setattr(self, 'instance_enumeration_scope', n.get_object_value(access_review_scope.AccessReviewScope)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "reviewers": lambda n : setattr(self, 'reviewers', n.get_collection_of_object_values(access_review_reviewer_scope.AccessReviewReviewerScope)),
            "scope": lambda n : setattr(self, 'scope', n.get_object_value(access_review_scope.AccessReviewScope)),
            "settings": lambda n : setattr(self, 'settings', n.get_object_value(access_review_schedule_settings.AccessReviewScheduleSettings)),
            "stageSettings": lambda n : setattr(self, 'stage_settings', n.get_collection_of_object_values(access_review_stage_settings.AccessReviewStageSettings)),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("additionalNotificationRecipients", self.additional_notification_recipients)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("descriptionForAdmins", self.description_for_admins)
        writer.write_str_value("descriptionForReviewers", self.description_for_reviewers)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("fallbackReviewers", self.fallback_reviewers)
        writer.write_collection_of_object_values("instances", self.instances)
        writer.write_object_value("instanceEnumerationScope", self.instance_enumeration_scope)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_collection_of_object_values("reviewers", self.reviewers)
        writer.write_object_value("scope", self.scope)
        writer.write_object_value("settings", self.settings)
        writer.write_collection_of_object_values("stageSettings", self.stage_settings)
        writer.write_str_value("status", self.status)
    

