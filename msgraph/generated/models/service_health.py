from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .service_health_issue import ServiceHealthIssue
    from .service_health_status import ServiceHealthStatus

from .entity import Entity

@dataclass
class ServiceHealth(Entity):
    # A collection of issues that happened on the service, with detailed information for each issue.
    issues: Optional[List[ServiceHealthIssue]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The service name. Use the list healthOverviews operation to get exact string names for services subscribed by the tenant.
    service: Optional[str] = None
    # The status property
    status: Optional[ServiceHealthStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ServiceHealth:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ServiceHealth
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ServiceHealth()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .service_health_issue import ServiceHealthIssue
        from .service_health_status import ServiceHealthStatus

        from .entity import Entity
        from .service_health_issue import ServiceHealthIssue
        from .service_health_status import ServiceHealthStatus

        fields: Dict[str, Callable[[Any], None]] = {
            "issues": lambda n : setattr(self, 'issues', n.get_collection_of_object_values(ServiceHealthIssue)),
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
        writer.write_collection_of_object_values("issues", self.issues)
        writer.write_str_value("service", self.service)
        writer.write_enum_value("status", self.status)
    

