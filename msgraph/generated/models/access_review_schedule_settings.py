from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_review_apply_action import AccessReviewApplyAction
    from .access_review_recommendation_insight_setting import AccessReviewRecommendationInsightSetting
    from .patterned_recurrence import PatternedRecurrence

@dataclass
class AccessReviewScheduleSettings(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Optional field. Describes the  actions to take once a review is complete. There are two types that are currently supported: removeAccessApplyAction (default) and disableAndDeleteUserApplyAction. Field only needs to be specified in the case of disableAndDeleteUserApplyAction.
    apply_actions: Optional[list[AccessReviewApplyAction]] = None
    # Indicates whether decisions are automatically applied. When set to false, an admin must apply the decisions manually once the reviewer completes the access review. When set to true, decisions are applied automatically after the access review instance duration ends, whether or not the reviewers have responded. Default value is false.  CAUTION: If both autoApplyDecisionsEnabled and defaultDecisionEnabled are true, all access for the principals to the resource risks being revoked if the reviewers fail to respond.
    auto_apply_decisions_enabled: Optional[bool] = None
    # Indicates whether decisions on previous access review stages are available for reviewers on an accessReviewInstance with multiple subsequent stages. If not provided, the default is disabled (false).
    decision_histories_for_reviewers_enabled: Optional[bool] = None
    # Decision chosen if defaultDecisionEnabled is enabled. Can be one of Approve, Deny, or Recommendation.
    default_decision: Optional[str] = None
    # Indicates whether the default decision is enabled or disabled when reviewers do not respond. Default value is false.  CAUTION: If both autoApplyDecisionsEnabled and defaultDecisionEnabled are true, all access for the principals to the resource risks being revoked if the reviewers fail to respond.
    default_decision_enabled: Optional[bool] = None
    # Duration of an access review instance in days. NOTE: If the stageSettings of the accessReviewScheduleDefinition object is defined, its durationInDays setting will be used instead of the value of this property.
    instance_duration_in_days: Optional[int] = None
    # Indicates whether reviewers are required to provide justification with their decision. Default value is false.
    justification_required_on_approval: Optional[bool] = None
    # Indicates whether emails are enabled or disabled. Default value is false.
    mail_notifications_enabled: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Optional. Describes the types of insights that aid reviewers to make access review decisions. NOTE: If the stageSettings of the accessReviewScheduleDefinition object is defined, its recommendationInsightSettings setting will be used instead of the value of this property.
    recommendation_insight_settings: Optional[list[AccessReviewRecommendationInsightSetting]] = None
    # Optional field. Indicates the period of inactivity (with respect to the start date of the review instance) that recommendations will be configured from. The recommendation will be to deny if the user is inactive during the look-back duration. For reviews of groups and Microsoft Entra roles, any duration is accepted. For reviews of applications, 30 days is the maximum duration. If not specified, the duration is 30 days. NOTE: If the stageSettings of the accessReviewScheduleDefinition object is defined, its recommendationLookBackDuration setting will be used instead of the value of this property.
    recommendation_look_back_duration: Optional[datetime.timedelta] = None
    # Indicates whether decision recommendations are enabled or disabled. NOTE: If the stageSettings of the accessReviewScheduleDefinition object is defined, its recommendationsEnabled setting will be used instead of the value of this property.
    recommendations_enabled: Optional[bool] = None
    # Detailed settings for recurrence using the standard Outlook recurrence object. Note: Only dayOfMonth, interval, and type (weekly, absoluteMonthly) properties are supported. Use the property startDate on recurrenceRange to determine the day the review starts.
    recurrence: Optional[PatternedRecurrence] = None
    # Indicates whether reminders are enabled or disabled. Default value is false.
    reminder_notifications_enabled: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AccessReviewScheduleSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AccessReviewScheduleSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AccessReviewScheduleSettings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .access_review_apply_action import AccessReviewApplyAction
        from .access_review_recommendation_insight_setting import AccessReviewRecommendationInsightSetting
        from .patterned_recurrence import PatternedRecurrence

        from .access_review_apply_action import AccessReviewApplyAction
        from .access_review_recommendation_insight_setting import AccessReviewRecommendationInsightSetting
        from .patterned_recurrence import PatternedRecurrence

        fields: dict[str, Callable[[Any], None]] = {
            "applyActions": lambda n : setattr(self, 'apply_actions', n.get_collection_of_object_values(AccessReviewApplyAction)),
            "autoApplyDecisionsEnabled": lambda n : setattr(self, 'auto_apply_decisions_enabled', n.get_bool_value()),
            "decisionHistoriesForReviewersEnabled": lambda n : setattr(self, 'decision_histories_for_reviewers_enabled', n.get_bool_value()),
            "defaultDecision": lambda n : setattr(self, 'default_decision', n.get_str_value()),
            "defaultDecisionEnabled": lambda n : setattr(self, 'default_decision_enabled', n.get_bool_value()),
            "instanceDurationInDays": lambda n : setattr(self, 'instance_duration_in_days', n.get_int_value()),
            "justificationRequiredOnApproval": lambda n : setattr(self, 'justification_required_on_approval', n.get_bool_value()),
            "mailNotificationsEnabled": lambda n : setattr(self, 'mail_notifications_enabled', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "recommendationInsightSettings": lambda n : setattr(self, 'recommendation_insight_settings', n.get_collection_of_object_values(AccessReviewRecommendationInsightSetting)),
            "recommendationLookBackDuration": lambda n : setattr(self, 'recommendation_look_back_duration', n.get_timedelta_value()),
            "recommendationsEnabled": lambda n : setattr(self, 'recommendations_enabled', n.get_bool_value()),
            "recurrence": lambda n : setattr(self, 'recurrence', n.get_object_value(PatternedRecurrence)),
            "reminderNotificationsEnabled": lambda n : setattr(self, 'reminder_notifications_enabled', n.get_bool_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_collection_of_object_values("applyActions", self.apply_actions)
        writer.write_bool_value("autoApplyDecisionsEnabled", self.auto_apply_decisions_enabled)
        writer.write_bool_value("decisionHistoriesForReviewersEnabled", self.decision_histories_for_reviewers_enabled)
        writer.write_str_value("defaultDecision", self.default_decision)
        writer.write_bool_value("defaultDecisionEnabled", self.default_decision_enabled)
        writer.write_int_value("instanceDurationInDays", self.instance_duration_in_days)
        writer.write_bool_value("justificationRequiredOnApproval", self.justification_required_on_approval)
        writer.write_bool_value("mailNotificationsEnabled", self.mail_notifications_enabled)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("recommendationInsightSettings", self.recommendation_insight_settings)
        writer.write_timedelta_value("recommendationLookBackDuration", self.recommendation_look_back_duration)
        writer.write_bool_value("recommendationsEnabled", self.recommendations_enabled)
        writer.write_object_value("recurrence", self.recurrence)
        writer.write_bool_value("reminderNotificationsEnabled", self.reminder_notifications_enabled)
        writer.write_additional_data_value(self.additional_data)
    

