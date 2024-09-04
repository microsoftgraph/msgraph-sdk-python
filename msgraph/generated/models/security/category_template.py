from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .file_plan_descriptor_template import FilePlanDescriptorTemplate
    from .subcategory_template import SubcategoryTemplate

from .file_plan_descriptor_template import FilePlanDescriptorTemplate

@dataclass
class CategoryTemplate(FilePlanDescriptorTemplate):
    # The OdataType property
    odata_type: Optional[str] = None
    # Represents all subcategories under a particular category.
    subcategories: Optional[List[SubcategoryTemplate]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CategoryTemplate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CategoryTemplate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CategoryTemplate()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .file_plan_descriptor_template import FilePlanDescriptorTemplate
        from .subcategory_template import SubcategoryTemplate

        from .file_plan_descriptor_template import FilePlanDescriptorTemplate
        from .subcategory_template import SubcategoryTemplate

        fields: Dict[str, Callable[[Any], None]] = {
            "subcategories": lambda n : setattr(self, 'subcategories', n.get_collection_of_object_values(SubcategoryTemplate)),
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
        writer.write_collection_of_object_values("subcategories", self.subcategories)
    

