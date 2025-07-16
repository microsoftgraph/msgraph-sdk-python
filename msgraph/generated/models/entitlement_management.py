from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_package import AccessPackage
    from .access_package_assignment import AccessPackageAssignment
    from .access_package_assignment_policy import AccessPackageAssignmentPolicy
    from .access_package_assignment_request import AccessPackageAssignmentRequest
    from .access_package_catalog import AccessPackageCatalog
    from .access_package_resource import AccessPackageResource
    from .access_package_resource_environment import AccessPackageResourceEnvironment
    from .access_package_resource_request import AccessPackageResourceRequest
    from .access_package_resource_role_scope import AccessPackageResourceRoleScope
    from .approval import Approval
    from .connected_organization import ConnectedOrganization
    from .entitlement_management_settings import EntitlementManagementSettings
    from .entity import Entity

from .entity import Entity

@dataclass
class EntitlementManagement(Entity, Parsable):
    # Approval stages for decisions associated with access package assignment requests.
    access_package_assignment_approvals: Optional[list[Approval]] = None
    # Access packages define the collection of resource roles and the policies for which subjects can request or be assigned access to those resources.
    access_packages: Optional[list[AccessPackage]] = None
    # Access package assignment policies govern which subjects can request or be assigned an access package via an access package assignment.
    assignment_policies: Optional[list[AccessPackageAssignmentPolicy]] = None
    # Access package assignment requests created by or on behalf of a subject.
    assignment_requests: Optional[list[AccessPackageAssignmentRequest]] = None
    # The assignment of an access package to a subject for a period of time.
    assignments: Optional[list[AccessPackageAssignment]] = None
    # A container for access packages.
    catalogs: Optional[list[AccessPackageCatalog]] = None
    # References to a directory or domain of another organization whose users can request access.
    connected_organizations: Optional[list[ConnectedOrganization]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # A reference to the geolocation environments in which a resource is located.
    resource_environments: Optional[list[AccessPackageResourceEnvironment]] = None
    # Represents a request to add or remove a resource to or from a catalog respectively.
    resource_requests: Optional[list[AccessPackageResourceRequest]] = None
    # The resourceRoleScopes property
    resource_role_scopes: Optional[list[AccessPackageResourceRoleScope]] = None
    # The resources associated with the catalogs.
    resources: Optional[list[AccessPackageResource]] = None
    # The settings that control the behavior of Microsoft Entra entitlement management.
    settings: Optional[EntitlementManagementSettings] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EntitlementManagement:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EntitlementManagement
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EntitlementManagement()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .access_package import AccessPackage
        from .access_package_assignment import AccessPackageAssignment
        from .access_package_assignment_policy import AccessPackageAssignmentPolicy
        from .access_package_assignment_request import AccessPackageAssignmentRequest
        from .access_package_catalog import AccessPackageCatalog
        from .access_package_resource import AccessPackageResource
        from .access_package_resource_environment import AccessPackageResourceEnvironment
        from .access_package_resource_request import AccessPackageResourceRequest
        from .access_package_resource_role_scope import AccessPackageResourceRoleScope
        from .approval import Approval
        from .connected_organization import ConnectedOrganization
        from .entitlement_management_settings import EntitlementManagementSettings
        from .entity import Entity

        from .access_package import AccessPackage
        from .access_package_assignment import AccessPackageAssignment
        from .access_package_assignment_policy import AccessPackageAssignmentPolicy
        from .access_package_assignment_request import AccessPackageAssignmentRequest
        from .access_package_catalog import AccessPackageCatalog
        from .access_package_resource import AccessPackageResource
        from .access_package_resource_environment import AccessPackageResourceEnvironment
        from .access_package_resource_request import AccessPackageResourceRequest
        from .access_package_resource_role_scope import AccessPackageResourceRoleScope
        from .approval import Approval
        from .connected_organization import ConnectedOrganization
        from .entitlement_management_settings import EntitlementManagementSettings
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "accessPackageAssignmentApprovals": lambda n : setattr(self, 'access_package_assignment_approvals', n.get_collection_of_object_values(Approval)),
            "accessPackages": lambda n : setattr(self, 'access_packages', n.get_collection_of_object_values(AccessPackage)),
            "assignmentPolicies": lambda n : setattr(self, 'assignment_policies', n.get_collection_of_object_values(AccessPackageAssignmentPolicy)),
            "assignmentRequests": lambda n : setattr(self, 'assignment_requests', n.get_collection_of_object_values(AccessPackageAssignmentRequest)),
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(AccessPackageAssignment)),
            "catalogs": lambda n : setattr(self, 'catalogs', n.get_collection_of_object_values(AccessPackageCatalog)),
            "connectedOrganizations": lambda n : setattr(self, 'connected_organizations', n.get_collection_of_object_values(ConnectedOrganization)),
            "resourceEnvironments": lambda n : setattr(self, 'resource_environments', n.get_collection_of_object_values(AccessPackageResourceEnvironment)),
            "resourceRequests": lambda n : setattr(self, 'resource_requests', n.get_collection_of_object_values(AccessPackageResourceRequest)),
            "resourceRoleScopes": lambda n : setattr(self, 'resource_role_scopes', n.get_collection_of_object_values(AccessPackageResourceRoleScope)),
            "resources": lambda n : setattr(self, 'resources', n.get_collection_of_object_values(AccessPackageResource)),
            "settings": lambda n : setattr(self, 'settings', n.get_object_value(EntitlementManagementSettings)),
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
        writer.write_collection_of_object_values("accessPackageAssignmentApprovals", self.access_package_assignment_approvals)
        writer.write_collection_of_object_values("accessPackages", self.access_packages)
        writer.write_collection_of_object_values("assignmentPolicies", self.assignment_policies)
        writer.write_collection_of_object_values("assignmentRequests", self.assignment_requests)
        writer.write_collection_of_object_values("assignments", self.assignments)
        writer.write_collection_of_object_values("catalogs", self.catalogs)
        writer.write_collection_of_object_values("connectedOrganizations", self.connected_organizations)
        writer.write_collection_of_object_values("resourceEnvironments", self.resource_environments)
        writer.write_collection_of_object_values("resourceRequests", self.resource_requests)
        writer.write_collection_of_object_values("resourceRoleScopes", self.resource_role_scopes)
        writer.write_collection_of_object_values("resources", self.resources)
        writer.write_object_value("settings", self.settings)
    

