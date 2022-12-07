from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

ios_home_screen_app = lazy_import('msgraph.generated.models.ios_home_screen_app')

class IosHomeScreenFolderPage(AdditionalDataHolder, Parsable):
    """
    A page for a folder containing apps and web clips on the Home Screen.
    """
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
    def apps(self,) -> Optional[List[ios_home_screen_app.IosHomeScreenApp]]:
        """
        Gets the apps property value. A list of apps and web clips to appear on a page within a folder. This collection can contain a maximum of 500 elements.
        Returns: Optional[List[ios_home_screen_app.IosHomeScreenApp]]
        """
        return self._apps
    
    @apps.setter
    def apps(self,value: Optional[List[ios_home_screen_app.IosHomeScreenApp]] = None) -> None:
        """
        Sets the apps property value. A list of apps and web clips to appear on a page within a folder. This collection can contain a maximum of 500 elements.
        Args:
            value: Value to set for the apps property.
        """
        self._apps = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new iosHomeScreenFolderPage and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # A list of apps and web clips to appear on a page within a folder. This collection can contain a maximum of 500 elements.
        self._apps: Optional[List[ios_home_screen_app.IosHomeScreenApp]] = None
        # Name of the folder page
        self._display_name: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IosHomeScreenFolderPage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IosHomeScreenFolderPage
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IosHomeScreenFolderPage()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Name of the folder page
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Name of the folder page
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "apps": lambda n : setattr(self, 'apps', n.get_collection_of_object_values(ios_home_screen_app.IosHomeScreenApp)),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_object_values("apps", self.apps)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

