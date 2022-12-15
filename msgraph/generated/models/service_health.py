from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
service_health_issue = lazy_import('msgraph.generated.models.service_health_issue')
service_health_status = lazy_import('msgraph.generated.models.service_health_status')

class ServiceHealth(entity.Entity):
    """
    Provides operations to manage the admin singleton.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new serviceHealth and sets the default values.
        """
        super().__init__()
        # A collection of issues that happened on the service, with detailed information for each issue.
        self._issues: Optional[List[service_health_issue.ServiceHealthIssue]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The service name. Use the list healthOverviews operation to get exact string names for services subscribed by the tenant.
        self._service: Optional[str] = None
        # The status property
        self._status: Optional[service_health_status.ServiceHealthStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ServiceHealth:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ServiceHealth
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ServiceHealth()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "issues": lambda n : setattr(self, 'issues', n.get_collection_of_object_values(service_health_issue.ServiceHealthIssue)),
            "service": lambda n : setattr(self, 'service', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(service_health_status.ServiceHealthStatus)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def issues(self,) -> Optional[List[service_health_issue.ServiceHealthIssue]]:
        """
        Gets the issues property value. A collection of issues that happened on the service, with detailed information for each issue.
        Returns: Optional[List[service_health_issue.ServiceHealthIssue]]
        """
        return self._issues
    
    @issues.setter
    def issues(self,value: Optional[List[service_health_issue.ServiceHealthIssue]] = None) -> None:
        """
        Sets the issues property value. A collection of issues that happened on the service, with detailed information for each issue.
        Args:
            value: Value to set for the issues property.
        """
        self._issues = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("issues", self.issues)
        writer.write_str_value("service", self.service)
        writer.write_enum_value("status", self.status)
    
    @property
    def service(self,) -> Optional[str]:
        """
        Gets the service property value. The service name. Use the list healthOverviews operation to get exact string names for services subscribed by the tenant.
        Returns: Optional[str]
        """
        return self._service
    
    @service.setter
    def service(self,value: Optional[str] = None) -> None:
        """
        Sets the service property value. The service name. Use the list healthOverviews operation to get exact string names for services subscribed by the tenant.
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
    

