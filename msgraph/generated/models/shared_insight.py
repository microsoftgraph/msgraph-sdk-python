from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
resource_reference = lazy_import('msgraph.generated.models.resource_reference')
resource_visualization = lazy_import('msgraph.generated.models.resource_visualization')
sharing_detail = lazy_import('msgraph.generated.models.sharing_detail')

class SharedInsight(entity.Entity):
    """
    Provides operations to manage the admin singleton.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new sharedInsight and sets the default values.
        """
        super().__init__()
        # Details about the shared item. Read only.
        self._last_shared: Optional[sharing_detail.SharingDetail] = None
        # The lastSharedMethod property
        self._last_shared_method: Optional[entity.Entity] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Used for navigating to the item that was shared. For file attachments, the type is fileAttachment. For linked attachments, the type is driveItem.
        self._resource: Optional[entity.Entity] = None
        # Reference properties of the shared document, such as the url and type of the document. Read-only
        self._resource_reference: Optional[resource_reference.ResourceReference] = None
        # Properties that you can use to visualize the document in your experience. Read-only
        self._resource_visualization: Optional[resource_visualization.ResourceVisualization] = None
        # The sharingHistory property
        self._sharing_history: Optional[List[sharing_detail.SharingDetail]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SharedInsight:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SharedInsight
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SharedInsight()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "last_shared": lambda n : setattr(self, 'last_shared', n.get_object_value(sharing_detail.SharingDetail)),
            "last_shared_method": lambda n : setattr(self, 'last_shared_method', n.get_object_value(entity.Entity)),
            "resource": lambda n : setattr(self, 'resource', n.get_object_value(entity.Entity)),
            "resource_reference": lambda n : setattr(self, 'resource_reference', n.get_object_value(resource_reference.ResourceReference)),
            "resource_visualization": lambda n : setattr(self, 'resource_visualization', n.get_object_value(resource_visualization.ResourceVisualization)),
            "sharing_history": lambda n : setattr(self, 'sharing_history', n.get_collection_of_object_values(sharing_detail.SharingDetail)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_shared(self,) -> Optional[sharing_detail.SharingDetail]:
        """
        Gets the lastShared property value. Details about the shared item. Read only.
        Returns: Optional[sharing_detail.SharingDetail]
        """
        return self._last_shared
    
    @last_shared.setter
    def last_shared(self,value: Optional[sharing_detail.SharingDetail] = None) -> None:
        """
        Sets the lastShared property value. Details about the shared item. Read only.
        Args:
            value: Value to set for the lastShared property.
        """
        self._last_shared = value
    
    @property
    def last_shared_method(self,) -> Optional[entity.Entity]:
        """
        Gets the lastSharedMethod property value. The lastSharedMethod property
        Returns: Optional[entity.Entity]
        """
        return self._last_shared_method
    
    @last_shared_method.setter
    def last_shared_method(self,value: Optional[entity.Entity] = None) -> None:
        """
        Sets the lastSharedMethod property value. The lastSharedMethod property
        Args:
            value: Value to set for the lastSharedMethod property.
        """
        self._last_shared_method = value
    
    @property
    def resource(self,) -> Optional[entity.Entity]:
        """
        Gets the resource property value. Used for navigating to the item that was shared. For file attachments, the type is fileAttachment. For linked attachments, the type is driveItem.
        Returns: Optional[entity.Entity]
        """
        return self._resource
    
    @resource.setter
    def resource(self,value: Optional[entity.Entity] = None) -> None:
        """
        Sets the resource property value. Used for navigating to the item that was shared. For file attachments, the type is fileAttachment. For linked attachments, the type is driveItem.
        Args:
            value: Value to set for the resource property.
        """
        self._resource = value
    
    @property
    def resource_reference(self,) -> Optional[resource_reference.ResourceReference]:
        """
        Gets the resourceReference property value. Reference properties of the shared document, such as the url and type of the document. Read-only
        Returns: Optional[resource_reference.ResourceReference]
        """
        return self._resource_reference
    
    @resource_reference.setter
    def resource_reference(self,value: Optional[resource_reference.ResourceReference] = None) -> None:
        """
        Sets the resourceReference property value. Reference properties of the shared document, such as the url and type of the document. Read-only
        Args:
            value: Value to set for the resourceReference property.
        """
        self._resource_reference = value
    
    @property
    def resource_visualization(self,) -> Optional[resource_visualization.ResourceVisualization]:
        """
        Gets the resourceVisualization property value. Properties that you can use to visualize the document in your experience. Read-only
        Returns: Optional[resource_visualization.ResourceVisualization]
        """
        return self._resource_visualization
    
    @resource_visualization.setter
    def resource_visualization(self,value: Optional[resource_visualization.ResourceVisualization] = None) -> None:
        """
        Sets the resourceVisualization property value. Properties that you can use to visualize the document in your experience. Read-only
        Args:
            value: Value to set for the resourceVisualization property.
        """
        self._resource_visualization = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("lastShared", self.last_shared)
        writer.write_object_value("lastSharedMethod", self.last_shared_method)
        writer.write_object_value("resource", self.resource)
        writer.write_collection_of_object_values("sharingHistory", self.sharing_history)
    
    @property
    def sharing_history(self,) -> Optional[List[sharing_detail.SharingDetail]]:
        """
        Gets the sharingHistory property value. The sharingHistory property
        Returns: Optional[List[sharing_detail.SharingDetail]]
        """
        return self._sharing_history
    
    @sharing_history.setter
    def sharing_history(self,value: Optional[List[sharing_detail.SharingDetail]] = None) -> None:
        """
        Sets the sharingHistory property value. The sharingHistory property
        Args:
            value: Value to set for the sharingHistory property.
        """
        self._sharing_history = value
    

