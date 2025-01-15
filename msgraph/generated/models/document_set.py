from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .column_definition import ColumnDefinition
    from .content_type_info import ContentTypeInfo
    from .document_set_content import DocumentSetContent

@dataclass
class DocumentSet(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Content types allowed in document set.
    allowed_content_types: Optional[list[ContentTypeInfo]] = None
    # Default contents of document set.
    default_contents: Optional[list[DocumentSetContent]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Specifies whether to push welcome page changes to inherited content types.
    propagate_welcome_page_changes: Optional[bool] = None
    # The sharedColumns property
    shared_columns: Optional[list[ColumnDefinition]] = None
    # Indicates whether to add the name of the document set to each file name.
    should_prefix_name_to_file: Optional[bool] = None
    # The welcomePageColumns property
    welcome_page_columns: Optional[list[ColumnDefinition]] = None
    # Welcome page absolute URL.
    welcome_page_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DocumentSet:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DocumentSet
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DocumentSet()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .column_definition import ColumnDefinition
        from .content_type_info import ContentTypeInfo
        from .document_set_content import DocumentSetContent

        from .column_definition import ColumnDefinition
        from .content_type_info import ContentTypeInfo
        from .document_set_content import DocumentSetContent

        fields: dict[str, Callable[[Any], None]] = {
            "allowedContentTypes": lambda n : setattr(self, 'allowed_content_types', n.get_collection_of_object_values(ContentTypeInfo)),
            "defaultContents": lambda n : setattr(self, 'default_contents', n.get_collection_of_object_values(DocumentSetContent)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "propagateWelcomePageChanges": lambda n : setattr(self, 'propagate_welcome_page_changes', n.get_bool_value()),
            "sharedColumns": lambda n : setattr(self, 'shared_columns', n.get_collection_of_object_values(ColumnDefinition)),
            "shouldPrefixNameToFile": lambda n : setattr(self, 'should_prefix_name_to_file', n.get_bool_value()),
            "welcomePageColumns": lambda n : setattr(self, 'welcome_page_columns', n.get_collection_of_object_values(ColumnDefinition)),
            "welcomePageUrl": lambda n : setattr(self, 'welcome_page_url', n.get_str_value()),
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
        writer.write_collection_of_object_values("allowedContentTypes", self.allowed_content_types)
        writer.write_collection_of_object_values("defaultContents", self.default_contents)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bool_value("propagateWelcomePageChanges", self.propagate_welcome_page_changes)
        writer.write_collection_of_object_values("sharedColumns", self.shared_columns)
        writer.write_bool_value("shouldPrefixNameToFile", self.should_prefix_name_to_file)
        writer.write_collection_of_object_values("welcomePageColumns", self.welcome_page_columns)
        writer.write_str_value("welcomePageUrl", self.welcome_page_url)
        writer.write_additional_data_value(self.additional_data)
    

