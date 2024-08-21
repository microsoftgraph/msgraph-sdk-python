from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from ....models.assigned_license import AssignedLicense

@dataclass
class AssignLicensePostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The addLicenses property
    add_licenses: Optional[List[AssignedLicense]] = None
    # The removeLicenses property
    remove_licenses: Optional[List[UUID]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AssignLicensePostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AssignLicensePostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AssignLicensePostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ....models.assigned_license import AssignedLicense

        from ....models.assigned_license import AssignedLicense

        fields: Dict[str, Callable[[Any], None]] = {
            "addLicenses": lambda n : setattr(self, 'add_licenses', n.get_collection_of_object_values(AssignedLicense)),
            "removeLicenses": lambda n : setattr(self, 'remove_licenses', n.get_collection_of_primitive_values(UUID)),
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
        writer.write_collection_of_object_values("addLicenses", self.add_licenses)
        writer.write_collection_of_primitive_values("removeLicenses", self.remove_licenses)
        writer.write_additional_data_value(self.additional_data)
    

