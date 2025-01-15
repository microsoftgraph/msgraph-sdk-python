from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_review_recommendation_insight_setting import AccessReviewRecommendationInsightSetting
    from .user_sign_in_recommendation_scope import UserSignInRecommendationScope

from .access_review_recommendation_insight_setting import AccessReviewRecommendationInsightSetting

@dataclass
class UserLastSignInRecommendationInsightSetting(AccessReviewRecommendationInsightSetting, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.userLastSignInRecommendationInsightSetting"
    # Optional. Indicates the time period of inactivity (with respect to the start date of the review instance) that recommendations will be configured from. The recommendation will be to deny if the user is inactive during the look-back duration. For reviews of groups and Microsoft Entra roles, any duration is accepted. For reviews of applications, 30 days is the maximum duration. If not specified, the duration is 30 days.
    recommendation_look_back_duration: Optional[datetime.timedelta] = None
    # Indicates whether inactivity is calculated based on the user's inactivity in the tenant or in the application. The possible values are tenant, application, unknownFutureValue. application is only relevant when the access review is a review of an assignment to an application.
    sign_in_scope: Optional[UserSignInRecommendationScope] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserLastSignInRecommendationInsightSetting:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserLastSignInRecommendationInsightSetting
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UserLastSignInRecommendationInsightSetting()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .access_review_recommendation_insight_setting import AccessReviewRecommendationInsightSetting
        from .user_sign_in_recommendation_scope import UserSignInRecommendationScope

        from .access_review_recommendation_insight_setting import AccessReviewRecommendationInsightSetting
        from .user_sign_in_recommendation_scope import UserSignInRecommendationScope

        fields: dict[str, Callable[[Any], None]] = {
            "recommendationLookBackDuration": lambda n : setattr(self, 'recommendation_look_back_duration', n.get_timedelta_value()),
            "signInScope": lambda n : setattr(self, 'sign_in_scope', n.get_enum_value(UserSignInRecommendationScope)),
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
        writer.write_timedelta_value("recommendationLookBackDuration", self.recommendation_look_back_duration)
        writer.write_enum_value("signInScope", self.sign_in_scope)
    

