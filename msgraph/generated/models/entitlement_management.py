from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_package import AccessPackage
    from .access_package_assignment import AccessPackageAssignment
    from .access_package_assignment_policy import AccessPackageAssignmentPolicy
    from .access_package_assignment_request import AccessPackageAssignmentRequest
    from .access_package_catalog import AccessPackageCatalog
    from .approval import Approval
    from .connected_organization import ConnectedOrganization
    from .entitlement_management_settings import EntitlementManagementSettings
    from .entity import Entity

from .entity import Entity

@dataclass
class EntitlementManagement(Entity):
    # Approval stages for decisions associated with access package assignment requests.
    access_package_assignment_approvals: Optional[List[Approval]] = None
    # Access packages define the collection of resource roles and the policies for which subjects can request or be assigned access to those resources.
    access_packages: Optional[List[AccessPackage]] = None
    # Access package assignment policies govern which subjects can request or be assigned an access package via an access package assignment.
    assignment_policies: Optional[List[AccessPackageAssignmentPolicy]] = None
    # Access package assignment requests created by or on behalf of a subject.
    assignment_requests: Optional[List[AccessPackageAssignmentRequest]] = None
    # The assignment of an access package to a subject for a period of time.
    assignments: Optional[List[AccessPackageAssignment]] = None
    # A container for access packages.
    catalogs: Optional[List[AccessPackageCatalog]] = None
    # References to a directory or domain of another organization whose users can request access.
    connected_organizations: Optional[List[ConnectedOrganization]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The settings that control the behavior of Azure AD entitlement management.
    settings: Optional[EntitlementManagementSettings] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EntitlementManagement:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EntitlementManagement
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return EntitlementManagement()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .access_package import AccessPackage
        from .access_package_assignment import AccessPackageAssignment
        from .access_package_assignment_policy import AccessPackageAssignmentPolicy
        from .access_package_assignment_request import AccessPackageAssignmentRequest
        from .access_package_catalog import AccessPackageCatalog
        from .approval import Approval
        from .connected_organization import ConnectedOrganization
        from .entitlement_management_settings import EntitlementManagementSettings
        from .entity import Entity

        from .access_package import AccessPackage
        from .access_package_assignment import AccessPackageAssignment
        from .access_package_assignment_policy import AccessPackageAssignmentPolicy
        from .access_package_assignment_request import AccessPackageAssignmentRequest
        from .access_package_catalog import AccessPackageCatalog
        from .approval import Approval
        from .connected_organization import ConnectedOrganization
        from .entitlement_management_settings import EntitlementManagementSettings
        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "accessPackageAssignmentApprovals": lambda n : setattr(self, 'access_package_assignment_approvals', n.get_collection_of_object_values(Approval)),
            "accessPackages": lambda n : setattr(self, 'access_packages', n.get_collection_of_object_values(AccessPackage)),
            "assignmentPolicies": lambda n : setattr(self, 'assignment_policies', n.get_collection_of_object_values(AccessPackageAssignmentPolicy)),
            "assignmentRequests": lambda n : setattr(self, 'assignment_requests', n.get_collection_of_object_values(AccessPackageAssignmentRequest)),
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(AccessPackageAssignment)),
            "catalogs": lambda n : setattr(self, 'catalogs', n.get_collection_of_object_values(AccessPackageCatalog)),
            "connectedOrganizations": lambda n : setattr(self, 'connected_organizations', n.get_collection_of_object_values(ConnectedOrganization)),
            "settings": lambda n : setattr(self, 'settings', n.get_object_value(EntitlementManagementSettings)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("accessPackageAssignmentApprovals", self.access_package_assignment_approvals)
        writer.write_collection_of_object_values("accessPackages", self.access_packages)
        writer.write_collection_of_object_values("assignmentPolicies", self.assignment_policies)
        writer.write_collection_of_object_values("assignmentRequests", self.assignment_requests)
        writer.write_collection_of_object_values("assignments", self.assignments)
        writer.write_collection_of_object_values("catalogs", self.catalogs)
        writer.write_collection_of_object_values("connectedOrganizations", self.connected_organizations)
        writer.write_object_value("settings", self.settings)
    

