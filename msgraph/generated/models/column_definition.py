from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

boolean_column = lazy_import('msgraph.generated.models.boolean_column')
calculated_column = lazy_import('msgraph.generated.models.calculated_column')
choice_column = lazy_import('msgraph.generated.models.choice_column')
column_types = lazy_import('msgraph.generated.models.column_types')
column_validation = lazy_import('msgraph.generated.models.column_validation')
content_approval_status_column = lazy_import('msgraph.generated.models.content_approval_status_column')
content_type_info = lazy_import('msgraph.generated.models.content_type_info')
currency_column = lazy_import('msgraph.generated.models.currency_column')
date_time_column = lazy_import('msgraph.generated.models.date_time_column')
default_column_value = lazy_import('msgraph.generated.models.default_column_value')
entity = lazy_import('msgraph.generated.models.entity')
geolocation_column = lazy_import('msgraph.generated.models.geolocation_column')
hyperlink_or_picture_column = lazy_import('msgraph.generated.models.hyperlink_or_picture_column')
lookup_column = lazy_import('msgraph.generated.models.lookup_column')
number_column = lazy_import('msgraph.generated.models.number_column')
person_or_group_column = lazy_import('msgraph.generated.models.person_or_group_column')
term_column = lazy_import('msgraph.generated.models.term_column')
text_column = lazy_import('msgraph.generated.models.text_column')
thumbnail_column = lazy_import('msgraph.generated.models.thumbnail_column')

class ColumnDefinition(entity.Entity):
    """
    Provides operations to manage the collection of agreement entities.
    """
    @property
    def boolean(self,) -> Optional[boolean_column.BooleanColumn]:
        """
        Gets the boolean property value. This column stores boolean values.
        Returns: Optional[boolean_column.BooleanColumn]
        """
        return self._boolean
    
    @boolean.setter
    def boolean(self,value: Optional[boolean_column.BooleanColumn] = None) -> None:
        """
        Sets the boolean property value. This column stores boolean values.
        Args:
            value: Value to set for the boolean property.
        """
        self._boolean = value
    
    @property
    def calculated(self,) -> Optional[calculated_column.CalculatedColumn]:
        """
        Gets the calculated property value. This column's data is calculated based on other columns.
        Returns: Optional[calculated_column.CalculatedColumn]
        """
        return self._calculated
    
    @calculated.setter
    def calculated(self,value: Optional[calculated_column.CalculatedColumn] = None) -> None:
        """
        Sets the calculated property value. This column's data is calculated based on other columns.
        Args:
            value: Value to set for the calculated property.
        """
        self._calculated = value
    
    @property
    def choice(self,) -> Optional[choice_column.ChoiceColumn]:
        """
        Gets the choice property value. This column stores data from a list of choices.
        Returns: Optional[choice_column.ChoiceColumn]
        """
        return self._choice
    
    @choice.setter
    def choice(self,value: Optional[choice_column.ChoiceColumn] = None) -> None:
        """
        Sets the choice property value. This column stores data from a list of choices.
        Args:
            value: Value to set for the choice property.
        """
        self._choice = value
    
    @property
    def column_group(self,) -> Optional[str]:
        """
        Gets the columnGroup property value. For site columns, the name of the group this column belongs to. Helps organize related columns.
        Returns: Optional[str]
        """
        return self._column_group
    
    @column_group.setter
    def column_group(self,value: Optional[str] = None) -> None:
        """
        Sets the columnGroup property value. For site columns, the name of the group this column belongs to. Helps organize related columns.
        Args:
            value: Value to set for the columnGroup property.
        """
        self._column_group = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new columnDefinition and sets the default values.
        """
        super().__init__()
        # This column stores boolean values.
        self._boolean: Optional[boolean_column.BooleanColumn] = None
        # This column's data is calculated based on other columns.
        self._calculated: Optional[calculated_column.CalculatedColumn] = None
        # This column stores data from a list of choices.
        self._choice: Optional[choice_column.ChoiceColumn] = None
        # For site columns, the name of the group this column belongs to. Helps organize related columns.
        self._column_group: Optional[str] = None
        # This column stores content approval status.
        self._content_approval_status: Optional[content_approval_status_column.ContentApprovalStatusColumn] = None
        # This column stores currency values.
        self._currency: Optional[currency_column.CurrencyColumn] = None
        # This column stores DateTime values.
        self._date_time: Optional[date_time_column.DateTimeColumn] = None
        # The default value for this column.
        self._default_value: Optional[default_column_value.DefaultColumnValue] = None
        # The user-facing description of the column.
        self._description: Optional[str] = None
        # The user-facing name of the column.
        self._display_name: Optional[str] = None
        # If true, no two list items may have the same value for this column.
        self._enforce_unique_values: Optional[bool] = None
        # This column stores a geolocation.
        self._geolocation: Optional[geolocation_column.GeolocationColumn] = None
        # Specifies whether the column is displayed in the user interface.
        self._hidden: Optional[bool] = None
        # This column stores hyperlink or picture values.
        self._hyperlink_or_picture: Optional[hyperlink_or_picture_column.HyperlinkOrPictureColumn] = None
        # Specifies whether the column values can be used for sorting and searching.
        self._indexed: Optional[bool] = None
        # Indicates whether this column can be deleted.
        self._is_deletable: Optional[bool] = None
        # Indicates whether values in the column can be reordered. Read-only.
        self._is_reorderable: Optional[bool] = None
        # Specifies whether the column can be changed.
        self._is_sealed: Optional[bool] = None
        # This column's data is looked up from another source in the site.
        self._lookup: Optional[lookup_column.LookupColumn] = None
        # The API-facing name of the column as it appears in the [fields][] on a [listItem][]. For the user-facing name, see displayName.
        self._name: Optional[str] = None
        # This column stores number values.
        self._number: Optional[number_column.NumberColumn] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # This column stores Person or Group values.
        self._person_or_group: Optional[person_or_group_column.PersonOrGroupColumn] = None
        # If 'true', changes to this column will be propagated to lists that implement the column.
        self._propagate_changes: Optional[bool] = None
        # Specifies whether the column values can be modified.
        self._read_only: Optional[bool] = None
        # Specifies whether the column value isn't optional.
        self._required: Optional[bool] = None
        # The source column for the content type column.
        self._source_column: Optional[ColumnDefinition] = None
        # ContentType from which this column is inherited from. Present only in contentTypes columns response. Read-only.
        self._source_content_type: Optional[content_type_info.ContentTypeInfo] = None
        # This column stores taxonomy terms.
        self._term: Optional[term_column.TermColumn] = None
        # This column stores text values.
        self._text: Optional[text_column.TextColumn] = None
        # This column stores thumbnail values.
        self._thumbnail: Optional[thumbnail_column.ThumbnailColumn] = None
        # For site columns, the type of column. Read-only.
        self._type: Optional[column_types.ColumnTypes] = None
        # This column stores validation formula and message for the column.
        self._validation: Optional[column_validation.ColumnValidation] = None
    
    @property
    def content_approval_status(self,) -> Optional[content_approval_status_column.ContentApprovalStatusColumn]:
        """
        Gets the contentApprovalStatus property value. This column stores content approval status.
        Returns: Optional[content_approval_status_column.ContentApprovalStatusColumn]
        """
        return self._content_approval_status
    
    @content_approval_status.setter
    def content_approval_status(self,value: Optional[content_approval_status_column.ContentApprovalStatusColumn] = None) -> None:
        """
        Sets the contentApprovalStatus property value. This column stores content approval status.
        Args:
            value: Value to set for the contentApprovalStatus property.
        """
        self._content_approval_status = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ColumnDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ColumnDefinition
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ColumnDefinition()
    
    @property
    def currency(self,) -> Optional[currency_column.CurrencyColumn]:
        """
        Gets the currency property value. This column stores currency values.
        Returns: Optional[currency_column.CurrencyColumn]
        """
        return self._currency
    
    @currency.setter
    def currency(self,value: Optional[currency_column.CurrencyColumn] = None) -> None:
        """
        Sets the currency property value. This column stores currency values.
        Args:
            value: Value to set for the currency property.
        """
        self._currency = value
    
    @property
    def date_time(self,) -> Optional[date_time_column.DateTimeColumn]:
        """
        Gets the dateTime property value. This column stores DateTime values.
        Returns: Optional[date_time_column.DateTimeColumn]
        """
        return self._date_time
    
    @date_time.setter
    def date_time(self,value: Optional[date_time_column.DateTimeColumn] = None) -> None:
        """
        Sets the dateTime property value. This column stores DateTime values.
        Args:
            value: Value to set for the dateTime property.
        """
        self._date_time = value
    
    @property
    def default_value(self,) -> Optional[default_column_value.DefaultColumnValue]:
        """
        Gets the defaultValue property value. The default value for this column.
        Returns: Optional[default_column_value.DefaultColumnValue]
        """
        return self._default_value
    
    @default_value.setter
    def default_value(self,value: Optional[default_column_value.DefaultColumnValue] = None) -> None:
        """
        Sets the defaultValue property value. The default value for this column.
        Args:
            value: Value to set for the defaultValue property.
        """
        self._default_value = value
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The user-facing description of the column.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The user-facing description of the column.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The user-facing name of the column.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The user-facing name of the column.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def enforce_unique_values(self,) -> Optional[bool]:
        """
        Gets the enforceUniqueValues property value. If true, no two list items may have the same value for this column.
        Returns: Optional[bool]
        """
        return self._enforce_unique_values
    
    @enforce_unique_values.setter
    def enforce_unique_values(self,value: Optional[bool] = None) -> None:
        """
        Sets the enforceUniqueValues property value. If true, no two list items may have the same value for this column.
        Args:
            value: Value to set for the enforceUniqueValues property.
        """
        self._enforce_unique_values = value
    
    @property
    def geolocation(self,) -> Optional[geolocation_column.GeolocationColumn]:
        """
        Gets the geolocation property value. This column stores a geolocation.
        Returns: Optional[geolocation_column.GeolocationColumn]
        """
        return self._geolocation
    
    @geolocation.setter
    def geolocation(self,value: Optional[geolocation_column.GeolocationColumn] = None) -> None:
        """
        Sets the geolocation property value. This column stores a geolocation.
        Args:
            value: Value to set for the geolocation property.
        """
        self._geolocation = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "boolean": lambda n : setattr(self, 'boolean', n.get_object_value(boolean_column.BooleanColumn)),
            "calculated": lambda n : setattr(self, 'calculated', n.get_object_value(calculated_column.CalculatedColumn)),
            "choice": lambda n : setattr(self, 'choice', n.get_object_value(choice_column.ChoiceColumn)),
            "column_group": lambda n : setattr(self, 'column_group', n.get_str_value()),
            "content_approval_status": lambda n : setattr(self, 'content_approval_status', n.get_object_value(content_approval_status_column.ContentApprovalStatusColumn)),
            "currency": lambda n : setattr(self, 'currency', n.get_object_value(currency_column.CurrencyColumn)),
            "date_time": lambda n : setattr(self, 'date_time', n.get_object_value(date_time_column.DateTimeColumn)),
            "default_value": lambda n : setattr(self, 'default_value', n.get_object_value(default_column_value.DefaultColumnValue)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "enforce_unique_values": lambda n : setattr(self, 'enforce_unique_values', n.get_bool_value()),
            "geolocation": lambda n : setattr(self, 'geolocation', n.get_object_value(geolocation_column.GeolocationColumn)),
            "hidden": lambda n : setattr(self, 'hidden', n.get_bool_value()),
            "hyperlink_or_picture": lambda n : setattr(self, 'hyperlink_or_picture', n.get_object_value(hyperlink_or_picture_column.HyperlinkOrPictureColumn)),
            "indexed": lambda n : setattr(self, 'indexed', n.get_bool_value()),
            "is_deletable": lambda n : setattr(self, 'is_deletable', n.get_bool_value()),
            "is_reorderable": lambda n : setattr(self, 'is_reorderable', n.get_bool_value()),
            "is_sealed": lambda n : setattr(self, 'is_sealed', n.get_bool_value()),
            "lookup": lambda n : setattr(self, 'lookup', n.get_object_value(lookup_column.LookupColumn)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "number": lambda n : setattr(self, 'number', n.get_object_value(number_column.NumberColumn)),
            "person_or_group": lambda n : setattr(self, 'person_or_group', n.get_object_value(person_or_group_column.PersonOrGroupColumn)),
            "propagate_changes": lambda n : setattr(self, 'propagate_changes', n.get_bool_value()),
            "read_only": lambda n : setattr(self, 'read_only', n.get_bool_value()),
            "required": lambda n : setattr(self, 'required', n.get_bool_value()),
            "source_column": lambda n : setattr(self, 'source_column', n.get_object_value(ColumnDefinition)),
            "source_content_type": lambda n : setattr(self, 'source_content_type', n.get_object_value(content_type_info.ContentTypeInfo)),
            "term": lambda n : setattr(self, 'term', n.get_object_value(term_column.TermColumn)),
            "text": lambda n : setattr(self, 'text', n.get_object_value(text_column.TextColumn)),
            "thumbnail": lambda n : setattr(self, 'thumbnail', n.get_object_value(thumbnail_column.ThumbnailColumn)),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(column_types.ColumnTypes)),
            "validation": lambda n : setattr(self, 'validation', n.get_object_value(column_validation.ColumnValidation)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def hidden(self,) -> Optional[bool]:
        """
        Gets the hidden property value. Specifies whether the column is displayed in the user interface.
        Returns: Optional[bool]
        """
        return self._hidden
    
    @hidden.setter
    def hidden(self,value: Optional[bool] = None) -> None:
        """
        Sets the hidden property value. Specifies whether the column is displayed in the user interface.
        Args:
            value: Value to set for the hidden property.
        """
        self._hidden = value
    
    @property
    def hyperlink_or_picture(self,) -> Optional[hyperlink_or_picture_column.HyperlinkOrPictureColumn]:
        """
        Gets the hyperlinkOrPicture property value. This column stores hyperlink or picture values.
        Returns: Optional[hyperlink_or_picture_column.HyperlinkOrPictureColumn]
        """
        return self._hyperlink_or_picture
    
    @hyperlink_or_picture.setter
    def hyperlink_or_picture(self,value: Optional[hyperlink_or_picture_column.HyperlinkOrPictureColumn] = None) -> None:
        """
        Sets the hyperlinkOrPicture property value. This column stores hyperlink or picture values.
        Args:
            value: Value to set for the hyperlinkOrPicture property.
        """
        self._hyperlink_or_picture = value
    
    @property
    def indexed(self,) -> Optional[bool]:
        """
        Gets the indexed property value. Specifies whether the column values can be used for sorting and searching.
        Returns: Optional[bool]
        """
        return self._indexed
    
    @indexed.setter
    def indexed(self,value: Optional[bool] = None) -> None:
        """
        Sets the indexed property value. Specifies whether the column values can be used for sorting and searching.
        Args:
            value: Value to set for the indexed property.
        """
        self._indexed = value
    
    @property
    def is_deletable(self,) -> Optional[bool]:
        """
        Gets the isDeletable property value. Indicates whether this column can be deleted.
        Returns: Optional[bool]
        """
        return self._is_deletable
    
    @is_deletable.setter
    def is_deletable(self,value: Optional[bool] = None) -> None:
        """
        Sets the isDeletable property value. Indicates whether this column can be deleted.
        Args:
            value: Value to set for the isDeletable property.
        """
        self._is_deletable = value
    
    @property
    def is_reorderable(self,) -> Optional[bool]:
        """
        Gets the isReorderable property value. Indicates whether values in the column can be reordered. Read-only.
        Returns: Optional[bool]
        """
        return self._is_reorderable
    
    @is_reorderable.setter
    def is_reorderable(self,value: Optional[bool] = None) -> None:
        """
        Sets the isReorderable property value. Indicates whether values in the column can be reordered. Read-only.
        Args:
            value: Value to set for the isReorderable property.
        """
        self._is_reorderable = value
    
    @property
    def is_sealed(self,) -> Optional[bool]:
        """
        Gets the isSealed property value. Specifies whether the column can be changed.
        Returns: Optional[bool]
        """
        return self._is_sealed
    
    @is_sealed.setter
    def is_sealed(self,value: Optional[bool] = None) -> None:
        """
        Sets the isSealed property value. Specifies whether the column can be changed.
        Args:
            value: Value to set for the isSealed property.
        """
        self._is_sealed = value
    
    @property
    def lookup(self,) -> Optional[lookup_column.LookupColumn]:
        """
        Gets the lookup property value. This column's data is looked up from another source in the site.
        Returns: Optional[lookup_column.LookupColumn]
        """
        return self._lookup
    
    @lookup.setter
    def lookup(self,value: Optional[lookup_column.LookupColumn] = None) -> None:
        """
        Sets the lookup property value. This column's data is looked up from another source in the site.
        Args:
            value: Value to set for the lookup property.
        """
        self._lookup = value
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. The API-facing name of the column as it appears in the [fields][] on a [listItem][]. For the user-facing name, see displayName.
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. The API-facing name of the column as it appears in the [fields][] on a [listItem][]. For the user-facing name, see displayName.
        Args:
            value: Value to set for the name property.
        """
        self._name = value
    
    @property
    def number(self,) -> Optional[number_column.NumberColumn]:
        """
        Gets the number property value. This column stores number values.
        Returns: Optional[number_column.NumberColumn]
        """
        return self._number
    
    @number.setter
    def number(self,value: Optional[number_column.NumberColumn] = None) -> None:
        """
        Sets the number property value. This column stores number values.
        Args:
            value: Value to set for the number property.
        """
        self._number = value
    
    @property
    def person_or_group(self,) -> Optional[person_or_group_column.PersonOrGroupColumn]:
        """
        Gets the personOrGroup property value. This column stores Person or Group values.
        Returns: Optional[person_or_group_column.PersonOrGroupColumn]
        """
        return self._person_or_group
    
    @person_or_group.setter
    def person_or_group(self,value: Optional[person_or_group_column.PersonOrGroupColumn] = None) -> None:
        """
        Sets the personOrGroup property value. This column stores Person or Group values.
        Args:
            value: Value to set for the personOrGroup property.
        """
        self._person_or_group = value
    
    @property
    def propagate_changes(self,) -> Optional[bool]:
        """
        Gets the propagateChanges property value. If 'true', changes to this column will be propagated to lists that implement the column.
        Returns: Optional[bool]
        """
        return self._propagate_changes
    
    @propagate_changes.setter
    def propagate_changes(self,value: Optional[bool] = None) -> None:
        """
        Sets the propagateChanges property value. If 'true', changes to this column will be propagated to lists that implement the column.
        Args:
            value: Value to set for the propagateChanges property.
        """
        self._propagate_changes = value
    
    @property
    def read_only(self,) -> Optional[bool]:
        """
        Gets the readOnly property value. Specifies whether the column values can be modified.
        Returns: Optional[bool]
        """
        return self._read_only
    
    @read_only.setter
    def read_only(self,value: Optional[bool] = None) -> None:
        """
        Sets the readOnly property value. Specifies whether the column values can be modified.
        Args:
            value: Value to set for the readOnly property.
        """
        self._read_only = value
    
    @property
    def required(self,) -> Optional[bool]:
        """
        Gets the required property value. Specifies whether the column value isn't optional.
        Returns: Optional[bool]
        """
        return self._required
    
    @required.setter
    def required(self,value: Optional[bool] = None) -> None:
        """
        Sets the required property value. Specifies whether the column value isn't optional.
        Args:
            value: Value to set for the required property.
        """
        self._required = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("boolean", self.boolean)
        writer.write_object_value("calculated", self.calculated)
        writer.write_object_value("choice", self.choice)
        writer.write_str_value("columnGroup", self.column_group)
        writer.write_object_value("contentApprovalStatus", self.content_approval_status)
        writer.write_object_value("currency", self.currency)
        writer.write_object_value("dateTime", self.date_time)
        writer.write_object_value("defaultValue", self.default_value)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("enforceUniqueValues", self.enforce_unique_values)
        writer.write_object_value("geolocation", self.geolocation)
        writer.write_bool_value("hidden", self.hidden)
        writer.write_object_value("hyperlinkOrPicture", self.hyperlink_or_picture)
        writer.write_bool_value("indexed", self.indexed)
        writer.write_bool_value("isDeletable", self.is_deletable)
        writer.write_bool_value("isReorderable", self.is_reorderable)
        writer.write_bool_value("isSealed", self.is_sealed)
        writer.write_object_value("lookup", self.lookup)
        writer.write_str_value("name", self.name)
        writer.write_object_value("number", self.number)
        writer.write_object_value("personOrGroup", self.person_or_group)
        writer.write_bool_value("propagateChanges", self.propagate_changes)
        writer.write_bool_value("readOnly", self.read_only)
        writer.write_bool_value("required", self.required)
        writer.write_object_value("sourceColumn", self.source_column)
        writer.write_object_value("sourceContentType", self.source_content_type)
        writer.write_object_value("term", self.term)
        writer.write_object_value("text", self.text)
        writer.write_object_value("thumbnail", self.thumbnail)
        writer.write_enum_value("type", self.type)
        writer.write_object_value("validation", self.validation)
    
    @property
    def source_column(self,) -> Optional[ColumnDefinition]:
        """
        Gets the sourceColumn property value. The source column for the content type column.
        Returns: Optional[ColumnDefinition]
        """
        return self._source_column
    
    @source_column.setter
    def source_column(self,value: Optional[ColumnDefinition] = None) -> None:
        """
        Sets the sourceColumn property value. The source column for the content type column.
        Args:
            value: Value to set for the sourceColumn property.
        """
        self._source_column = value
    
    @property
    def source_content_type(self,) -> Optional[content_type_info.ContentTypeInfo]:
        """
        Gets the sourceContentType property value. ContentType from which this column is inherited from. Present only in contentTypes columns response. Read-only.
        Returns: Optional[content_type_info.ContentTypeInfo]
        """
        return self._source_content_type
    
    @source_content_type.setter
    def source_content_type(self,value: Optional[content_type_info.ContentTypeInfo] = None) -> None:
        """
        Sets the sourceContentType property value. ContentType from which this column is inherited from. Present only in contentTypes columns response. Read-only.
        Args:
            value: Value to set for the sourceContentType property.
        """
        self._source_content_type = value
    
    @property
    def term(self,) -> Optional[term_column.TermColumn]:
        """
        Gets the term property value. This column stores taxonomy terms.
        Returns: Optional[term_column.TermColumn]
        """
        return self._term
    
    @term.setter
    def term(self,value: Optional[term_column.TermColumn] = None) -> None:
        """
        Sets the term property value. This column stores taxonomy terms.
        Args:
            value: Value to set for the term property.
        """
        self._term = value
    
    @property
    def text(self,) -> Optional[text_column.TextColumn]:
        """
        Gets the text property value. This column stores text values.
        Returns: Optional[text_column.TextColumn]
        """
        return self._text
    
    @text.setter
    def text(self,value: Optional[text_column.TextColumn] = None) -> None:
        """
        Sets the text property value. This column stores text values.
        Args:
            value: Value to set for the text property.
        """
        self._text = value
    
    @property
    def thumbnail(self,) -> Optional[thumbnail_column.ThumbnailColumn]:
        """
        Gets the thumbnail property value. This column stores thumbnail values.
        Returns: Optional[thumbnail_column.ThumbnailColumn]
        """
        return self._thumbnail
    
    @thumbnail.setter
    def thumbnail(self,value: Optional[thumbnail_column.ThumbnailColumn] = None) -> None:
        """
        Sets the thumbnail property value. This column stores thumbnail values.
        Args:
            value: Value to set for the thumbnail property.
        """
        self._thumbnail = value
    
    @property
    def type(self,) -> Optional[column_types.ColumnTypes]:
        """
        Gets the type property value. For site columns, the type of column. Read-only.
        Returns: Optional[column_types.ColumnTypes]
        """
        return self._type
    
    @type.setter
    def type(self,value: Optional[column_types.ColumnTypes] = None) -> None:
        """
        Sets the type property value. For site columns, the type of column. Read-only.
        Args:
            value: Value to set for the type property.
        """
        self._type = value
    
    @property
    def validation(self,) -> Optional[column_validation.ColumnValidation]:
        """
        Gets the validation property value. This column stores validation formula and message for the column.
        Returns: Optional[column_validation.ColumnValidation]
        """
        return self._validation
    
    @validation.setter
    def validation(self,value: Optional[column_validation.ColumnValidation] = None) -> None:
        """
        Sets the validation property value. This column stores validation formula and message for the column.
        Args:
            value: Value to set for the validation property.
        """
        self._validation = value
    

