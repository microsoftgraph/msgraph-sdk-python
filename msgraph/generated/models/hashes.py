from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class Hashes(AdditionalDataHolder, Parsable):
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
        Instantiates a new hashes and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The CRC32 value of the file in little endian (if available). Read-only.
        self._crc32_hash: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # A proprietary hash of the file that can be used to determine if the contents of the file have changed (if available). Read-only.
        self._quick_xor_hash: Optional[str] = None
        # SHA1 hash for the contents of the file (if available). Read-only.
        self._sha1_hash: Optional[str] = None
        # SHA256 hash for the contents of the file (if available). Read-only.
        self._sha256_hash: Optional[str] = None
    
    @property
    def crc32_hash(self,) -> Optional[str]:
        """
        Gets the crc32Hash property value. The CRC32 value of the file in little endian (if available). Read-only.
        Returns: Optional[str]
        """
        return self._crc32_hash
    
    @crc32_hash.setter
    def crc32_hash(self,value: Optional[str] = None) -> None:
        """
        Sets the crc32Hash property value. The CRC32 value of the file in little endian (if available). Read-only.
        Args:
            value: Value to set for the crc32Hash property.
        """
        self._crc32_hash = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Hashes:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Hashes
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Hashes()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "crc32_hash": lambda n : setattr(self, 'crc32_hash', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "quick_xor_hash": lambda n : setattr(self, 'quick_xor_hash', n.get_str_value()),
            "sha1_hash": lambda n : setattr(self, 'sha1_hash', n.get_str_value()),
            "sha256_hash": lambda n : setattr(self, 'sha256_hash', n.get_str_value()),
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
    def quick_xor_hash(self,) -> Optional[str]:
        """
        Gets the quickXorHash property value. A proprietary hash of the file that can be used to determine if the contents of the file have changed (if available). Read-only.
        Returns: Optional[str]
        """
        return self._quick_xor_hash
    
    @quick_xor_hash.setter
    def quick_xor_hash(self,value: Optional[str] = None) -> None:
        """
        Sets the quickXorHash property value. A proprietary hash of the file that can be used to determine if the contents of the file have changed (if available). Read-only.
        Args:
            value: Value to set for the quickXorHash property.
        """
        self._quick_xor_hash = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("crc32Hash", self.crc32_hash)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("quickXorHash", self.quick_xor_hash)
        writer.write_str_value("sha1Hash", self.sha1_hash)
        writer.write_str_value("sha256Hash", self.sha256_hash)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def sha1_hash(self,) -> Optional[str]:
        """
        Gets the sha1Hash property value. SHA1 hash for the contents of the file (if available). Read-only.
        Returns: Optional[str]
        """
        return self._sha1_hash
    
    @sha1_hash.setter
    def sha1_hash(self,value: Optional[str] = None) -> None:
        """
        Sets the sha1Hash property value. SHA1 hash for the contents of the file (if available). Read-only.
        Args:
            value: Value to set for the sha1Hash property.
        """
        self._sha1_hash = value
    
    @property
    def sha256_hash(self,) -> Optional[str]:
        """
        Gets the sha256Hash property value. SHA256 hash for the contents of the file (if available). Read-only.
        Returns: Optional[str]
        """
        return self._sha256_hash
    
    @sha256_hash.setter
    def sha256_hash(self,value: Optional[str] = None) -> None:
        """
        Sets the sha256Hash property value. SHA256 hash for the contents of the file (if available). Read-only.
        Args:
            value: Value to set for the sha256Hash property.
        """
        self._sha256_hash = value
    

