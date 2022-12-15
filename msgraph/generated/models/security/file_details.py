from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class FileDetails(AdditionalDataHolder, Parsable):
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
        Instantiates a new fileDetails and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The name of the file.
        self._file_name: Optional[str] = None
        # The file path (location) of the file instance.
        self._file_path: Optional[str] = None
        # The publisher of the file.
        self._file_publisher: Optional[str] = None
        # The size of the file in bytes.
        self._file_size: Optional[int] = None
        # The certificate authority (CA) that issued the certificate.
        self._issuer: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The Sha1 cryptographic hash of the file content.
        self._sha1: Optional[str] = None
        # The Sha256 cryptographic hash of the file content.
        self._sha256: Optional[str] = None
        # The signer of the signed file.
        self._signer: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> FileDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: FileDetails
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return FileDetails()
    
    @property
    def file_name(self,) -> Optional[str]:
        """
        Gets the fileName property value. The name of the file.
        Returns: Optional[str]
        """
        return self._file_name
    
    @file_name.setter
    def file_name(self,value: Optional[str] = None) -> None:
        """
        Sets the fileName property value. The name of the file.
        Args:
            value: Value to set for the fileName property.
        """
        self._file_name = value
    
    @property
    def file_path(self,) -> Optional[str]:
        """
        Gets the filePath property value. The file path (location) of the file instance.
        Returns: Optional[str]
        """
        return self._file_path
    
    @file_path.setter
    def file_path(self,value: Optional[str] = None) -> None:
        """
        Sets the filePath property value. The file path (location) of the file instance.
        Args:
            value: Value to set for the filePath property.
        """
        self._file_path = value
    
    @property
    def file_publisher(self,) -> Optional[str]:
        """
        Gets the filePublisher property value. The publisher of the file.
        Returns: Optional[str]
        """
        return self._file_publisher
    
    @file_publisher.setter
    def file_publisher(self,value: Optional[str] = None) -> None:
        """
        Sets the filePublisher property value. The publisher of the file.
        Args:
            value: Value to set for the filePublisher property.
        """
        self._file_publisher = value
    
    @property
    def file_size(self,) -> Optional[int]:
        """
        Gets the fileSize property value. The size of the file in bytes.
        Returns: Optional[int]
        """
        return self._file_size
    
    @file_size.setter
    def file_size(self,value: Optional[int] = None) -> None:
        """
        Sets the fileSize property value. The size of the file in bytes.
        Args:
            value: Value to set for the fileSize property.
        """
        self._file_size = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "file_name": lambda n : setattr(self, 'file_name', n.get_str_value()),
            "file_path": lambda n : setattr(self, 'file_path', n.get_str_value()),
            "file_publisher": lambda n : setattr(self, 'file_publisher', n.get_str_value()),
            "file_size": lambda n : setattr(self, 'file_size', n.get_int_value()),
            "issuer": lambda n : setattr(self, 'issuer', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "sha1": lambda n : setattr(self, 'sha1', n.get_str_value()),
            "sha256": lambda n : setattr(self, 'sha256', n.get_str_value()),
            "signer": lambda n : setattr(self, 'signer', n.get_str_value()),
        }
        return fields
    
    @property
    def issuer(self,) -> Optional[str]:
        """
        Gets the issuer property value. The certificate authority (CA) that issued the certificate.
        Returns: Optional[str]
        """
        return self._issuer
    
    @issuer.setter
    def issuer(self,value: Optional[str] = None) -> None:
        """
        Sets the issuer property value. The certificate authority (CA) that issued the certificate.
        Args:
            value: Value to set for the issuer property.
        """
        self._issuer = value
    
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
        writer.write_str_value("fileName", self.file_name)
        writer.write_str_value("filePath", self.file_path)
        writer.write_str_value("filePublisher", self.file_publisher)
        writer.write_int_value("fileSize", self.file_size)
        writer.write_str_value("issuer", self.issuer)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("sha1", self.sha1)
        writer.write_str_value("sha256", self.sha256)
        writer.write_str_value("signer", self.signer)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def sha1(self,) -> Optional[str]:
        """
        Gets the sha1 property value. The Sha1 cryptographic hash of the file content.
        Returns: Optional[str]
        """
        return self._sha1
    
    @sha1.setter
    def sha1(self,value: Optional[str] = None) -> None:
        """
        Sets the sha1 property value. The Sha1 cryptographic hash of the file content.
        Args:
            value: Value to set for the sha1 property.
        """
        self._sha1 = value
    
    @property
    def sha256(self,) -> Optional[str]:
        """
        Gets the sha256 property value. The Sha256 cryptographic hash of the file content.
        Returns: Optional[str]
        """
        return self._sha256
    
    @sha256.setter
    def sha256(self,value: Optional[str] = None) -> None:
        """
        Sets the sha256 property value. The Sha256 cryptographic hash of the file content.
        Args:
            value: Value to set for the sha256 property.
        """
        self._sha256 = value
    
    @property
    def signer(self,) -> Optional[str]:
        """
        Gets the signer property value. The signer of the signed file.
        Returns: Optional[str]
        """
        return self._signer
    
    @signer.setter
    def signer(self,value: Optional[str] = None) -> None:
        """
        Sets the signer property value. The signer of the signed file.
        Args:
            value: Value to set for the signer property.
        """
        self._signer = value
    

