from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

alert_evidence = lazy_import('msgraph.generated.models.security.alert_evidence')

class UrlEvidence(alert_evidence.AlertEvidence):
    def __init__(self,) -> None:
        """
        Instantiates a new UrlEvidence and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The Unique Resource Locator (URL).
        self._url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UrlEvidence:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UrlEvidence
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UrlEvidence()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "url": lambda n : setattr(self, 'url', n.get_str_value()),
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
        writer.write_str_value("url", self.url)
    
    @property
    def url(self,) -> Optional[str]:
        """
        Gets the url property value. The Unique Resource Locator (URL).
        Returns: Optional[str]
        """
        return self._url
    
    @url.setter
    def url(self,value: Optional[str] = None) -> None:
        """
        Sets the url property value. The Unique Resource Locator (URL).
        Args:
            value: Value to set for the url property.
        """
        self._url = value
    

