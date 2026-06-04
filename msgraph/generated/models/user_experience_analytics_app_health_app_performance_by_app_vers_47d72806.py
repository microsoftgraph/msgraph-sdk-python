from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
    from .user_experience_analytics_app_health_app_performance_by_app_vers_ba5b7522 import UserExperienceAnalyticsAppHealthAppPerformanceByAppVers_ba5b7522

from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse

@dataclass
class UserExperienceAnalyticsAppHealthAppPerformanceByAppVers_47d72806(BaseCollectionPaginationCountResponse, Parsable):
    """
    Original name: UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDetailsCollectionResponse
    """
    # The value property
    value: Optional[list[UserExperienceAnalyticsAppHealthAppPerformanceByAppVers_ba5b7522]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserExperienceAnalyticsAppHealthAppPerformanceByAppVers_47d72806:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsAppHealthAppPerformanceByAppVers_47d72806
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UserExperienceAnalyticsAppHealthAppPerformanceByAppVers_47d72806()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
        from .user_experience_analytics_app_health_app_performance_by_app_vers_ba5b7522 import UserExperienceAnalyticsAppHealthAppPerformanceByAppVers_ba5b7522

        from .base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
        from .user_experience_analytics_app_health_app_performance_by_app_vers_ba5b7522 import UserExperienceAnalyticsAppHealthAppPerformanceByAppVers_ba5b7522

        fields: dict[str, Callable[[Any], None]] = {
            "value": lambda n : setattr(self, 'value', n.get_collection_of_object_values(UserExperienceAnalyticsAppHealthAppPerformanceByAppVers_ba5b7522)),
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
        writer.write_collection_of_object_values("value", self.value)
    

