from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

external_link = lazy_import('msgraph.generated.models.external_link')

class NotebookLinks(AdditionalDataHolder, Parsable):
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
        Instantiates a new notebookLinks and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # Opens the notebook in the OneNote native client if it's installed.
        self._one_note_client_url: Optional[external_link.ExternalLink] = None
        # Opens the notebook in OneNote on the web.
        self._one_note_web_url: Optional[external_link.ExternalLink] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> NotebookLinks:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: NotebookLinks
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return NotebookLinks()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "one_note_client_url": lambda n : setattr(self, 'one_note_client_url', n.get_object_value(external_link.ExternalLink)),
            "one_note_web_url": lambda n : setattr(self, 'one_note_web_url', n.get_object_value(external_link.ExternalLink)),
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
    def one_note_client_url(self,) -> Optional[external_link.ExternalLink]:
        """
        Gets the oneNoteClientUrl property value. Opens the notebook in the OneNote native client if it's installed.
        Returns: Optional[external_link.ExternalLink]
        """
        return self._one_note_client_url
    
    @one_note_client_url.setter
    def one_note_client_url(self,value: Optional[external_link.ExternalLink] = None) -> None:
        """
        Sets the oneNoteClientUrl property value. Opens the notebook in the OneNote native client if it's installed.
        Args:
            value: Value to set for the oneNoteClientUrl property.
        """
        self._one_note_client_url = value
    
    @property
    def one_note_web_url(self,) -> Optional[external_link.ExternalLink]:
        """
        Gets the oneNoteWebUrl property value. Opens the notebook in OneNote on the web.
        Returns: Optional[external_link.ExternalLink]
        """
        return self._one_note_web_url
    
    @one_note_web_url.setter
    def one_note_web_url(self,value: Optional[external_link.ExternalLink] = None) -> None:
        """
        Sets the oneNoteWebUrl property value. Opens the notebook in OneNote on the web.
        Args:
            value: Value to set for the oneNoteWebUrl property.
        """
        self._one_note_web_url = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("oneNoteClientUrl", self.one_note_client_url)
        writer.write_object_value("oneNoteWebUrl", self.one_note_web_url)
        writer.write_additional_data_value(self.additional_data)
    

