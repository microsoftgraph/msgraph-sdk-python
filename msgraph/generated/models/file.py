from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

hashes = lazy_import('msgraph.generated.models.hashes')

class File(AdditionalDataHolder, Parsable):
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
        Instantiates a new file and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Hashes of the file's binary content, if available. Read-only.
        self._hashes: Optional[hashes.Hashes] = None
        # The MIME type for the file. This is determined by logic on the server and might not be the value provided when the file was uploaded. Read-only.
        self._mime_type: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The processingMetadata property
        self._processing_metadata: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> File:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: File
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return File()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "hashes": lambda n : setattr(self, 'hashes', n.get_object_value(hashes.Hashes)),
            "mime_type": lambda n : setattr(self, 'mime_type', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "processing_metadata": lambda n : setattr(self, 'processing_metadata', n.get_bool_value()),
        }
        return fields
    
    @property
    def hashes(self,) -> Optional[hashes.Hashes]:
        """
        Gets the hashes property value. Hashes of the file's binary content, if available. Read-only.
        Returns: Optional[hashes.Hashes]
        """
        return self._hashes
    
    @hashes.setter
    def hashes(self,value: Optional[hashes.Hashes] = None) -> None:
        """
        Sets the hashes property value. Hashes of the file's binary content, if available. Read-only.
        Args:
            value: Value to set for the hashes property.
        """
        self._hashes = value
    
    @property
    def mime_type(self,) -> Optional[str]:
        """
        Gets the mimeType property value. The MIME type for the file. This is determined by logic on the server and might not be the value provided when the file was uploaded. Read-only.
        Returns: Optional[str]
        """
        return self._mime_type
    
    @mime_type.setter
    def mime_type(self,value: Optional[str] = None) -> None:
        """
        Sets the mimeType property value. The MIME type for the file. This is determined by logic on the server and might not be the value provided when the file was uploaded. Read-only.
        Args:
            value: Value to set for the mimeType property.
        """
        self._mime_type = value
    
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
    def processing_metadata(self,) -> Optional[bool]:
        """
        Gets the processingMetadata property value. The processingMetadata property
        Returns: Optional[bool]
        """
        return self._processing_metadata
    
    @processing_metadata.setter
    def processing_metadata(self,value: Optional[bool] = None) -> None:
        """
        Sets the processingMetadata property value. The processingMetadata property
        Args:
            value: Value to set for the processingMetadata property.
        """
        self._processing_metadata = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("hashes", self.hashes)
        writer.write_str_value("mimeType", self.mime_type)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bool_value("processingMetadata", self.processing_metadata)
        writer.write_additional_data_value(self.additional_data)
    

