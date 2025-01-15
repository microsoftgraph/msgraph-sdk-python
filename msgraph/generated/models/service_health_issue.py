from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .service_announcement_base import ServiceAnnouncementBase
    from .service_health_classification_type import ServiceHealthClassificationType
    from .service_health_issue_post import ServiceHealthIssuePost
    from .service_health_origin import ServiceHealthOrigin
    from .service_health_status import ServiceHealthStatus

from .service_announcement_base import ServiceAnnouncementBase

@dataclass
class ServiceHealthIssue(ServiceAnnouncementBase, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.serviceHealthIssue"
    # The classification property
    classification: Optional[ServiceHealthClassificationType] = None
    # The feature name of the service issue.
    feature: Optional[str] = None
    # The feature group name of the service issue.
    feature_group: Optional[str] = None
    # The description of the service issue impact.
    impact_description: Optional[str] = None
    # Indicates whether the issue is resolved.
    is_resolved: Optional[bool] = None
    # The origin property
    origin: Optional[ServiceHealthOrigin] = None
    # Collection of historical posts for the service issue.
    posts: Optional[list[ServiceHealthIssuePost]] = None
    # Indicates the service affected by the issue.
    service: Optional[str] = None
    # The status property
    status: Optional[ServiceHealthStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ServiceHealthIssue:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ServiceHealthIssue
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ServiceHealthIssue()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .service_announcement_base import ServiceAnnouncementBase
        from .service_health_classification_type import ServiceHealthClassificationType
        from .service_health_issue_post import ServiceHealthIssuePost
        from .service_health_origin import ServiceHealthOrigin
        from .service_health_status import ServiceHealthStatus

        from .service_announcement_base import ServiceAnnouncementBase
        from .service_health_classification_type import ServiceHealthClassificationType
        from .service_health_issue_post import ServiceHealthIssuePost
        from .service_health_origin import ServiceHealthOrigin
        from .service_health_status import ServiceHealthStatus

        fields: dict[str, Callable[[Any], None]] = {
            "classification": lambda n : setattr(self, 'classification', n.get_enum_value(ServiceHealthClassificationType)),
            "feature": lambda n : setattr(self, 'feature', n.get_str_value()),
            "featureGroup": lambda n : setattr(self, 'feature_group', n.get_str_value()),
            "impactDescription": lambda n : setattr(self, 'impact_description', n.get_str_value()),
            "isResolved": lambda n : setattr(self, 'is_resolved', n.get_bool_value()),
            "origin": lambda n : setattr(self, 'origin', n.get_enum_value(ServiceHealthOrigin)),
            "posts": lambda n : setattr(self, 'posts', n.get_collection_of_object_values(ServiceHealthIssuePost)),
            "service": lambda n : setattr(self, 'service', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(ServiceHealthStatus)),
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
        writer.write_enum_value("classification", self.classification)
        writer.write_str_value("feature", self.feature)
        writer.write_str_value("featureGroup", self.feature_group)
        writer.write_str_value("impactDescription", self.impact_description)
        writer.write_bool_value("isResolved", self.is_resolved)
        writer.write_enum_value("origin", self.origin)
        writer.write_collection_of_object_values("posts", self.posts)
        writer.write_str_value("service", self.service)
        writer.write_enum_value("status", self.status)
    

