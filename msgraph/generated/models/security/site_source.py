from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

site = lazy_import('msgraph.generated.models.site')
data_source = lazy_import('msgraph.generated.models.security.data_source')

class SiteSource(data_source.DataSource):
    def __init__(self,) -> None:
        """
        Instantiates a new SiteSource and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.security.siteSource"
        # The site property
        self._site: Optional[site.Site] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SiteSource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SiteSource
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SiteSource()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "site": lambda n : setattr(self, 'site', n.get_object_value(site.Site)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("site", self.site)
    
    @property
    def site(self,) -> Optional[site.Site]:
        """
        Gets the site property value. The site property
        Returns: Optional[site.Site]
        """
        return self._site
    
    @site.setter
    def site(self,value: Optional[site.Site] = None) -> None:
        """
        Sets the site property value. The site property
        Args:
            value: Value to set for the site property.
        """
        self._site = value
    

