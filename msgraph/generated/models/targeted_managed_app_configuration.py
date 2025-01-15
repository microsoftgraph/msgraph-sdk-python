from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .managed_app_configuration import ManagedAppConfiguration
    from .managed_app_policy_deployment_summary import ManagedAppPolicyDeploymentSummary
    from .managed_mobile_app import ManagedMobileApp
    from .targeted_managed_app_policy_assignment import TargetedManagedAppPolicyAssignment

from .managed_app_configuration import ManagedAppConfiguration

@dataclass
class TargetedManagedAppConfiguration(ManagedAppConfiguration, Parsable):
    """
    Configuration used to deliver a set of custom settings as-is to all users in the targeted security group
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.targetedManagedAppConfiguration"
    # List of apps to which the policy is deployed.
    apps: Optional[list[ManagedMobileApp]] = None
    # Navigation property to list of inclusion and exclusion groups to which the policy is deployed.
    assignments: Optional[list[TargetedManagedAppPolicyAssignment]] = None
    # Count of apps to which the current policy is deployed.
    deployed_app_count: Optional[int] = None
    # Navigation property to deployment summary of the configuration.
    deployment_summary: Optional[ManagedAppPolicyDeploymentSummary] = None
    # Indicates if the policy is deployed to any inclusion groups or not.
    is_assigned: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TargetedManagedAppConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TargetedManagedAppConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TargetedManagedAppConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .managed_app_configuration import ManagedAppConfiguration
        from .managed_app_policy_deployment_summary import ManagedAppPolicyDeploymentSummary
        from .managed_mobile_app import ManagedMobileApp
        from .targeted_managed_app_policy_assignment import TargetedManagedAppPolicyAssignment

        from .managed_app_configuration import ManagedAppConfiguration
        from .managed_app_policy_deployment_summary import ManagedAppPolicyDeploymentSummary
        from .managed_mobile_app import ManagedMobileApp
        from .targeted_managed_app_policy_assignment import TargetedManagedAppPolicyAssignment

        fields: dict[str, Callable[[Any], None]] = {
            "apps": lambda n : setattr(self, 'apps', n.get_collection_of_object_values(ManagedMobileApp)),
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(TargetedManagedAppPolicyAssignment)),
            "deployedAppCount": lambda n : setattr(self, 'deployed_app_count', n.get_int_value()),
            "deploymentSummary": lambda n : setattr(self, 'deployment_summary', n.get_object_value(ManagedAppPolicyDeploymentSummary)),
            "isAssigned": lambda n : setattr(self, 'is_assigned', n.get_bool_value()),
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
        writer.write_collection_of_object_values("apps", self.apps)
        writer.write_collection_of_object_values("assignments", self.assignments)
        writer.write_int_value("deployedAppCount", self.deployed_app_count)
        writer.write_object_value("deploymentSummary", self.deployment_summary)
        writer.write_bool_value("isAssigned", self.is_assigned)
    

