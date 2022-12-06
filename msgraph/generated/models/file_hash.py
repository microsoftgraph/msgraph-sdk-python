from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

file_hash_type = lazy_import('msgraph.generated.models.file_hash_type')

class FileHash(AdditionalDataHolder, Parsable):
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
        Instantiates a new fileHash and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # File hash type. Possible values are: unknown, sha1, sha256, md5, authenticodeHash256, lsHash, ctph, peSha1, peSha256.
        self._hash_type: Optional[file_hash_type.FileHashType] = None
        # Value of the file hash.
        self._hash_value: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> FileHash:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: FileHash
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return FileHash()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "hash_type": lambda n : setattr(self, 'hash_type', n.get_enum_value(file_hash_type.FileHashType)),
            "hash_value": lambda n : setattr(self, 'hash_value', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def hash_type(self,) -> Optional[file_hash_type.FileHashType]:
        """
        Gets the hashType property value. File hash type. Possible values are: unknown, sha1, sha256, md5, authenticodeHash256, lsHash, ctph, peSha1, peSha256.
        Returns: Optional[file_hash_type.FileHashType]
        """
        return self._hash_type
    
    @hash_type.setter
    def hash_type(self,value: Optional[file_hash_type.FileHashType] = None) -> None:
        """
        Sets the hashType property value. File hash type. Possible values are: unknown, sha1, sha256, md5, authenticodeHash256, lsHash, ctph, peSha1, peSha256.
        Args:
            value: Value to set for the hashType property.
        """
        self._hash_type = value
    
    @property
    def hash_value(self,) -> Optional[str]:
        """
        Gets the hashValue property value. Value of the file hash.
        Returns: Optional[str]
        """
        return self._hash_value
    
    @hash_value.setter
    def hash_value(self,value: Optional[str] = None) -> None:
        """
        Sets the hashValue property value. Value of the file hash.
        Args:
            value: Value to set for the hashValue property.
        """
        self._hash_value = value
    
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
        writer.write_enum_value("hashType", self.hash_type)
        writer.write_str_value("hashValue", self.hash_value)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

