from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

identity = lazy_import('msgraph.generated.models.identity')

class SharingLink(AdditionalDataHolder, Parsable):
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
    def application(self,) -> Optional[identity.Identity]:
        """
        Gets the application property value. The app the link is associated with.
        Returns: Optional[identity.Identity]
        """
        return self._application
    
    @application.setter
    def application(self,value: Optional[identity.Identity] = None) -> None:
        """
        Sets the application property value. The app the link is associated with.
        Args:
            value: Value to set for the application property.
        """
        self._application = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new sharingLink and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The app the link is associated with.
        self._application: Optional[identity.Identity] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # If true then the user can only use this link to view the item on the web, and cannot use it to download the contents of the item. Only for OneDrive for Business and SharePoint.
        self._prevents_download: Optional[bool] = None
        # The scope of the link represented by this permission. Value anonymous indicates the link is usable by anyone, organization indicates the link is only usable for users signed into the same tenant.
        self._scope: Optional[str] = None
        # The type of the link created.
        self._type: Optional[str] = None
        # For embed links, this property contains the HTML code for an <iframe> element that will embed the item in a webpage.
        self._web_html: Optional[str] = None
        # A URL that opens the item in the browser on the OneDrive website.
        self._web_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SharingLink:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SharingLink
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SharingLink()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "application": lambda n : setattr(self, 'application', n.get_object_value(identity.Identity)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "prevents_download": lambda n : setattr(self, 'prevents_download', n.get_bool_value()),
            "scope": lambda n : setattr(self, 'scope', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
            "web_html": lambda n : setattr(self, 'web_html', n.get_str_value()),
            "web_url": lambda n : setattr(self, 'web_url', n.get_str_value()),
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
    def prevents_download(self,) -> Optional[bool]:
        """
        Gets the preventsDownload property value. If true then the user can only use this link to view the item on the web, and cannot use it to download the contents of the item. Only for OneDrive for Business and SharePoint.
        Returns: Optional[bool]
        """
        return self._prevents_download
    
    @prevents_download.setter
    def prevents_download(self,value: Optional[bool] = None) -> None:
        """
        Sets the preventsDownload property value. If true then the user can only use this link to view the item on the web, and cannot use it to download the contents of the item. Only for OneDrive for Business and SharePoint.
        Args:
            value: Value to set for the preventsDownload property.
        """
        self._prevents_download = value
    
    @property
    def scope(self,) -> Optional[str]:
        """
        Gets the scope property value. The scope of the link represented by this permission. Value anonymous indicates the link is usable by anyone, organization indicates the link is only usable for users signed into the same tenant.
        Returns: Optional[str]
        """
        return self._scope
    
    @scope.setter
    def scope(self,value: Optional[str] = None) -> None:
        """
        Sets the scope property value. The scope of the link represented by this permission. Value anonymous indicates the link is usable by anyone, organization indicates the link is only usable for users signed into the same tenant.
        Args:
            value: Value to set for the scope property.
        """
        self._scope = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("application", self.application)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bool_value("preventsDownload", self.prevents_download)
        writer.write_str_value("scope", self.scope)
        writer.write_str_value("type", self.type)
        writer.write_str_value("webHtml", self.web_html)
        writer.write_str_value("webUrl", self.web_url)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def type(self,) -> Optional[str]:
        """
        Gets the type property value. The type of the link created.
        Returns: Optional[str]
        """
        return self._type
    
    @type.setter
    def type(self,value: Optional[str] = None) -> None:
        """
        Sets the type property value. The type of the link created.
        Args:
            value: Value to set for the type property.
        """
        self._type = value
    
    @property
    def web_html(self,) -> Optional[str]:
        """
        Gets the webHtml property value. For embed links, this property contains the HTML code for an <iframe> element that will embed the item in a webpage.
        Returns: Optional[str]
        """
        return self._web_html
    
    @web_html.setter
    def web_html(self,value: Optional[str] = None) -> None:
        """
        Sets the webHtml property value. For embed links, this property contains the HTML code for an <iframe> element that will embed the item in a webpage.
        Args:
            value: Value to set for the webHtml property.
        """
        self._web_html = value
    
    @property
    def web_url(self,) -> Optional[str]:
        """
        Gets the webUrl property value. A URL that opens the item in the browser on the OneDrive website.
        Returns: Optional[str]
        """
        return self._web_url
    
    @web_url.setter
    def web_url(self,value: Optional[str] = None) -> None:
        """
        Sets the webUrl property value. A URL that opens the item in the browser on the OneDrive website.
        Args:
            value: Value to set for the webUrl property.
        """
        self._web_url = value
    

