from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
outlook_category = lazy_import('msgraph.generated.models.outlook_category')

class OutlookUser(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new outlookUser and sets the default values.
        """
        super().__init__()
        # A list of categories defined for the user.
        self._master_categories: Optional[List[outlook_category.OutlookCategory]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OutlookUser:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OutlookUser
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return OutlookUser()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "master_categories": lambda n : setattr(self, 'master_categories', n.get_collection_of_object_values(outlook_category.OutlookCategory)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def master_categories(self,) -> Optional[List[outlook_category.OutlookCategory]]:
        """
        Gets the masterCategories property value. A list of categories defined for the user.
        Returns: Optional[List[outlook_category.OutlookCategory]]
        """
        return self._master_categories
    
    @master_categories.setter
    def master_categories(self,value: Optional[List[outlook_category.OutlookCategory]] = None) -> None:
        """
        Sets the masterCategories property value. A list of categories defined for the user.
        Args:
            value: Value to set for the masterCategories property.
        """
        self._master_categories = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("masterCategories", self.master_categories)
    

