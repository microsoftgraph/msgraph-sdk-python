from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

service_announcement_base = lazy_import('msgraph.generated.models.service_announcement_base')
service_health_classification_type = lazy_import('msgraph.generated.models.service_health_classification_type')
service_health_issue_post = lazy_import('msgraph.generated.models.service_health_issue_post')
service_health_origin = lazy_import('msgraph.generated.models.service_health_origin')
service_health_status = lazy_import('msgraph.generated.models.service_health_status')

class ServiceHealthIssue(service_announcement_base.ServiceAnnouncementBase):
    @property
    def classification(self,) -> Optional[service_health_classification_type.ServiceHealthClassificationType]:
        """
        Gets the classification property value. The classification property
        Returns: Optional[service_health_classification_type.ServiceHealthClassificationType]
        """
        return self._classification
    
    @classification.setter
    def classification(self,value: Optional[service_health_classification_type.ServiceHealthClassificationType] = None) -> None:
        """
        Sets the classification property value. The classification property
        Args:
            value: Value to set for the classification property.
        """
        self._classification = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new ServiceHealthIssue and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.serviceHealthIssue"
        # The classification property
        self._classification: Optional[service_health_classification_type.ServiceHealthClassificationType] = None
        # The feature name of the service issue.
        self._feature: Optional[str] = None
        # The feature group name of the service issue.
        self._feature_group: Optional[str] = None
        # The description of the service issue impact.
        self._impact_description: Optional[str] = None
        # Indicates whether the issue is resolved.
        self._is_resolved: Optional[bool] = None
        # The origin property
        self._origin: Optional[service_health_origin.ServiceHealthOrigin] = None
        # Collection of historical posts for the service issue.
        self._posts: Optional[List[service_health_issue_post.ServiceHealthIssuePost]] = None
        # Indicates the service affected by the issue.
        self._service: Optional[str] = None
        # The status property
        self._status: Optional[service_health_status.ServiceHealthStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ServiceHealthIssue:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ServiceHealthIssue
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ServiceHealthIssue()
    
    @property
    def feature(self,) -> Optional[str]:
        """
        Gets the feature property value. The feature name of the service issue.
        Returns: Optional[str]
        """
        return self._feature
    
    @feature.setter
    def feature(self,value: Optional[str] = None) -> None:
        """
        Sets the feature property value. The feature name of the service issue.
        Args:
            value: Value to set for the feature property.
        """
        self._feature = value
    
    @property
    def feature_group(self,) -> Optional[str]:
        """
        Gets the featureGroup property value. The feature group name of the service issue.
        Returns: Optional[str]
        """
        return self._feature_group
    
    @feature_group.setter
    def feature_group(self,value: Optional[str] = None) -> None:
        """
        Sets the featureGroup property value. The feature group name of the service issue.
        Args:
            value: Value to set for the featureGroup property.
        """
        self._feature_group = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "classification": lambda n : setattr(self, 'classification', n.get_enum_value(service_health_classification_type.ServiceHealthClassificationType)),
            "feature": lambda n : setattr(self, 'feature', n.get_str_value()),
            "feature_group": lambda n : setattr(self, 'feature_group', n.get_str_value()),
            "impact_description": lambda n : setattr(self, 'impact_description', n.get_str_value()),
            "is_resolved": lambda n : setattr(self, 'is_resolved', n.get_bool_value()),
            "origin": lambda n : setattr(self, 'origin', n.get_enum_value(service_health_origin.ServiceHealthOrigin)),
            "posts": lambda n : setattr(self, 'posts', n.get_collection_of_object_values(service_health_issue_post.ServiceHealthIssuePost)),
            "service": lambda n : setattr(self, 'service', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(service_health_status.ServiceHealthStatus)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def impact_description(self,) -> Optional[str]:
        """
        Gets the impactDescription property value. The description of the service issue impact.
        Returns: Optional[str]
        """
        return self._impact_description
    
    @impact_description.setter
    def impact_description(self,value: Optional[str] = None) -> None:
        """
        Sets the impactDescription property value. The description of the service issue impact.
        Args:
            value: Value to set for the impactDescription property.
        """
        self._impact_description = value
    
    @property
    def is_resolved(self,) -> Optional[bool]:
        """
        Gets the isResolved property value. Indicates whether the issue is resolved.
        Returns: Optional[bool]
        """
        return self._is_resolved
    
    @is_resolved.setter
    def is_resolved(self,value: Optional[bool] = None) -> None:
        """
        Sets the isResolved property value. Indicates whether the issue is resolved.
        Args:
            value: Value to set for the isResolved property.
        """
        self._is_resolved = value
    
    @property
    def origin(self,) -> Optional[service_health_origin.ServiceHealthOrigin]:
        """
        Gets the origin property value. The origin property
        Returns: Optional[service_health_origin.ServiceHealthOrigin]
        """
        return self._origin
    
    @origin.setter
    def origin(self,value: Optional[service_health_origin.ServiceHealthOrigin] = None) -> None:
        """
        Sets the origin property value. The origin property
        Args:
            value: Value to set for the origin property.
        """
        self._origin = value
    
    @property
    def posts(self,) -> Optional[List[service_health_issue_post.ServiceHealthIssuePost]]:
        """
        Gets the posts property value. Collection of historical posts for the service issue.
        Returns: Optional[List[service_health_issue_post.ServiceHealthIssuePost]]
        """
        return self._posts
    
    @posts.setter
    def posts(self,value: Optional[List[service_health_issue_post.ServiceHealthIssuePost]] = None) -> None:
        """
        Sets the posts property value. Collection of historical posts for the service issue.
        Args:
            value: Value to set for the posts property.
        """
        self._posts = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
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
    
    @property
    def service(self,) -> Optional[str]:
        """
        Gets the service property value. Indicates the service affected by the issue.
        Returns: Optional[str]
        """
        return self._service
    
    @service.setter
    def service(self,value: Optional[str] = None) -> None:
        """
        Sets the service property value. Indicates the service affected by the issue.
        Args:
            value: Value to set for the service property.
        """
        self._service = value
    
    @property
    def status(self,) -> Optional[service_health_status.ServiceHealthStatus]:
        """
        Gets the status property value. The status property
        Returns: Optional[service_health_status.ServiceHealthStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[service_health_status.ServiceHealthStatus] = None) -> None:
        """
        Sets the status property value. The status property
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    

