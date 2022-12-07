from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

mail_folder = lazy_import('msgraph.generated.models.mail_folder')

class MailSearchFolder(mail_folder.MailFolder):
    def __init__(self,) -> None:
        """
        Instantiates a new MailSearchFolder and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.mailSearchFolder"
        # The OData query to filter the messages.
        self._filter_query: Optional[str] = None
        # Indicates how the mailbox folder hierarchy should be traversed in the search. true means that a deep search should be done to include child folders in the hierarchy of each folder explicitly specified in sourceFolderIds. false means a shallow search of only each of the folders explicitly specified in sourceFolderIds.
        self._include_nested_folders: Optional[bool] = None
        # Indicates whether a search folder is editable using REST APIs.
        self._is_supported: Optional[bool] = None
        # The mailbox folders that should be mined.
        self._source_folder_ids: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MailSearchFolder:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MailSearchFolder
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MailSearchFolder()
    
    @property
    def filter_query(self,) -> Optional[str]:
        """
        Gets the filterQuery property value. The OData query to filter the messages.
        Returns: Optional[str]
        """
        return self._filter_query
    
    @filter_query.setter
    def filter_query(self,value: Optional[str] = None) -> None:
        """
        Sets the filterQuery property value. The OData query to filter the messages.
        Args:
            value: Value to set for the filterQuery property.
        """
        self._filter_query = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "filter_query": lambda n : setattr(self, 'filter_query', n.get_str_value()),
            "include_nested_folders": lambda n : setattr(self, 'include_nested_folders', n.get_bool_value()),
            "is_supported": lambda n : setattr(self, 'is_supported', n.get_bool_value()),
            "source_folder_ids": lambda n : setattr(self, 'source_folder_ids', n.get_collection_of_primitive_values(str)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def include_nested_folders(self,) -> Optional[bool]:
        """
        Gets the includeNestedFolders property value. Indicates how the mailbox folder hierarchy should be traversed in the search. true means that a deep search should be done to include child folders in the hierarchy of each folder explicitly specified in sourceFolderIds. false means a shallow search of only each of the folders explicitly specified in sourceFolderIds.
        Returns: Optional[bool]
        """
        return self._include_nested_folders
    
    @include_nested_folders.setter
    def include_nested_folders(self,value: Optional[bool] = None) -> None:
        """
        Sets the includeNestedFolders property value. Indicates how the mailbox folder hierarchy should be traversed in the search. true means that a deep search should be done to include child folders in the hierarchy of each folder explicitly specified in sourceFolderIds. false means a shallow search of only each of the folders explicitly specified in sourceFolderIds.
        Args:
            value: Value to set for the includeNestedFolders property.
        """
        self._include_nested_folders = value
    
    @property
    def is_supported(self,) -> Optional[bool]:
        """
        Gets the isSupported property value. Indicates whether a search folder is editable using REST APIs.
        Returns: Optional[bool]
        """
        return self._is_supported
    
    @is_supported.setter
    def is_supported(self,value: Optional[bool] = None) -> None:
        """
        Sets the isSupported property value. Indicates whether a search folder is editable using REST APIs.
        Args:
            value: Value to set for the isSupported property.
        """
        self._is_supported = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("filterQuery", self.filter_query)
        writer.write_bool_value("includeNestedFolders", self.include_nested_folders)
        writer.write_bool_value("isSupported", self.is_supported)
        writer.write_collection_of_primitive_values("sourceFolderIds", self.source_folder_ids)
    
    @property
    def source_folder_ids(self,) -> Optional[List[str]]:
        """
        Gets the sourceFolderIds property value. The mailbox folders that should be mined.
        Returns: Optional[List[str]]
        """
        return self._source_folder_ids
    
    @source_folder_ids.setter
    def source_folder_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the sourceFolderIds property value. The mailbox folders that should be mined.
        Args:
            value: Value to set for the sourceFolderIds property.
        """
        self._source_folder_ids = value
    

