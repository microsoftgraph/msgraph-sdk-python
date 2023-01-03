from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
resource_reference = lazy_import('msgraph.generated.models.resource_reference')
resource_visualization = lazy_import('msgraph.generated.models.resource_visualization')
usage_details = lazy_import('msgraph.generated.models.usage_details')

class UsedInsight(entity.Entity):
    """
    Provides operations to manage the admin singleton.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new usedInsight and sets the default values.
        """
        super().__init__()
        # Information about when the item was last viewed or modified by the user. Read only.
        self._last_used: Optional[usage_details.UsageDetails] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Used for navigating to the item that was used. For file attachments, the type is fileAttachment. For linked attachments, the type is driveItem.
        self._resource: Optional[entity.Entity] = None
        # Reference properties of the used document, such as the url and type of the document. Read-only
        self._resource_reference: Optional[resource_reference.ResourceReference] = None
        # Properties that you can use to visualize the document in your experience. Read-only
        self._resource_visualization: Optional[resource_visualization.ResourceVisualization] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UsedInsight:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UsedInsight
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UsedInsight()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "last_used": lambda n : setattr(self, 'last_used', n.get_object_value(usage_details.UsageDetails)),
            "resource": lambda n : setattr(self, 'resource', n.get_object_value(entity.Entity)),
            "resource_reference": lambda n : setattr(self, 'resource_reference', n.get_object_value(resource_reference.ResourceReference)),
            "resource_visualization": lambda n : setattr(self, 'resource_visualization', n.get_object_value(resource_visualization.ResourceVisualization)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_used(self,) -> Optional[usage_details.UsageDetails]:
        """
        Gets the lastUsed property value. Information about when the item was last viewed or modified by the user. Read only.
        Returns: Optional[usage_details.UsageDetails]
        """
        return self._last_used
    
    @last_used.setter
    def last_used(self,value: Optional[usage_details.UsageDetails] = None) -> None:
        """
        Sets the lastUsed property value. Information about when the item was last viewed or modified by the user. Read only.
        Args:
            value: Value to set for the lastUsed property.
        """
        self._last_used = value
    
    @property
    def resource(self,) -> Optional[entity.Entity]:
        """
        Gets the resource property value. Used for navigating to the item that was used. For file attachments, the type is fileAttachment. For linked attachments, the type is driveItem.
        Returns: Optional[entity.Entity]
        """
        return self._resource
    
    @resource.setter
    def resource(self,value: Optional[entity.Entity] = None) -> None:
        """
        Sets the resource property value. Used for navigating to the item that was used. For file attachments, the type is fileAttachment. For linked attachments, the type is driveItem.
        Args:
            value: Value to set for the resource property.
        """
        self._resource = value
    
    @property
    def resource_reference(self,) -> Optional[resource_reference.ResourceReference]:
        """
        Gets the resourceReference property value. Reference properties of the used document, such as the url and type of the document. Read-only
        Returns: Optional[resource_reference.ResourceReference]
        """
        return self._resource_reference
    
    @resource_reference.setter
    def resource_reference(self,value: Optional[resource_reference.ResourceReference] = None) -> None:
        """
        Sets the resourceReference property value. Reference properties of the used document, such as the url and type of the document. Read-only
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
        writer.write_object_value("lastUsed", self.last_used)
        writer.write_object_value("resource", self.resource)
    

