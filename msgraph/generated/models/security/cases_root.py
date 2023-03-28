from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import ediscovery_case
    from .. import entity

from .. import entity

class CasesRoot(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new casesRoot and sets the default values.
        """
        super().__init__()
        # The ediscoveryCases property
        self._ediscovery_cases: Optional[List[ediscovery_case.EdiscoveryCase]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CasesRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CasesRoot
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CasesRoot()
    
    @property
    def ediscovery_cases(self,) -> Optional[List[ediscovery_case.EdiscoveryCase]]:
        """
        Gets the ediscoveryCases property value. The ediscoveryCases property
        Returns: Optional[List[ediscovery_case.EdiscoveryCase]]
        """
        return self._ediscovery_cases
    
    @ediscovery_cases.setter
    def ediscovery_cases(self,value: Optional[List[ediscovery_case.EdiscoveryCase]] = None) -> None:
        """
        Sets the ediscoveryCases property value. The ediscoveryCases property
        Args:
            value: Value to set for the ediscovery_cases property.
        """
        self._ediscovery_cases = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import ediscovery_case
        from .. import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "ediscoveryCases": lambda n : setattr(self, 'ediscovery_cases', n.get_collection_of_object_values(ediscovery_case.EdiscoveryCase)),
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
        writer.write_collection_of_object_values("ediscoveryCases", self.ediscovery_cases)
    

