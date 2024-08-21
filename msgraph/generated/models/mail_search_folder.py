from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .mail_folder import MailFolder

from .mail_folder import MailFolder

@dataclass
class MailSearchFolder(MailFolder):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.mailSearchFolder"
    # The OData query to filter the messages.
    filter_query: Optional[str] = None
    # Indicates how the mailbox folder hierarchy should be traversed in the search. true means that a deep search should be done to include child folders in the hierarchy of each folder explicitly specified in sourceFolderIds. false means a shallow search of only each of the folders explicitly specified in sourceFolderIds.
    include_nested_folders: Optional[bool] = None
    # Indicates whether a search folder is editable using REST APIs.
    is_supported: Optional[bool] = None
    # The mailbox folders that should be mined.
    source_folder_ids: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MailSearchFolder:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MailSearchFolder
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MailSearchFolder()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .mail_folder import MailFolder

        from .mail_folder import MailFolder

        fields: Dict[str, Callable[[Any], None]] = {
            "filterQuery": lambda n : setattr(self, 'filter_query', n.get_str_value()),
            "includeNestedFolders": lambda n : setattr(self, 'include_nested_folders', n.get_bool_value()),
            "isSupported": lambda n : setattr(self, 'is_supported', n.get_bool_value()),
            "sourceFolderIds": lambda n : setattr(self, 'source_folder_ids', n.get_collection_of_primitive_values(str)),
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
        writer.write_str_value("filterQuery", self.filter_query)
        writer.write_bool_value("includeNestedFolders", self.include_nested_folders)
        writer.write_bool_value("isSupported", self.is_supported)
        writer.write_collection_of_primitive_values("sourceFolderIds", self.source_folder_ids)
    

