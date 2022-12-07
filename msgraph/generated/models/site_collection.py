from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

root = lazy_import('msgraph.generated.models.root')

class SiteCollection(AdditionalDataHolder, Parsable):
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
        Instantiates a new siteCollection and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The geographic region code for where this site collection resides. Read-only.
        self._data_location_code: Optional[str] = None
        # The hostname for the site collection. Read-only.
        self._hostname: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # If present, indicates that this is a root site collection in SharePoint. Read-only.
        self._root: Optional[root.Root] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SiteCollection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SiteCollection
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SiteCollection()
    
    @property
    def data_location_code(self,) -> Optional[str]:
        """
        Gets the dataLocationCode property value. The geographic region code for where this site collection resides. Read-only.
        Returns: Optional[str]
        """
        return self._data_location_code
    
    @data_location_code.setter
    def data_location_code(self,value: Optional[str] = None) -> None:
        """
        Sets the dataLocationCode property value. The geographic region code for where this site collection resides. Read-only.
        Args:
            value: Value to set for the dataLocationCode property.
        """
        self._data_location_code = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "data_location_code": lambda n : setattr(self, 'data_location_code', n.get_str_value()),
            "hostname": lambda n : setattr(self, 'hostname', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "root": lambda n : setattr(self, 'root', n.get_object_value(root.Root)),
        }
        return fields
    
    @property
    def hostname(self,) -> Optional[str]:
        """
        Gets the hostname property value. The hostname for the site collection. Read-only.
        Returns: Optional[str]
        """
        return self._hostname
    
    @hostname.setter
    def hostname(self,value: Optional[str] = None) -> None:
        """
        Sets the hostname property value. The hostname for the site collection. Read-only.
        Args:
            value: Value to set for the hostname property.
        """
        self._hostname = value
    
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
    def root(self,) -> Optional[root.Root]:
        """
        Gets the root property value. If present, indicates that this is a root site collection in SharePoint. Read-only.
        Returns: Optional[root.Root]
        """
        return self._root
    
    @root.setter
    def root(self,value: Optional[root.Root] = None) -> None:
        """
        Sets the root property value. If present, indicates that this is a root site collection in SharePoint. Read-only.
        Args:
            value: Value to set for the root property.
        """
        self._root = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("dataLocationCode", self.data_location_code)
        writer.write_str_value("hostname", self.hostname)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("root", self.root)
        writer.write_additional_data_value(self.additional_data)
    

