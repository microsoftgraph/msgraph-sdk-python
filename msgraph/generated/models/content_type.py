from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

column_definition = lazy_import('msgraph.generated.models.column_definition')
column_link = lazy_import('msgraph.generated.models.column_link')
content_type_order = lazy_import('msgraph.generated.models.content_type_order')
document_set = lazy_import('msgraph.generated.models.document_set')
document_set_content = lazy_import('msgraph.generated.models.document_set_content')
entity = lazy_import('msgraph.generated.models.entity')
item_reference = lazy_import('msgraph.generated.models.item_reference')

class ContentType(entity.Entity):
    """
    Provides operations to manage the admin singleton.
    """
    @property
    def associated_hubs_urls(self,) -> Optional[List[str]]:
        """
        Gets the associatedHubsUrls property value. List of canonical URLs for hub sites with which this content type is associated to. This will contain all hub sites where this content type is queued to be enforced or is already enforced. Enforcing a content type means that the content type will be applied to the lists in the enforced sites.
        Returns: Optional[List[str]]
        """
        return self._associated_hubs_urls
    
    @associated_hubs_urls.setter
    def associated_hubs_urls(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the associatedHubsUrls property value. List of canonical URLs for hub sites with which this content type is associated to. This will contain all hub sites where this content type is queued to be enforced or is already enforced. Enforcing a content type means that the content type will be applied to the lists in the enforced sites.
        Args:
            value: Value to set for the associatedHubsUrls property.
        """
        self._associated_hubs_urls = value
    
    @property
    def base(self,) -> Optional[ContentType]:
        """
        Gets the base property value. Parent contentType from which this content type is derived.
        Returns: Optional[ContentType]
        """
        return self._base
    
    @base.setter
    def base(self,value: Optional[ContentType] = None) -> None:
        """
        Sets the base property value. Parent contentType from which this content type is derived.
        Args:
            value: Value to set for the base property.
        """
        self._base = value
    
    @property
    def base_types(self,) -> Optional[List[ContentType]]:
        """
        Gets the baseTypes property value. The collection of content types that are ancestors of this content type.
        Returns: Optional[List[ContentType]]
        """
        return self._base_types
    
    @base_types.setter
    def base_types(self,value: Optional[List[ContentType]] = None) -> None:
        """
        Sets the baseTypes property value. The collection of content types that are ancestors of this content type.
        Args:
            value: Value to set for the baseTypes property.
        """
        self._base_types = value
    
    @property
    def column_links(self,) -> Optional[List[column_link.ColumnLink]]:
        """
        Gets the columnLinks property value. The collection of columns that are required by this content type.
        Returns: Optional[List[column_link.ColumnLink]]
        """
        return self._column_links
    
    @column_links.setter
    def column_links(self,value: Optional[List[column_link.ColumnLink]] = None) -> None:
        """
        Sets the columnLinks property value. The collection of columns that are required by this content type.
        Args:
            value: Value to set for the columnLinks property.
        """
        self._column_links = value
    
    @property
    def column_positions(self,) -> Optional[List[column_definition.ColumnDefinition]]:
        """
        Gets the columnPositions property value. Column order information in a content type.
        Returns: Optional[List[column_definition.ColumnDefinition]]
        """
        return self._column_positions
    
    @column_positions.setter
    def column_positions(self,value: Optional[List[column_definition.ColumnDefinition]] = None) -> None:
        """
        Sets the columnPositions property value. Column order information in a content type.
        Args:
            value: Value to set for the columnPositions property.
        """
        self._column_positions = value
    
    @property
    def columns(self,) -> Optional[List[column_definition.ColumnDefinition]]:
        """
        Gets the columns property value. The collection of column definitions for this contentType.
        Returns: Optional[List[column_definition.ColumnDefinition]]
        """
        return self._columns
    
    @columns.setter
    def columns(self,value: Optional[List[column_definition.ColumnDefinition]] = None) -> None:
        """
        Sets the columns property value. The collection of column definitions for this contentType.
        Args:
            value: Value to set for the columns property.
        """
        self._columns = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new contentType and sets the default values.
        """
        super().__init__()
        # List of canonical URLs for hub sites with which this content type is associated to. This will contain all hub sites where this content type is queued to be enforced or is already enforced. Enforcing a content type means that the content type will be applied to the lists in the enforced sites.
        self._associated_hubs_urls: Optional[List[str]] = None
        # Parent contentType from which this content type is derived.
        self._base: Optional[ContentType] = None
        # The collection of content types that are ancestors of this content type.
        self._base_types: Optional[List[ContentType]] = None
        # The collection of columns that are required by this content type.
        self._column_links: Optional[List[column_link.ColumnLink]] = None
        # Column order information in a content type.
        self._column_positions: Optional[List[column_definition.ColumnDefinition]] = None
        # The collection of column definitions for this contentType.
        self._columns: Optional[List[column_definition.ColumnDefinition]] = None
        # The descriptive text for the item.
        self._description: Optional[str] = None
        # Document Set metadata.
        self._document_set: Optional[document_set.DocumentSet] = None
        # Document template metadata. To make sure that documents have consistent content across a site and its subsites, you can associate a Word, Excel, or PowerPoint template with a site content type.
        self._document_template: Optional[document_set_content.DocumentSetContent] = None
        # The name of the group this content type belongs to. Helps organize related content types.
        self._group: Optional[str] = None
        # Indicates whether the content type is hidden in the list's 'New' menu.
        self._hidden: Optional[bool] = None
        # If this content type is inherited from another scope (like a site), provides a reference to the item where the content type is defined.
        self._inherited_from: Optional[item_reference.ItemReference] = None
        # Specifies if a content type is a built-in content type.
        self._is_built_in: Optional[bool] = None
        # The name of the content type.
        self._name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Specifies the order in which the content type appears in the selection UI.
        self._order: Optional[content_type_order.ContentTypeOrder] = None
        # The unique identifier of the content type.
        self._parent_id: Optional[str] = None
        # If true, any changes made to the content type will be pushed to inherited content types and lists that implement the content type.
        self._propagate_changes: Optional[bool] = None
        # If true, the content type can't be modified unless this value is first set to false.
        self._read_only: Optional[bool] = None
        # If true, the content type can't be modified by users or through push-down operations. Only site collection administrators can seal or unseal content types.
        self._sealed: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ContentType:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ContentType
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ContentType()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The descriptive text for the item.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The descriptive text for the item.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def document_set(self,) -> Optional[document_set.DocumentSet]:
        """
        Gets the documentSet property value. Document Set metadata.
        Returns: Optional[document_set.DocumentSet]
        """
        return self._document_set
    
    @document_set.setter
    def document_set(self,value: Optional[document_set.DocumentSet] = None) -> None:
        """
        Sets the documentSet property value. Document Set metadata.
        Args:
            value: Value to set for the documentSet property.
        """
        self._document_set = value
    
    @property
    def document_template(self,) -> Optional[document_set_content.DocumentSetContent]:
        """
        Gets the documentTemplate property value. Document template metadata. To make sure that documents have consistent content across a site and its subsites, you can associate a Word, Excel, or PowerPoint template with a site content type.
        Returns: Optional[document_set_content.DocumentSetContent]
        """
        return self._document_template
    
    @document_template.setter
    def document_template(self,value: Optional[document_set_content.DocumentSetContent] = None) -> None:
        """
        Sets the documentTemplate property value. Document template metadata. To make sure that documents have consistent content across a site and its subsites, you can associate a Word, Excel, or PowerPoint template with a site content type.
        Args:
            value: Value to set for the documentTemplate property.
        """
        self._document_template = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "associated_hubs_urls": lambda n : setattr(self, 'associated_hubs_urls', n.get_collection_of_primitive_values(str)),
            "base": lambda n : setattr(self, 'base', n.get_object_value(ContentType)),
            "base_types": lambda n : setattr(self, 'base_types', n.get_collection_of_object_values(ContentType)),
            "column_links": lambda n : setattr(self, 'column_links', n.get_collection_of_object_values(column_link.ColumnLink)),
            "column_positions": lambda n : setattr(self, 'column_positions', n.get_collection_of_object_values(column_definition.ColumnDefinition)),
            "columns": lambda n : setattr(self, 'columns', n.get_collection_of_object_values(column_definition.ColumnDefinition)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "document_set": lambda n : setattr(self, 'document_set', n.get_object_value(document_set.DocumentSet)),
            "document_template": lambda n : setattr(self, 'document_template', n.get_object_value(document_set_content.DocumentSetContent)),
            "group": lambda n : setattr(self, 'group', n.get_str_value()),
            "hidden": lambda n : setattr(self, 'hidden', n.get_bool_value()),
            "inherited_from": lambda n : setattr(self, 'inherited_from', n.get_object_value(item_reference.ItemReference)),
            "is_built_in": lambda n : setattr(self, 'is_built_in', n.get_bool_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "order": lambda n : setattr(self, 'order', n.get_object_value(content_type_order.ContentTypeOrder)),
            "parent_id": lambda n : setattr(self, 'parent_id', n.get_str_value()),
            "propagate_changes": lambda n : setattr(self, 'propagate_changes', n.get_bool_value()),
            "read_only": lambda n : setattr(self, 'read_only', n.get_bool_value()),
            "sealed": lambda n : setattr(self, 'sealed', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def group(self,) -> Optional[str]:
        """
        Gets the group property value. The name of the group this content type belongs to. Helps organize related content types.
        Returns: Optional[str]
        """
        return self._group
    
    @group.setter
    def group(self,value: Optional[str] = None) -> None:
        """
        Sets the group property value. The name of the group this content type belongs to. Helps organize related content types.
        Args:
            value: Value to set for the group property.
        """
        self._group = value
    
    @property
    def hidden(self,) -> Optional[bool]:
        """
        Gets the hidden property value. Indicates whether the content type is hidden in the list's 'New' menu.
        Returns: Optional[bool]
        """
        return self._hidden
    
    @hidden.setter
    def hidden(self,value: Optional[bool] = None) -> None:
        """
        Sets the hidden property value. Indicates whether the content type is hidden in the list's 'New' menu.
        Args:
            value: Value to set for the hidden property.
        """
        self._hidden = value
    
    @property
    def inherited_from(self,) -> Optional[item_reference.ItemReference]:
        """
        Gets the inheritedFrom property value. If this content type is inherited from another scope (like a site), provides a reference to the item where the content type is defined.
        Returns: Optional[item_reference.ItemReference]
        """
        return self._inherited_from
    
    @inherited_from.setter
    def inherited_from(self,value: Optional[item_reference.ItemReference] = None) -> None:
        """
        Sets the inheritedFrom property value. If this content type is inherited from another scope (like a site), provides a reference to the item where the content type is defined.
        Args:
            value: Value to set for the inheritedFrom property.
        """
        self._inherited_from = value
    
    @property
    def is_built_in(self,) -> Optional[bool]:
        """
        Gets the isBuiltIn property value. Specifies if a content type is a built-in content type.
        Returns: Optional[bool]
        """
        return self._is_built_in
    
    @is_built_in.setter
    def is_built_in(self,value: Optional[bool] = None) -> None:
        """
        Sets the isBuiltIn property value. Specifies if a content type is a built-in content type.
        Args:
            value: Value to set for the isBuiltIn property.
        """
        self._is_built_in = value
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. The name of the content type.
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. The name of the content type.
        Args:
            value: Value to set for the name property.
        """
        self._name = value
    
    @property
    def order(self,) -> Optional[content_type_order.ContentTypeOrder]:
        """
        Gets the order property value. Specifies the order in which the content type appears in the selection UI.
        Returns: Optional[content_type_order.ContentTypeOrder]
        """
        return self._order
    
    @order.setter
    def order(self,value: Optional[content_type_order.ContentTypeOrder] = None) -> None:
        """
        Sets the order property value. Specifies the order in which the content type appears in the selection UI.
        Args:
            value: Value to set for the order property.
        """
        self._order = value
    
    @property
    def parent_id(self,) -> Optional[str]:
        """
        Gets the parentId property value. The unique identifier of the content type.
        Returns: Optional[str]
        """
        return self._parent_id
    
    @parent_id.setter
    def parent_id(self,value: Optional[str] = None) -> None:
        """
        Sets the parentId property value. The unique identifier of the content type.
        Args:
            value: Value to set for the parentId property.
        """
        self._parent_id = value
    
    @property
    def propagate_changes(self,) -> Optional[bool]:
        """
        Gets the propagateChanges property value. If true, any changes made to the content type will be pushed to inherited content types and lists that implement the content type.
        Returns: Optional[bool]
        """
        return self._propagate_changes
    
    @propagate_changes.setter
    def propagate_changes(self,value: Optional[bool] = None) -> None:
        """
        Sets the propagateChanges property value. If true, any changes made to the content type will be pushed to inherited content types and lists that implement the content type.
        Args:
            value: Value to set for the propagateChanges property.
        """
        self._propagate_changes = value
    
    @property
    def read_only(self,) -> Optional[bool]:
        """
        Gets the readOnly property value. If true, the content type can't be modified unless this value is first set to false.
        Returns: Optional[bool]
        """
        return self._read_only
    
    @read_only.setter
    def read_only(self,value: Optional[bool] = None) -> None:
        """
        Sets the readOnly property value. If true, the content type can't be modified unless this value is first set to false.
        Args:
            value: Value to set for the readOnly property.
        """
        self._read_only = value
    
    @property
    def sealed(self,) -> Optional[bool]:
        """
        Gets the sealed property value. If true, the content type can't be modified by users or through push-down operations. Only site collection administrators can seal or unseal content types.
        Returns: Optional[bool]
        """
        return self._sealed
    
    @sealed.setter
    def sealed(self,value: Optional[bool] = None) -> None:
        """
        Sets the sealed property value. If true, the content type can't be modified by users or through push-down operations. Only site collection administrators can seal or unseal content types.
        Args:
            value: Value to set for the sealed property.
        """
        self._sealed = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
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
    

