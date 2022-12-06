from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
service_health = lazy_import('msgraph.generated.models.service_health')
service_health_issue = lazy_import('msgraph.generated.models.service_health_issue')
service_update_message = lazy_import('msgraph.generated.models.service_update_message')

class ServiceAnnouncement(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new serviceAnnouncement and sets the default values.
        """
        super().__init__()
        # A collection of service health information for tenant. This property is a contained navigation property, it is nullable and readonly.
        self._health_overviews: Optional[List[service_health.ServiceHealth]] = None
        # A collection of service issues for tenant. This property is a contained navigation property, it is nullable and readonly.
        self._issues: Optional[List[service_health_issue.ServiceHealthIssue]] = None
        # A collection of service messages for tenant. This property is a contained navigation property, it is nullable and readonly.
        self._messages: Optional[List[service_update_message.ServiceUpdateMessage]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ServiceAnnouncement:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ServiceAnnouncement
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ServiceAnnouncement()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "health_overviews": lambda n : setattr(self, 'health_overviews', n.get_collection_of_object_values(service_health.ServiceHealth)),
            "issues": lambda n : setattr(self, 'issues', n.get_collection_of_object_values(service_health_issue.ServiceHealthIssue)),
            "messages": lambda n : setattr(self, 'messages', n.get_collection_of_object_values(service_update_message.ServiceUpdateMessage)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def health_overviews(self,) -> Optional[List[service_health.ServiceHealth]]:
        """
        Gets the healthOverviews property value. A collection of service health information for tenant. This property is a contained navigation property, it is nullable and readonly.
        Returns: Optional[List[service_health.ServiceHealth]]
        """
        return self._health_overviews
    
    @health_overviews.setter
    def health_overviews(self,value: Optional[List[service_health.ServiceHealth]] = None) -> None:
        """
        Sets the healthOverviews property value. A collection of service health information for tenant. This property is a contained navigation property, it is nullable and readonly.
        Args:
            value: Value to set for the healthOverviews property.
        """
        self._health_overviews = value
    
    @property
    def issues(self,) -> Optional[List[service_health_issue.ServiceHealthIssue]]:
        """
        Gets the issues property value. A collection of service issues for tenant. This property is a contained navigation property, it is nullable and readonly.
        Returns: Optional[List[service_health_issue.ServiceHealthIssue]]
        """
        return self._issues
    
    @issues.setter
    def issues(self,value: Optional[List[service_health_issue.ServiceHealthIssue]] = None) -> None:
        """
        Sets the issues property value. A collection of service issues for tenant. This property is a contained navigation property, it is nullable and readonly.
        Args:
            value: Value to set for the issues property.
        """
        self._issues = value
    
    @property
    def messages(self,) -> Optional[List[service_update_message.ServiceUpdateMessage]]:
        """
        Gets the messages property value. A collection of service messages for tenant. This property is a contained navigation property, it is nullable and readonly.
        Returns: Optional[List[service_update_message.ServiceUpdateMessage]]
        """
        return self._messages
    
    @messages.setter
    def messages(self,value: Optional[List[service_update_message.ServiceUpdateMessage]] = None) -> None:
        """
        Sets the messages property value. A collection of service messages for tenant. This property is a contained navigation property, it is nullable and readonly.
        Args:
            value: Value to set for the messages property.
        """
        self._messages = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("healthOverviews", self.health_overviews)
        writer.write_collection_of_object_values("issues", self.issues)
        writer.write_collection_of_object_values("messages", self.messages)
    

