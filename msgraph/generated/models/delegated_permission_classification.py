from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .permission_classification_type import PermissionClassificationType

from .entity import Entity

@dataclass
class DelegatedPermissionClassification(Entity, Parsable):
    # The classification value. Possible values: low, medium (preview), high (preview). Doesn't support $filter.
    classification: Optional[PermissionClassificationType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The unique identifier (id) for the delegated permission listed in the oauth2PermissionScopes collection of the servicePrincipal. Required on create. Doesn't support $filter.
    permission_id: Optional[str] = None
    # The claim value (value) for the delegated permission listed in the oauth2PermissionScopes collection of the servicePrincipal. Doesn't support $filter.
    permission_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DelegatedPermissionClassification:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DelegatedPermissionClassification
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DelegatedPermissionClassification()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .permission_classification_type import PermissionClassificationType

        from .entity import Entity
        from .permission_classification_type import PermissionClassificationType

        fields: dict[str, Callable[[Any], None]] = {
            "classification": lambda n : setattr(self, 'classification', n.get_enum_value(PermissionClassificationType)),
            "permissionId": lambda n : setattr(self, 'permission_id', n.get_str_value()),
            "permissionName": lambda n : setattr(self, 'permission_name', n.get_str_value()),
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
        writer.write_enum_value("classification", self.classification)
        writer.write_str_value("permissionId", self.permission_id)
        writer.write_str_value("permissionName", self.permission_name)
    

