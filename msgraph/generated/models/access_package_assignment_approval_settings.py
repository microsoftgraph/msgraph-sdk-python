from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_package_approval_stage import AccessPackageApprovalStage

@dataclass
class AccessPackageAssignmentApprovalSettings(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # If false, then approval isn't required for new requests in this policy.
    is_approval_required_for_add: Optional[bool] = None
    # If false, then approval isn't required for updates to requests in this policy.
    is_approval_required_for_update: Optional[bool] = None
    # If false, then requestor justification isn't required for updates to requests in this policy.
    is_requestor_justification_required: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # If approval is required, the one, two or three elements of this collection define each of the stages of approval. An empty array is present if no approval is required.
    stages: Optional[list[AccessPackageApprovalStage]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AccessPackageAssignmentApprovalSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageAssignmentApprovalSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AccessPackageAssignmentApprovalSettings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .access_package_approval_stage import AccessPackageApprovalStage

        from .access_package_approval_stage import AccessPackageApprovalStage

        fields: dict[str, Callable[[Any], None]] = {
            "isApprovalRequiredForAdd": lambda n : setattr(self, 'is_approval_required_for_add', n.get_bool_value()),
            "isApprovalRequiredForUpdate": lambda n : setattr(self, 'is_approval_required_for_update', n.get_bool_value()),
            "isRequestorJustificationRequired": lambda n : setattr(self, 'is_requestor_justification_required', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "stages": lambda n : setattr(self, 'stages', n.get_collection_of_object_values(AccessPackageApprovalStage)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_bool_value("isApprovalRequiredForAdd", self.is_approval_required_for_add)
        writer.write_bool_value("isApprovalRequiredForUpdate", self.is_approval_required_for_update)
        writer.write_bool_value("isRequestorJustificationRequired", self.is_requestor_justification_required)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("stages", self.stages)
        writer.write_additional_data_value(self.additional_data)
    

