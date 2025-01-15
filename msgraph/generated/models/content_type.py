from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .column_definition import ColumnDefinition
    from .column_link import ColumnLink
    from .content_type_order import ContentTypeOrder
    from .document_set import DocumentSet
    from .document_set_content import DocumentSetContent
    from .entity import Entity
    from .item_reference import ItemReference

from .entity import Entity

@dataclass
class ContentType(Entity, Parsable):
    # List of canonical URLs for hub sites with which this content type is associated to. This will contain all hub sites where this content type is queued to be enforced or is already enforced. Enforcing a content type means that the content type is applied to the lists in the enforced sites.
    associated_hubs_urls: Optional[list[str]] = None
    # Parent contentType from which this content type is derived.
    base: Optional[ContentType] = None
    # The collection of content types that are ancestors of this content type.
    base_types: Optional[list[ContentType]] = None
    # The collection of columns that are required by this content type.
    column_links: Optional[list[ColumnLink]] = None
    # Column order information in a content type.
    column_positions: Optional[list[ColumnDefinition]] = None
    # The collection of column definitions for this content type.
    columns: Optional[list[ColumnDefinition]] = None
    # The descriptive text for the item.
    description: Optional[str] = None
    # Document Set metadata.
    document_set: Optional[DocumentSet] = None
    # Document template metadata. To make sure that documents have consistent content across a site and its subsites, you can associate a Word, Excel, or PowerPoint template with a site content type.
    document_template: Optional[DocumentSetContent] = None
    # The name of the group this content type belongs to. Helps organize related content types.
    group: Optional[str] = None
    # Indicates whether the content type is hidden in the list's 'New' menu.
    hidden: Optional[bool] = None
    # If this content type is inherited from another scope (like a site), provides a reference to the item where the content type is defined.
    inherited_from: Optional[ItemReference] = None
    # Specifies if a content type is a built-in content type.
    is_built_in: Optional[bool] = None
    # The name of the content type.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Specifies the order in which the content type appears in the selection UI.
    order: Optional[ContentTypeOrder] = None
    # The unique identifier of the content type.
    parent_id: Optional[str] = None
    # If true, any changes made to the content type are pushed to inherited content types and lists that implement the content type.
    propagate_changes: Optional[bool] = None
    # If true, the content type can't be modified unless this value is first set to false.
    read_only: Optional[bool] = None
    # If true, the content type can't be modified by users or through push-down operations. Only site collection administrators can seal or unseal content types.
    sealed: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ContentType:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ContentType
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ContentType()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .column_definition import ColumnDefinition
        from .column_link import ColumnLink
        from .content_type_order import ContentTypeOrder
        from .document_set import DocumentSet
        from .document_set_content import DocumentSetContent
        from .entity import Entity
        from .item_reference import ItemReference

        from .column_definition import ColumnDefinition
        from .column_link import ColumnLink
        from .content_type_order import ContentTypeOrder
        from .document_set import DocumentSet
        from .document_set_content import DocumentSetContent
        from .entity import Entity
        from .item_reference import ItemReference

        fields: dict[str, Callable[[Any], None]] = {
            "associatedHubsUrls": lambda n : setattr(self, 'associated_hubs_urls', n.get_collection_of_primitive_values(str)),
            "base": lambda n : setattr(self, 'base', n.get_object_value(ContentType)),
            "baseTypes": lambda n : setattr(self, 'base_types', n.get_collection_of_object_values(ContentType)),
            "columnLinks": lambda n : setattr(self, 'column_links', n.get_collection_of_object_values(ColumnLink)),
            "columnPositions": lambda n : setattr(self, 'column_positions', n.get_collection_of_object_values(ColumnDefinition)),
            "columns": lambda n : setattr(self, 'columns', n.get_collection_of_object_values(ColumnDefinition)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "documentSet": lambda n : setattr(self, 'document_set', n.get_object_value(DocumentSet)),
            "documentTemplate": lambda n : setattr(self, 'document_template', n.get_object_value(DocumentSetContent)),
            "group": lambda n : setattr(self, 'group', n.get_str_value()),
            "hidden": lambda n : setattr(self, 'hidden', n.get_bool_value()),
            "inheritedFrom": lambda n : setattr(self, 'inherited_from', n.get_object_value(ItemReference)),
            "isBuiltIn": lambda n : setattr(self, 'is_built_in', n.get_bool_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "order": lambda n : setattr(self, 'order', n.get_object_value(ContentTypeOrder)),
            "parentId": lambda n : setattr(self, 'parent_id', n.get_str_value()),
            "propagateChanges": lambda n : setattr(self, 'propagate_changes', n.get_bool_value()),
            "readOnly": lambda n : setattr(self, 'read_only', n.get_bool_value()),
            "sealed": lambda n : setattr(self, 'sealed', n.get_bool_value()),
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
        writer.write_collection_of_primitive_values("associatedHubsUrls", self.associated_hubs_urls)
        writer.write_object_value("base", self.base)
        writer.write_collection_of_object_values("baseTypes", self.base_types)
        writer.write_collection_of_object_values("columnLinks", self.column_links)
        writer.write_collection_of_object_values("columnPositions", self.column_positions)
        writer.write_collection_of_object_values("columns", self.columns)
        writer.write_str_value("description", self.description)
        writer.write_object_value("documentSet", self.document_set)
        writer.write_object_value("documentTemplate", self.document_template)
        writer.write_str_value("group", self.group)
        writer.write_bool_value("hidden", self.hidden)
        writer.write_object_value("inheritedFrom", self.inherited_from)
        writer.write_bool_value("isBuiltIn", self.is_built_in)
        writer.write_str_value("name", self.name)
        writer.write_object_value("order", self.order)
        writer.write_str_value("parentId", self.parent_id)
        writer.write_bool_value("propagateChanges", self.propagate_changes)
        writer.write_bool_value("readOnly", self.read_only)
        writer.write_bool_value("sealed", self.sealed)
    

