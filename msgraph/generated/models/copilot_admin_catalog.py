from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .copilot_package_detail import CopilotPackageDetail
    from .entity import Entity

from .entity import Entity

@dataclass
class CopilotAdminCatalog(Entity, Parsable):
    # The OdataType property
    odata_type: Optional[str] = None
    # The packages property
    packages: Optional[list[CopilotPackageDetail]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CopilotAdminCatalog:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CopilotAdminCatalog
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CopilotAdminCatalog()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .copilot_package_detail import CopilotPackageDetail
        from .entity import Entity

        from .copilot_package_detail import CopilotPackageDetail
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "packages": lambda n : setattr(self, 'packages', n.get_collection_of_object_values(CopilotPackageDetail)),
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
        writer.write_collection_of_object_values("packages", self.packages)
    

