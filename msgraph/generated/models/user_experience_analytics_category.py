from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .user_experience_analytics_insight import UserExperienceAnalyticsInsight
    from .user_experience_analytics_metric import UserExperienceAnalyticsMetric

from .entity import Entity

@dataclass
class UserExperienceAnalyticsCategory(Entity, Parsable):
    """
    The user experience analytics category entity contains the scores and insights for the various metrics of a category.
    """
    # The insights for the category. Read-only.
    insights: Optional[list[UserExperienceAnalyticsInsight]] = None
    # The metric values for the user experience analytics category. Read-only.
    metric_values: Optional[list[UserExperienceAnalyticsMetric]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserExperienceAnalyticsCategory:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsCategory
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UserExperienceAnalyticsCategory()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .user_experience_analytics_insight import UserExperienceAnalyticsInsight
        from .user_experience_analytics_metric import UserExperienceAnalyticsMetric

        from .entity import Entity
        from .user_experience_analytics_insight import UserExperienceAnalyticsInsight
        from .user_experience_analytics_metric import UserExperienceAnalyticsMetric

        fields: dict[str, Callable[[Any], None]] = {
            "insights": lambda n : setattr(self, 'insights', n.get_collection_of_object_values(UserExperienceAnalyticsInsight)),
            "metricValues": lambda n : setattr(self, 'metric_values', n.get_collection_of_object_values(UserExperienceAnalyticsMetric)),
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
        writer.write_collection_of_object_values("insights", self.insights)
        writer.write_collection_of_object_values("metricValues", self.metric_values)
    

