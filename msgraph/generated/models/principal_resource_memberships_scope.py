from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import access_review_scope

from . import access_review_scope

@dataclass
class PrincipalResourceMembershipsScope(access_review_scope.AccessReviewScope):
    odata_type = "#microsoft.graph.principalResourceMembershipsScope"
    # Defines the scopes of the principals whose access to resources are reviewed in the access review.
    principal_scopes: Optional[List[access_review_scope.AccessReviewScope]] = None
    # Defines the scopes of the resources for which access is reviewed.
    resource_scopes: Optional[List[access_review_scope.AccessReviewScope]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PrincipalResourceMembershipsScope:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PrincipalResourceMembershipsScope
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return PrincipalResourceMembershipsScope()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import access_review_scope

        from . import access_review_scope

        fields: Dict[str, Callable[[Any], None]] = {
            "principalScopes": lambda n : setattr(self, 'principal_scopes', n.get_collection_of_object_values(access_review_scope.AccessReviewScope)),
            "resourceScopes": lambda n : setattr(self, 'resource_scopes', n.get_collection_of_object_values(access_review_scope.AccessReviewScope)),
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
        writer.write_collection_of_object_values("principalScopes", self.principal_scopes)
        writer.write_collection_of_object_values("resourceScopes", self.resource_scopes)
    

