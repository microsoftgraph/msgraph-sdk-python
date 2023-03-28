from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

access_review_instance_decision_item_resource = lazy_import('msgraph.generated.models.access_review_instance_decision_item_resource')

class AccessReviewInstanceDecisionItemAzureRoleResource(access_review_instance_decision_item_resource.AccessReviewInstanceDecisionItemResource):
    def __init__(self,) -> None:
        """
        Instantiates a new AccessReviewInstanceDecisionItemAzureRoleResource and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.accessReviewInstanceDecisionItemAzureRoleResource"
        # Details of the scope this role is associated with.
        self._scope: Optional[access_review_instance_decision_item_resource.AccessReviewInstanceDecisionItemResource] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessReviewInstanceDecisionItemAzureRoleResource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessReviewInstanceDecisionItemAzureRoleResource
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AccessReviewInstanceDecisionItemAzureRoleResource()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "scope": lambda n : setattr(self, 'scope', n.get_object_value(access_review_instance_decision_item_resource.AccessReviewInstanceDecisionItemResource)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def scope(self,) -> Optional[access_review_instance_decision_item_resource.AccessReviewInstanceDecisionItemResource]:
        """
        Gets the scope property value. Details of the scope this role is associated with.
        Returns: Optional[access_review_instance_decision_item_resource.AccessReviewInstanceDecisionItemResource]
        """
        return self._scope
    
    @scope.setter
    def scope(self,value: Optional[access_review_instance_decision_item_resource.AccessReviewInstanceDecisionItemResource] = None) -> None:
        """
        Sets the scope property value. Details of the scope this role is associated with.
        Args:
            value: Value to set for the scope property.
        """
        self._scope = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("scope", self.scope)
    

