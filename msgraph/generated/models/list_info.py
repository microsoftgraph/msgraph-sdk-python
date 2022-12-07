from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class ListInfo(AdditionalDataHolder, Parsable):
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new listInfo and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # If true, indicates that content types are enabled for this list.
        self._content_types_enabled: Optional[bool] = None
        # If true, indicates that the list is not normally visible in the SharePoint user experience.
        self._hidden: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # An enumerated value that represents the base list template used in creating the list. Possible values include documentLibrary, genericList, task, survey, announcements, contacts, and more.
        self._template: Optional[str] = None
    
    @property
    def content_types_enabled(self,) -> Optional[bool]:
        """
        Gets the contentTypesEnabled property value. If true, indicates that content types are enabled for this list.
        Returns: Optional[bool]
        """
        return self._content_types_enabled
    
    @content_types_enabled.setter
    def content_types_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the contentTypesEnabled property value. If true, indicates that content types are enabled for this list.
        Args:
            value: Value to set for the contentTypesEnabled property.
        """
        self._content_types_enabled = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ListInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ListInfo
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ListInfo()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "content_types_enabled": lambda n : setattr(self, 'content_types_enabled', n.get_bool_value()),
            "hidden": lambda n : setattr(self, 'hidden', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "template": lambda n : setattr(self, 'template', n.get_str_value()),
        }
        return fields
    
    @property
    def hidden(self,) -> Optional[bool]:
        """
        Gets the hidden property value. If true, indicates that the list is not normally visible in the SharePoint user experience.
        Returns: Optional[bool]
        """
        return self._hidden
    
    @hidden.setter
    def hidden(self,value: Optional[bool] = None) -> None:
        """
        Sets the hidden property value. If true, indicates that the list is not normally visible in the SharePoint user experience.
        Args:
            value: Value to set for the hidden property.
        """
        self._hidden = value
    
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_bool_value("contentTypesEnabled", self.content_types_enabled)
        writer.write_bool_value("hidden", self.hidden)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("template", self.template)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def template(self,) -> Optional[str]:
        """
        Gets the template property value. An enumerated value that represents the base list template used in creating the list. Possible values include documentLibrary, genericList, task, survey, announcements, contacts, and more.
        Returns: Optional[str]
        """
        return self._template
    
    @template.setter
    def template(self,value: Optional[str] = None) -> None:
        """
        Sets the template property value. An enumerated value that represents the base list template used in creating the list. Possible values include documentLibrary, genericList, task, survey, announcements, contacts, and more.
        Args:
            value: Value to set for the template property.
        """
        self._template = value
    

