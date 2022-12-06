from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

access_review_scope = lazy_import('msgraph.generated.models.access_review_scope')

class PrincipalResourceMembershipsScope(access_review_scope.AccessReviewScope):
    def __init__(self,) -> None:
        """
        Instantiates a new PrincipalResourceMembershipsScope and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.principalResourceMembershipsScope"
        # Defines the scopes of the principals whose access to resources are reviewed in the access review.
        self._principal_scopes: Optional[List[access_review_scope.AccessReviewScope]] = None
        # Defines the scopes of the resources for which access is reviewed.
        self._resource_scopes: Optional[List[access_review_scope.AccessReviewScope]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PrincipalResourceMembershipsScope:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PrincipalResourceMembershipsScope
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PrincipalResourceMembershipsScope()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "principal_scopes": lambda n : setattr(self, 'principal_scopes', n.get_collection_of_object_values(access_review_scope.AccessReviewScope)),
            "resource_scopes": lambda n : setattr(self, 'resource_scopes', n.get_collection_of_object_values(access_review_scope.AccessReviewScope)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def principal_scopes(self,) -> Optional[List[access_review_scope.AccessReviewScope]]:
        """
        Gets the principalScopes property value. Defines the scopes of the principals whose access to resources are reviewed in the access review.
        Returns: Optional[List[access_review_scope.AccessReviewScope]]
        """
        return self._principal_scopes
    
    @principal_scopes.setter
    def principal_scopes(self,value: Optional[List[access_review_scope.AccessReviewScope]] = None) -> None:
        """
        Sets the principalScopes property value. Defines the scopes of the principals whose access to resources are reviewed in the access review.
        Args:
            value: Value to set for the principalScopes property.
        """
        self._principal_scopes = value
    
    @property
    def resource_scopes(self,) -> Optional[List[access_review_scope.AccessReviewScope]]:
        """
        Gets the resourceScopes property value. Defines the scopes of the resources for which access is reviewed.
        Returns: Optional[List[access_review_scope.AccessReviewScope]]
        """
        return self._resource_scopes
    
    @resource_scopes.setter
    def resource_scopes(self,value: Optional[List[access_review_scope.AccessReviewScope]] = None) -> None:
        """
        Sets the resourceScopes property value. Defines the scopes of the resources for which access is reviewed.
        Args:
            value: Value to set for the resourceScopes property.
        """
        self._resource_scopes = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("principalScopes", self.principal_scopes)
        writer.write_collection_of_object_values("resourceScopes", self.resource_scopes)
    

