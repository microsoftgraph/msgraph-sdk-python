from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from ....models import assigned_license

@dataclass
class AssignLicensePostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The addLicenses property
    add_licenses: Optional[List[assigned_license.AssignedLicense]] = None
    # The removeLicenses property
    remove_licenses: Optional[List[UUID]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AssignLicensePostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AssignLicensePostRequestBody
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AssignLicensePostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ....models import assigned_license

        from ....models import assigned_license

        fields: Dict[str, Callable[[Any], None]] = {
            "addLicenses": lambda n : setattr(self, 'add_licenses', n.get_collection_of_object_values(assigned_license.AssignedLicense)),
            "removeLicenses": lambda n : setattr(self, 'remove_licenses', n.get_collection_of_primitive_values(UUID)),
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
        writer.write_collection_of_object_values("addLicenses", self.add_licenses)
        writer.write_collection_of_primitive_values("removeLicenses", self.remove_licenses)
        writer.write_additional_data_value(self.additional_data)
    

