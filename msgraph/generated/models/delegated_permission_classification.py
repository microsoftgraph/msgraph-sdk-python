from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
permission_classification_type = lazy_import('msgraph.generated.models.permission_classification_type')

class DelegatedPermissionClassification(entity.Entity):
    """
    Provides operations to call the instantiate method.
    """
    @property
    def classification(self,) -> Optional[permission_classification_type.PermissionClassificationType]:
        """
        Gets the classification property value. The classification value being given. Possible value: low. Does not support $filter.
        Returns: Optional[permission_classification_type.PermissionClassificationType]
        """
        return self._classification
    
    @classification.setter
    def classification(self,value: Optional[permission_classification_type.PermissionClassificationType] = None) -> None:
        """
        Sets the classification property value. The classification value being given. Possible value: low. Does not support $filter.
        Args:
            value: Value to set for the classification property.
        """
        self._classification = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new delegatedPermissionClassification and sets the default values.
        """
        super().__init__()
        # The classification value being given. Possible value: low. Does not support $filter.
        self._classification: Optional[permission_classification_type.PermissionClassificationType] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The unique identifier (id) for the delegated permission listed in the oauth2PermissionScopes collection of the servicePrincipal. Required on create. Does not support $filter.
        self._permission_id: Optional[str] = None
        # The claim value (value) for the delegated permission listed in the oauth2PermissionScopes collection of the servicePrincipal. Does not support $filter.
        self._permission_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DelegatedPermissionClassification:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DelegatedPermissionClassification
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DelegatedPermissionClassification()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "classification": lambda n : setattr(self, 'classification', n.get_enum_value(permission_classification_type.PermissionClassificationType)),
            "permission_id": lambda n : setattr(self, 'permission_id', n.get_str_value()),
            "permission_name": lambda n : setattr(self, 'permission_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def permission_id(self,) -> Optional[str]:
        """
        Gets the permissionId property value. The unique identifier (id) for the delegated permission listed in the oauth2PermissionScopes collection of the servicePrincipal. Required on create. Does not support $filter.
        Returns: Optional[str]
        """
        return self._permission_id
    
    @permission_id.setter
    def permission_id(self,value: Optional[str] = None) -> None:
        """
        Sets the permissionId property value. The unique identifier (id) for the delegated permission listed in the oauth2PermissionScopes collection of the servicePrincipal. Required on create. Does not support $filter.
        Args:
            value: Value to set for the permissionId property.
        """
        self._permission_id = value
    
    @property
    def permission_name(self,) -> Optional[str]:
        """
        Gets the permissionName property value. The claim value (value) for the delegated permission listed in the oauth2PermissionScopes collection of the servicePrincipal. Does not support $filter.
        Returns: Optional[str]
        """
        return self._permission_name
    
    @permission_name.setter
    def permission_name(self,value: Optional[str] = None) -> None:
        """
        Sets the permissionName property value. The claim value (value) for the delegated permission listed in the oauth2PermissionScopes collection of the servicePrincipal. Does not support $filter.
        Args:
            value: Value to set for the permissionName property.
        """
        self._permission_name = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("classification", self.classification)
        writer.write_str_value("permissionId", self.permission_id)
        writer.write_str_value("permissionName", self.permission_name)
    

