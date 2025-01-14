from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .boolean_column import BooleanColumn
    from .calculated_column import CalculatedColumn
    from .choice_column import ChoiceColumn
    from .column_types import ColumnTypes
    from .column_validation import ColumnValidation
    from .content_approval_status_column import ContentApprovalStatusColumn
    from .content_type_info import ContentTypeInfo
    from .currency_column import CurrencyColumn
    from .date_time_column import DateTimeColumn
    from .default_column_value import DefaultColumnValue
    from .entity import Entity
    from .geolocation_column import GeolocationColumn
    from .hyperlink_or_picture_column import HyperlinkOrPictureColumn
    from .lookup_column import LookupColumn
    from .number_column import NumberColumn
    from .person_or_group_column import PersonOrGroupColumn
    from .term_column import TermColumn
    from .text_column import TextColumn
    from .thumbnail_column import ThumbnailColumn

from .entity import Entity

@dataclass
class ColumnDefinition(Entity, Parsable):
    # This column stores Boolean values.
    boolean: Optional[BooleanColumn] = None
    # This column's data is calculated based on other columns.
    calculated: Optional[CalculatedColumn] = None
    # This column stores data from a list of choices.
    choice: Optional[ChoiceColumn] = None
    # For site columns, the name of the group this column belongs to. Helps organize related columns.
    column_group: Optional[str] = None
    # This column stores content approval status.
    content_approval_status: Optional[ContentApprovalStatusColumn] = None
    # This column stores currency values.
    currency: Optional[CurrencyColumn] = None
    # This column stores DateTime values.
    date_time: Optional[DateTimeColumn] = None
    # The default value for this column.
    default_value: Optional[DefaultColumnValue] = None
    # The user-facing description of the column.
    description: Optional[str] = None
    # The user-facing name of the column.
    display_name: Optional[str] = None
    # If true, no two list items may have the same value for this column.
    enforce_unique_values: Optional[bool] = None
    # This column stores a geolocation.
    geolocation: Optional[GeolocationColumn] = None
    # Specifies whether the column is displayed in the user interface.
    hidden: Optional[bool] = None
    # This column stores hyperlink or picture values.
    hyperlink_or_picture: Optional[HyperlinkOrPictureColumn] = None
    # Specifies whether the column values can be used for sorting and searching.
    indexed: Optional[bool] = None
    # Indicates whether this column can be deleted.
    is_deletable: Optional[bool] = None
    # Indicates whether values in the column can be reordered. Read-only.
    is_reorderable: Optional[bool] = None
    # Specifies whether the column can be changed.
    is_sealed: Optional[bool] = None
    # This column's data is looked up from another source in the site.
    lookup: Optional[LookupColumn] = None
    # The API-facing name of the column as it appears in the fields on a listItem. For the user-facing name, see displayName.
    name: Optional[str] = None
    # This column stores number values.
    number: Optional[NumberColumn] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # This column stores Person or Group values.
    person_or_group: Optional[PersonOrGroupColumn] = None
    # If 'true', changes to this column will be propagated to lists that implement the column.
    propagate_changes: Optional[bool] = None
    # Specifies whether the column values can be modified.
    read_only: Optional[bool] = None
    # Specifies whether the column value isn't optional.
    required: Optional[bool] = None
    # The source column for the content type column.
    source_column: Optional[ColumnDefinition] = None
    # ContentType from which this column is inherited from. Present only in contentTypes columns response. Read-only.
    source_content_type: Optional[ContentTypeInfo] = None
    # This column stores taxonomy terms.
    term: Optional[TermColumn] = None
    # This column stores text values.
    text: Optional[TextColumn] = None
    # This column stores thumbnail values.
    thumbnail: Optional[ThumbnailColumn] = None
    # For site columns, the type of column. Read-only.
    type: Optional[ColumnTypes] = None
    # This column stores validation formula and message for the column.
    validation: Optional[ColumnValidation] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ColumnDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ColumnDefinition
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ColumnDefinition()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .boolean_column import BooleanColumn
        from .calculated_column import CalculatedColumn
        from .choice_column import ChoiceColumn
        from .column_types import ColumnTypes
        from .column_validation import ColumnValidation
        from .content_approval_status_column import ContentApprovalStatusColumn
        from .content_type_info import ContentTypeInfo
        from .currency_column import CurrencyColumn
        from .date_time_column import DateTimeColumn
        from .default_column_value import DefaultColumnValue
        from .entity import Entity
        from .geolocation_column import GeolocationColumn
        from .hyperlink_or_picture_column import HyperlinkOrPictureColumn
        from .lookup_column import LookupColumn
        from .number_column import NumberColumn
        from .person_or_group_column import PersonOrGroupColumn
        from .term_column import TermColumn
        from .text_column import TextColumn
        from .thumbnail_column import ThumbnailColumn

        from .boolean_column import BooleanColumn
        from .calculated_column import CalculatedColumn
        from .choice_column import ChoiceColumn
        from .column_types import ColumnTypes
        from .column_validation import ColumnValidation
        from .content_approval_status_column import ContentApprovalStatusColumn
        from .content_type_info import ContentTypeInfo
        from .currency_column import CurrencyColumn
        from .date_time_column import DateTimeColumn
        from .default_column_value import DefaultColumnValue
        from .entity import Entity
        from .geolocation_column import GeolocationColumn
        from .hyperlink_or_picture_column import HyperlinkOrPictureColumn
        from .lookup_column import LookupColumn
        from .number_column import NumberColumn
        from .person_or_group_column import PersonOrGroupColumn
        from .term_column import TermColumn
        from .text_column import TextColumn
        from .thumbnail_column import ThumbnailColumn

        fields: dict[str, Callable[[Any], None]] = {
            "boolean": lambda n : setattr(self, 'boolean', n.get_object_value(BooleanColumn)),
            "calculated": lambda n : setattr(self, 'calculated', n.get_object_value(CalculatedColumn)),
            "choice": lambda n : setattr(self, 'choice', n.get_object_value(ChoiceColumn)),
            "columnGroup": lambda n : setattr(self, 'column_group', n.get_str_value()),
            "contentApprovalStatus": lambda n : setattr(self, 'content_approval_status', n.get_object_value(ContentApprovalStatusColumn)),
            "currency": lambda n : setattr(self, 'currency', n.get_object_value(CurrencyColumn)),
            "dateTime": lambda n : setattr(self, 'date_time', n.get_object_value(DateTimeColumn)),
            "defaultValue": lambda n : setattr(self, 'default_value', n.get_object_value(DefaultColumnValue)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "enforceUniqueValues": lambda n : setattr(self, 'enforce_unique_values', n.get_bool_value()),
            "geolocation": lambda n : setattr(self, 'geolocation', n.get_object_value(GeolocationColumn)),
            "hidden": lambda n : setattr(self, 'hidden', n.get_bool_value()),
            "hyperlinkOrPicture": lambda n : setattr(self, 'hyperlink_or_picture', n.get_object_value(HyperlinkOrPictureColumn)),
            "indexed": lambda n : setattr(self, 'indexed', n.get_bool_value()),
            "isDeletable": lambda n : setattr(self, 'is_deletable', n.get_bool_value()),
            "isReorderable": lambda n : setattr(self, 'is_reorderable', n.get_bool_value()),
            "isSealed": lambda n : setattr(self, 'is_sealed', n.get_bool_value()),
            "lookup": lambda n : setattr(self, 'lookup', n.get_object_value(LookupColumn)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "number": lambda n : setattr(self, 'number', n.get_object_value(NumberColumn)),
            "personOrGroup": lambda n : setattr(self, 'person_or_group', n.get_object_value(PersonOrGroupColumn)),
            "propagateChanges": lambda n : setattr(self, 'propagate_changes', n.get_bool_value()),
            "readOnly": lambda n : setattr(self, 'read_only', n.get_bool_value()),
            "required": lambda n : setattr(self, 'required', n.get_bool_value()),
            "sourceColumn": lambda n : setattr(self, 'source_column', n.get_object_value(ColumnDefinition)),
            "sourceContentType": lambda n : setattr(self, 'source_content_type', n.get_object_value(ContentTypeInfo)),
            "term": lambda n : setattr(self, 'term', n.get_object_value(TermColumn)),
            "text": lambda n : setattr(self, 'text', n.get_object_value(TextColumn)),
            "thumbnail": lambda n : setattr(self, 'thumbnail', n.get_object_value(ThumbnailColumn)),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(ColumnTypes)),
            "validation": lambda n : setattr(self, 'validation', n.get_object_value(ColumnValidation)),
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
    

