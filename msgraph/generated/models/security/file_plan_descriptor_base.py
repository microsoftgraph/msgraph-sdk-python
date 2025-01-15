from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .file_plan_applied_category import FilePlanAppliedCategory
    from .file_plan_authority import FilePlanAuthority
    from .file_plan_citation import FilePlanCitation
    from .file_plan_department import FilePlanDepartment
    from .file_plan_reference import FilePlanReference
    from .file_plan_subcategory import FilePlanSubcategory

@dataclass
class FilePlanDescriptorBase(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Unique string that defines the name for the file plan descriptor associated with a particular retention label.
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FilePlanDescriptorBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FilePlanDescriptorBase
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.filePlanAppliedCategory".casefold():
            from .file_plan_applied_category import FilePlanAppliedCategory

            return FilePlanAppliedCategory()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.filePlanAuthority".casefold():
            from .file_plan_authority import FilePlanAuthority

            return FilePlanAuthority()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.filePlanCitation".casefold():
            from .file_plan_citation import FilePlanCitation

            return FilePlanCitation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.filePlanDepartment".casefold():
            from .file_plan_department import FilePlanDepartment

            return FilePlanDepartment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.filePlanReference".casefold():
            from .file_plan_reference import FilePlanReference

            return FilePlanReference()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.filePlanSubcategory".casefold():
            from .file_plan_subcategory import FilePlanSubcategory

            return FilePlanSubcategory()
        return FilePlanDescriptorBase()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .file_plan_applied_category import FilePlanAppliedCategory
        from .file_plan_authority import FilePlanAuthority
        from .file_plan_citation import FilePlanCitation
        from .file_plan_department import FilePlanDepartment
        from .file_plan_reference import FilePlanReference
        from .file_plan_subcategory import FilePlanSubcategory

        from .file_plan_applied_category import FilePlanAppliedCategory
        from .file_plan_authority import FilePlanAuthority
        from .file_plan_citation import FilePlanCitation
        from .file_plan_department import FilePlanDepartment
        from .file_plan_reference import FilePlanReference
        from .file_plan_subcategory import FilePlanSubcategory

        fields: dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

