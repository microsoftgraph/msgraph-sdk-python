from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
resource_reference = lazy_import('msgraph.generated.models.resource_reference')
resource_visualization = lazy_import('msgraph.generated.models.resource_visualization')

class Trending(entity.Entity):
    """
    Provides operations to manage the admin singleton.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new trending and sets the default values.
        """
        super().__init__()
        # The lastModifiedDateTime property
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Used for navigating to the trending document.
        self._resource: Optional[entity.Entity] = None
        # Reference properties of the trending document, such as the url and type of the document.
        self._resource_reference: Optional[resource_reference.ResourceReference] = None
        # Properties that you can use to visualize the document in your experience.
        self._resource_visualization: Optional[resource_visualization.ResourceVisualization] = None
        # Value indicating how much the document is currently trending. The larger the number, the more the document is currently trending around the user (the more relevant it is). Returned documents are sorted by this value.
        self._weight: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Trending:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Trending
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Trending()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "resource": lambda n : setattr(self, 'resource', n.get_object_value(entity.Entity)),
            "resource_reference": lambda n : setattr(self, 'resource_reference', n.get_object_value(resource_reference.ResourceReference)),
            "resource_visualization": lambda n : setattr(self, 'resource_visualization', n.get_object_value(resource_visualization.ResourceVisualization)),
            "weight": lambda n : setattr(self, 'weight', n.get_float_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. The lastModifiedDateTime property
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. The lastModifiedDateTime property
        Args:
            value: Value to set for the lastModifiedDateTime property.
        """
        self._last_modified_date_time = value
    
    @property
    def resource(self,) -> Optional[entity.Entity]:
        """
        Gets the resource property value. Used for navigating to the trending document.
        Returns: Optional[entity.Entity]
        """
        return self._resource
    
    @resource.setter
    def resource(self,value: Optional[entity.Entity] = None) -> None:
        """
        Sets the resource property value. Used for navigating to the trending document.
        Args:
            value: Value to set for the resource property.
        """
        self._resource = value
    
    @property
    def resource_reference(self,) -> Optional[resource_reference.ResourceReference]:
        """
        Gets the resourceReference property value. Reference properties of the trending document, such as the url and type of the document.
        Returns: Optional[resource_reference.ResourceReference]
        """
        return self._resource_reference
    
    @resource_reference.setter
    def resource_reference(self,value: Optional[resource_reference.ResourceReference] = None) -> None:
        """
        Sets the resourceReference property value. Reference properties of the trending document, such as the url and type of the document.
        Args:
            value: Value to set for the resourceReference property.
        """
        self._resource_reference = value
    
    @property
    def resource_visualization(self,) -> Optional[resource_visualization.ResourceVisualization]:
        """
        Gets the resourceVisualization property value. Properties that you can use to visualize the document in your experience.
        Returns: Optional[resource_visualization.ResourceVisualization]
        """
        return self._resource_visualization
    
    @resource_visualization.setter
    def resource_visualization(self,value: Optional[resource_visualization.ResourceVisualization] = None) -> None:
        """
        Sets the resourceVisualization property value. Properties that you can use to visualize the document in your experience.
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
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_object_value("resource", self.resource)
        writer.write_float_value("weight", self.weight)
    
    @property
    def weight(self,) -> Optional[float]:
        """
        Gets the weight property value. Value indicating how much the document is currently trending. The larger the number, the more the document is currently trending around the user (the more relevant it is). Returned documents are sorted by this value.
        Returns: Optional[float]
        """
        return self._weight
    
    @weight.setter
    def weight(self,value: Optional[float] = None) -> None:
        """
        Sets the weight property value. Value indicating how much the document is currently trending. The larger the number, the more the document is currently trending around the user (the more relevant it is). Returned documents are sorted by this value.
        Args:
            value: Value to set for the weight property.
        """
        self._weight = value
    

