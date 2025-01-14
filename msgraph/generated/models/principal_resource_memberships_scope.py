from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_review_scope import AccessReviewScope

from .access_review_scope import AccessReviewScope

@dataclass
class PrincipalResourceMembershipsScope(AccessReviewScope, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.principalResourceMembershipsScope"
    # Defines the scopes of the principals whose access to resources are reviewed in the access review.
    principal_scopes: Optional[list[AccessReviewScope]] = None
    # Defines the scopes of the resources for which access is reviewed.
    resource_scopes: Optional[list[AccessReviewScope]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PrincipalResourceMembershipsScope:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PrincipalResourceMembershipsScope
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PrincipalResourceMembershipsScope()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .access_review_scope import AccessReviewScope

        from .access_review_scope import AccessReviewScope

        fields: dict[str, Callable[[Any], None]] = {
            "principalScopes": lambda n : setattr(self, 'principal_scopes', n.get_collection_of_object_values(AccessReviewScope)),
            "resourceScopes": lambda n : setattr(self, 'resource_scopes', n.get_collection_of_object_values(AccessReviewScope)),
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
        writer.write_collection_of_object_values("principalScopes", self.principal_scopes)
        writer.write_collection_of_object_values("resourceScopes", self.resource_scopes)
    

