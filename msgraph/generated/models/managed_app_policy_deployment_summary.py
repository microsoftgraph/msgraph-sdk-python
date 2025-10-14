from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .managed_app_policy_deployment_summary_per_app import ManagedAppPolicyDeploymentSummaryPerApp

from .entity import Entity

@dataclass
class ManagedAppPolicyDeploymentSummary(Entity, Parsable):
    """
    The ManagedAppEntity is the base entity type for all other entity types under app management workflow.
    """
    # The configurationDeployedUserCount property
    configuration_deployed_user_count: Optional[int] = None
    # The configurationDeploymentSummaryPerApp property
    configuration_deployment_summary_per_app: Optional[list[ManagedAppPolicyDeploymentSummaryPerApp]] = None
    # The displayName property
    display_name: Optional[str] = None
    # The lastRefreshTime property
    last_refresh_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Version of the entity.
    version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ManagedAppPolicyDeploymentSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ManagedAppPolicyDeploymentSummary
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ManagedAppPolicyDeploymentSummary()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .managed_app_policy_deployment_summary_per_app import ManagedAppPolicyDeploymentSummaryPerApp

        from .entity import Entity
        from .managed_app_policy_deployment_summary_per_app import ManagedAppPolicyDeploymentSummaryPerApp

        fields: dict[str, Callable[[Any], None]] = {
            "configurationDeployedUserCount": lambda n : setattr(self, 'configuration_deployed_user_count', n.get_int_value()),
            "configurationDeploymentSummaryPerApp": lambda n : setattr(self, 'configuration_deployment_summary_per_app', n.get_collection_of_object_values(ManagedAppPolicyDeploymentSummaryPerApp)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastRefreshTime": lambda n : setattr(self, 'last_refresh_time', n.get_datetime_value()),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
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
        writer.write_int_value("configurationDeployedUserCount", self.configuration_deployed_user_count)
        writer.write_collection_of_object_values("configurationDeploymentSummaryPerApp", self.configuration_deployment_summary_per_app)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("lastRefreshTime", self.last_refresh_time)
        writer.write_str_value("version", self.version)
    

