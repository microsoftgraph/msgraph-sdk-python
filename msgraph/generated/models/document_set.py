from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

column_definition = lazy_import('msgraph.generated.models.column_definition')
content_type_info = lazy_import('msgraph.generated.models.content_type_info')
document_set_content = lazy_import('msgraph.generated.models.document_set_content')

class DocumentSet(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def allowed_content_types(self,) -> Optional[List[content_type_info.ContentTypeInfo]]:
        """
        Gets the allowedContentTypes property value. Content types allowed in document set.
        Returns: Optional[List[content_type_info.ContentTypeInfo]]
        """
        return self._allowed_content_types
    
    @allowed_content_types.setter
    def allowed_content_types(self,value: Optional[List[content_type_info.ContentTypeInfo]] = None) -> None:
        """
        Sets the allowedContentTypes property value. Content types allowed in document set.
        Args:
            value: Value to set for the allowedContentTypes property.
        """
        self._allowed_content_types = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new documentSet and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Content types allowed in document set.
        self._allowed_content_types: Optional[List[content_type_info.ContentTypeInfo]] = None
        # Default contents of document set.
        self._default_contents: Optional[List[document_set_content.DocumentSetContent]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Specifies whether to push welcome page changes to inherited content types.
        self._propagate_welcome_page_changes: Optional[bool] = None
        # The sharedColumns property
        self._shared_columns: Optional[List[column_definition.ColumnDefinition]] = None
        # Indicates whether to add the name of the document set to each file name.
        self._should_prefix_name_to_file: Optional[bool] = None
        # The welcomePageColumns property
        self._welcome_page_columns: Optional[List[column_definition.ColumnDefinition]] = None
        # Welcome page absolute URL.
        self._welcome_page_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DocumentSet:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DocumentSet
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DocumentSet()
    
    @property
    def default_contents(self,) -> Optional[List[document_set_content.DocumentSetContent]]:
        """
        Gets the defaultContents property value. Default contents of document set.
        Returns: Optional[List[document_set_content.DocumentSetContent]]
        """
        return self._default_contents
    
    @default_contents.setter
    def default_contents(self,value: Optional[List[document_set_content.DocumentSetContent]] = None) -> None:
        """
        Sets the defaultContents property value. Default contents of document set.
        Args:
            value: Value to set for the defaultContents property.
        """
        self._default_contents = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "allowed_content_types": lambda n : setattr(self, 'allowed_content_types', n.get_collection_of_object_values(content_type_info.ContentTypeInfo)),
            "default_contents": lambda n : setattr(self, 'default_contents', n.get_collection_of_object_values(document_set_content.DocumentSetContent)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "propagate_welcome_page_changes": lambda n : setattr(self, 'propagate_welcome_page_changes', n.get_bool_value()),
            "shared_columns": lambda n : setattr(self, 'shared_columns', n.get_collection_of_object_values(column_definition.ColumnDefinition)),
            "should_prefix_name_to_file": lambda n : setattr(self, 'should_prefix_name_to_file', n.get_bool_value()),
            "welcome_page_columns": lambda n : setattr(self, 'welcome_page_columns', n.get_collection_of_object_values(column_definition.ColumnDefinition)),
            "welcome_page_url": lambda n : setattr(self, 'welcome_page_url', n.get_str_value()),
        }
        return fields
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def propagate_welcome_page_changes(self,) -> Optional[bool]:
        """
        Gets the propagateWelcomePageChanges property value. Specifies whether to push welcome page changes to inherited content types.
        Returns: Optional[bool]
        """
        return self._propagate_welcome_page_changes
    
    @propagate_welcome_page_changes.setter
    def propagate_welcome_page_changes(self,value: Optional[bool] = None) -> None:
        """
        Sets the propagateWelcomePageChanges property value. Specifies whether to push welcome page changes to inherited content types.
        Args:
            value: Value to set for the propagateWelcomePageChanges property.
        """
        self._propagate_welcome_page_changes = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_object_values("allowedContentTypes", self.allowed_content_types)
        writer.write_collection_of_object_values("defaultContents", self.default_contents)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bool_value("propagateWelcomePageChanges", self.propagate_welcome_page_changes)
        writer.write_collection_of_object_values("sharedColumns", self.shared_columns)
        writer.write_bool_value("shouldPrefixNameToFile", self.should_prefix_name_to_file)
        writer.write_collection_of_object_values("welcomePageColumns", self.welcome_page_columns)
        writer.write_str_value("welcomePageUrl", self.welcome_page_url)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def shared_columns(self,) -> Optional[List[column_definition.ColumnDefinition]]:
        """
        Gets the sharedColumns property value. The sharedColumns property
        Returns: Optional[List[column_definition.ColumnDefinition]]
        """
        return self._shared_columns
    
    @shared_columns.setter
    def shared_columns(self,value: Optional[List[column_definition.ColumnDefinition]] = None) -> None:
        """
        Sets the sharedColumns property value. The sharedColumns property
        Args:
            value: Value to set for the sharedColumns property.
        """
        self._shared_columns = value
    
    @property
    def should_prefix_name_to_file(self,) -> Optional[bool]:
        """
        Gets the shouldPrefixNameToFile property value. Indicates whether to add the name of the document set to each file name.
        Returns: Optional[bool]
        """
        return self._should_prefix_name_to_file
    
    @should_prefix_name_to_file.setter
    def should_prefix_name_to_file(self,value: Optional[bool] = None) -> None:
        """
        Sets the shouldPrefixNameToFile property value. Indicates whether to add the name of the document set to each file name.
        Args:
            value: Value to set for the shouldPrefixNameToFile property.
        """
        self._should_prefix_name_to_file = value
    
    @property
    def welcome_page_columns(self,) -> Optional[List[column_definition.ColumnDefinition]]:
        """
        Gets the welcomePageColumns property value. The welcomePageColumns property
        Returns: Optional[List[column_definition.ColumnDefinition]]
        """
        return self._welcome_page_columns
    
    @welcome_page_columns.setter
    def welcome_page_columns(self,value: Optional[List[column_definition.ColumnDefinition]] = None) -> None:
        """
        Sets the welcomePageColumns property value. The welcomePageColumns property
        Args:
            value: Value to set for the welcomePageColumns property.
        """
        self._welcome_page_columns = value
    
    @property
    def welcome_page_url(self,) -> Optional[str]:
        """
        Gets the welcomePageUrl property value. Welcome page absolute URL.
        Returns: Optional[str]
        """
        return self._welcome_page_url
    
    @welcome_page_url.setter
    def welcome_page_url(self,value: Optional[str] = None) -> None:
        """
        Sets the welcomePageUrl property value. Welcome page absolute URL.
        Args:
            value: Value to set for the welcomePageUrl property.
        """
        self._welcome_page_url = value
    

