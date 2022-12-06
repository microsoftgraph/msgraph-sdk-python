from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

access_review_instance_decision_item_resource = lazy_import('msgraph.generated.models.access_review_instance_decision_item_resource')

class AccessReviewInstanceDecisionItemAccessPackageAssignmentPolicyResource(access_review_instance_decision_item_resource.AccessReviewInstanceDecisionItemResource):
    @property
    def access_package_display_name(self,) -> Optional[str]:
        """
        Gets the accessPackageDisplayName property value. Display name of the access package to which access has been granted.
        Returns: Optional[str]
        """
        return self._access_package_display_name
    
    @access_package_display_name.setter
    def access_package_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the accessPackageDisplayName property value. Display name of the access package to which access has been granted.
        Args:
            value: Value to set for the accessPackageDisplayName property.
        """
        self._access_package_display_name = value
    
    @property
    def access_package_id(self,) -> Optional[str]:
        """
        Gets the accessPackageId property value. Identifier of the access package to which access has been granted.
        Returns: Optional[str]
        """
        return self._access_package_id
    
    @access_package_id.setter
    def access_package_id(self,value: Optional[str] = None) -> None:
        """
        Sets the accessPackageId property value. Identifier of the access package to which access has been granted.
        Args:
            value: Value to set for the accessPackageId property.
        """
        self._access_package_id = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new AccessReviewInstanceDecisionItemAccessPackageAssignmentPolicyResource and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.accessReviewInstanceDecisionItemAccessPackageAssignmentPolicyResource"
        # Display name of the access package to which access has been granted.
        self._access_package_display_name: Optional[str] = None
        # Identifier of the access package to which access has been granted.
        self._access_package_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessReviewInstanceDecisionItemAccessPackageAssignmentPolicyResource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessReviewInstanceDecisionItemAccessPackageAssignmentPolicyResource
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AccessReviewInstanceDecisionItemAccessPackageAssignmentPolicyResource()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "access_package_display_name": lambda n : setattr(self, 'access_package_display_name', n.get_str_value()),
            "access_package_id": lambda n : setattr(self, 'access_package_id', n.get_str_value()),
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
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("accessPackageDisplayName", self.access_package_display_name)
        writer.write_str_value("accessPackageId", self.access_package_id)
    

