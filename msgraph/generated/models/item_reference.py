from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

sharepoint_ids = lazy_import('msgraph.generated.models.sharepoint_ids')

class ItemReference(AdditionalDataHolder, Parsable):
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
        Instantiates a new itemReference and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Unique identifier of the drive instance that contains the item. Read-only.
        self._drive_id: Optional[str] = None
        # Identifies the type of drive. See [drive][] resource for values.
        self._drive_type: Optional[str] = None
        # Unique identifier of the item in the drive. Read-only.
        self._id: Optional[str] = None
        # The name of the item being referenced. Read-only.
        self._name: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Path that can be used to navigate to the item. Read-only.
        self._path: Optional[str] = None
        # A unique identifier for a shared resource that can be accessed via the [Shares][] API.
        self._share_id: Optional[str] = None
        # Returns identifiers useful for SharePoint REST compatibility. Read-only.
        self._sharepoint_ids: Optional[sharepoint_ids.SharepointIds] = None
        # For OneDrive for Business and SharePoint, this property represents the ID of the site that contains the parent document library of the driveItem resource. The value is the same as the id property of that [site][] resource. It is an opaque string that consists of three identifiers of the site. For OneDrive, this property is not populated.
        self._site_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ItemReference:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ItemReference
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ItemReference()
    
    @property
    def drive_id(self,) -> Optional[str]:
        """
        Gets the driveId property value. Unique identifier of the drive instance that contains the item. Read-only.
        Returns: Optional[str]
        """
        return self._drive_id
    
    @drive_id.setter
    def drive_id(self,value: Optional[str] = None) -> None:
        """
        Sets the driveId property value. Unique identifier of the drive instance that contains the item. Read-only.
        Args:
            value: Value to set for the driveId property.
        """
        self._drive_id = value
    
    @property
    def drive_type(self,) -> Optional[str]:
        """
        Gets the driveType property value. Identifies the type of drive. See [drive][] resource for values.
        Returns: Optional[str]
        """
        return self._drive_type
    
    @drive_type.setter
    def drive_type(self,value: Optional[str] = None) -> None:
        """
        Sets the driveType property value. Identifies the type of drive. See [drive][] resource for values.
        Args:
            value: Value to set for the driveType property.
        """
        self._drive_type = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "drive_id": lambda n : setattr(self, 'drive_id', n.get_str_value()),
            "drive_type": lambda n : setattr(self, 'drive_type', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "path": lambda n : setattr(self, 'path', n.get_str_value()),
            "share_id": lambda n : setattr(self, 'share_id', n.get_str_value()),
            "sharepoint_ids": lambda n : setattr(self, 'sharepoint_ids', n.get_object_value(sharepoint_ids.SharepointIds)),
            "site_id": lambda n : setattr(self, 'site_id', n.get_str_value()),
        }
        return fields
    
    @property
    def id(self,) -> Optional[str]:
        """
        Gets the id property value. Unique identifier of the item in the drive. Read-only.
        Returns: Optional[str]
        """
        return self._id
    
    @id.setter
    def id(self,value: Optional[str] = None) -> None:
        """
        Sets the id property value. Unique identifier of the item in the drive. Read-only.
        Args:
            value: Value to set for the id property.
        """
        self._id = value
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. The name of the item being referenced. Read-only.
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. The name of the item being referenced. Read-only.
        Args:
            value: Value to set for the name property.
        """
        self._name = value
    
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
    def path(self,) -> Optional[str]:
        """
        Gets the path property value. Path that can be used to navigate to the item. Read-only.
        Returns: Optional[str]
        """
        return self._path
    
    @path.setter
    def path(self,value: Optional[str] = None) -> None:
        """
        Sets the path property value. Path that can be used to navigate to the item. Read-only.
        Args:
            value: Value to set for the path property.
        """
        self._path = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("driveId", self.drive_id)
        writer.write_str_value("driveType", self.drive_type)
        writer.write_str_value("id", self.id)
        writer.write_str_value("name", self.name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("path", self.path)
        writer.write_str_value("shareId", self.share_id)
        writer.write_object_value("sharepointIds", self.sharepoint_ids)
        writer.write_str_value("siteId", self.site_id)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def share_id(self,) -> Optional[str]:
        """
        Gets the shareId property value. A unique identifier for a shared resource that can be accessed via the [Shares][] API.
        Returns: Optional[str]
        """
        return self._share_id
    
    @share_id.setter
    def share_id(self,value: Optional[str] = None) -> None:
        """
        Sets the shareId property value. A unique identifier for a shared resource that can be accessed via the [Shares][] API.
        Args:
            value: Value to set for the shareId property.
        """
        self._share_id = value
    
    @property
    def sharepoint_ids(self,) -> Optional[sharepoint_ids.SharepointIds]:
        """
        Gets the sharepointIds property value. Returns identifiers useful for SharePoint REST compatibility. Read-only.
        Returns: Optional[sharepoint_ids.SharepointIds]
        """
        return self._sharepoint_ids
    
    @sharepoint_ids.setter
    def sharepoint_ids(self,value: Optional[sharepoint_ids.SharepointIds] = None) -> None:
        """
        Sets the sharepointIds property value. Returns identifiers useful for SharePoint REST compatibility. Read-only.
        Args:
            value: Value to set for the sharepointIds property.
        """
        self._sharepoint_ids = value
    
    @property
    def site_id(self,) -> Optional[str]:
        """
        Gets the siteId property value. For OneDrive for Business and SharePoint, this property represents the ID of the site that contains the parent document library of the driveItem resource. The value is the same as the id property of that [site][] resource. It is an opaque string that consists of three identifiers of the site. For OneDrive, this property is not populated.
        Returns: Optional[str]
        """
        return self._site_id
    
    @site_id.setter
    def site_id(self,value: Optional[str] = None) -> None:
        """
        Sets the siteId property value. For OneDrive for Business and SharePoint, this property represents the ID of the site that contains the parent document library of the driveItem resource. The value is the same as the id property of that [site][] resource. It is an opaque string that consists of three identifiers of the site. For OneDrive, this property is not populated.
        Args:
            value: Value to set for the siteId property.
        """
        self._site_id = value
    

