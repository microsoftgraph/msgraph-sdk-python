from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_review_resource_scope import AccessReviewResourceScope

from .access_review_resource_scope import AccessReviewResourceScope

@dataclass
class AccessReviewAccessPackageAssignmentPolicyScope(AccessReviewResourceScope, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.accessReviewAccessPackageAssignmentPolicyScope"
    # The display name of the access package.
    access_package_display_name: Optional[str] = None
    # The access package identifier.
    access_package_id: Optional[str] = None
    # The display name of the catalog.
    catalog_display_name: Optional[str] = None
    # The catalog identifier.
    catalog_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AccessReviewAccessPackageAssignmentPolicyScope:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AccessReviewAccessPackageAssignmentPolicyScope
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AccessReviewAccessPackageAssignmentPolicyScope()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .access_review_resource_scope import AccessReviewResourceScope

        from .access_review_resource_scope import AccessReviewResourceScope

        fields: dict[str, Callable[[Any], None]] = {
            "accessPackageDisplayName": lambda n : setattr(self, 'access_package_display_name', n.get_str_value()),
            "accessPackageId": lambda n : setattr(self, 'access_package_id', n.get_str_value()),
            "catalogDisplayName": lambda n : setattr(self, 'catalog_display_name', n.get_str_value()),
            "catalogId": lambda n : setattr(self, 'catalog_id', n.get_str_value()),
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
        writer.write_str_value("accessPackageDisplayName", self.access_package_display_name)
        writer.write_str_value("accessPackageId", self.access_package_id)
        writer.write_str_value("catalogDisplayName", self.catalog_display_name)
        writer.write_str_value("catalogId", self.catalog_id)
    

