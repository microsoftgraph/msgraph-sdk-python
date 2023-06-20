from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import access_package_approval_stage

@dataclass
class AccessPackageAssignmentApprovalSettings(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # If false, then approval is not required for new requests in this policy.
    is_approval_required_for_add: Optional[bool] = None
    # If false, then approval is not required for updates to requests in this policy.
    is_approval_required_for_update: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # If approval is required, the one, two or three elements of this collection define each of the stages of approval. An empty array is present if no approval is required.
    stages: Optional[List[access_package_approval_stage.AccessPackageApprovalStage]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessPackageAssignmentApprovalSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageAssignmentApprovalSettings
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AccessPackageAssignmentApprovalSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import access_package_approval_stage

        from . import access_package_approval_stage

        fields: Dict[str, Callable[[Any], None]] = {
            "isApprovalRequiredForAdd": lambda n : setattr(self, 'is_approval_required_for_add', n.get_bool_value()),
            "isApprovalRequiredForUpdate": lambda n : setattr(self, 'is_approval_required_for_update', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "stages": lambda n : setattr(self, 'stages', n.get_collection_of_object_values(access_package_approval_stage.AccessPackageApprovalStage)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_bool_value("isApprovalRequiredForAdd", self.is_approval_required_for_add)
        writer.write_bool_value("isApprovalRequiredForUpdate", self.is_approval_required_for_update)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("stages", self.stages)
        writer.write_additional_data_value(self.additional_data)
    

