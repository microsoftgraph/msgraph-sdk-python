from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .ediscovery_case import EdiscoveryCase

from ..entity import Entity

@dataclass
class CasesRoot(Entity):
    # The ediscoveryCases property
    ediscovery_cases: Optional[List[EdiscoveryCase]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CasesRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CasesRoot
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CasesRoot()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .ediscovery_case import EdiscoveryCase

        from ..entity import Entity
        from .ediscovery_case import EdiscoveryCase

        fields: Dict[str, Callable[[Any], None]] = {
            "ediscoveryCases": lambda n : setattr(self, 'ediscovery_cases', n.get_collection_of_object_values(EdiscoveryCase)),
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
        writer.write_collection_of_object_values("ediscoveryCases", self.ediscovery_cases)
    

