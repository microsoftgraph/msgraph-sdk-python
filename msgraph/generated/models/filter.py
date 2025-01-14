from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .filter_group import FilterGroup

@dataclass
class Filter(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # *Experimental* Filter group set used to decide whether given object belongs and should be processed as part of this object mapping. An object is considered in scope if ANY of the groups in the collection is evaluated to true.
    category_filter_groups: Optional[list[FilterGroup]] = None
    # Filter group set used to decide whether given object is in scope for provisioning. This is the filter which should be used in most cases. If an object used to satisfy this filter at a given moment, and then the object or the filter was changed so that filter isn't satisfied any longer, such object will get deprovisioned'. An object is considered in scope if ANY of the groups in the collection is evaluated to true.
    groups: Optional[list[FilterGroup]] = None
    # *Experimental* Filter group set used to filter out objects at the early stage of reading them from the directory. If an object doesn't satisfy this filter, then it will not be processed further. Important to understand is that if an object used to satisfy this filter at a given moment, and then the object or the filter was changed so that filter is no longer satisfied, such object will NOT get deprovisioned. An object is considered in scope if ANY of the groups in the collection is evaluated to true.
    input_filter_groups: Optional[list[FilterGroup]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Filter:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Filter
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Filter()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .filter_group import FilterGroup

        from .filter_group import FilterGroup

        fields: dict[str, Callable[[Any], None]] = {
            "categoryFilterGroups": lambda n : setattr(self, 'category_filter_groups', n.get_collection_of_object_values(FilterGroup)),
            "groups": lambda n : setattr(self, 'groups', n.get_collection_of_object_values(FilterGroup)),
            "inputFilterGroups": lambda n : setattr(self, 'input_filter_groups', n.get_collection_of_object_values(FilterGroup)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_collection_of_object_values("categoryFilterGroups", self.category_filter_groups)
        writer.write_collection_of_object_values("groups", self.groups)
        writer.write_collection_of_object_values("inputFilterGroups", self.input_filter_groups)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

