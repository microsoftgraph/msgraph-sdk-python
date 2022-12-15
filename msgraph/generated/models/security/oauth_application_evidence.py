from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

alert_evidence = lazy_import('msgraph.generated.models.security.alert_evidence')

class OauthApplicationEvidence(alert_evidence.AlertEvidence):
    @property
    def app_id(self,) -> Optional[str]:
        """
        Gets the appId property value. Unique identifier of the application.
        Returns: Optional[str]
        """
        return self._app_id
    
    @app_id.setter
    def app_id(self,value: Optional[str] = None) -> None:
        """
        Sets the appId property value. Unique identifier of the application.
        Args:
            value: Value to set for the appId property.
        """
        self._app_id = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new OauthApplicationEvidence and sets the default values.
        """
        super().__init__()
        # Unique identifier of the application.
        self._app_id: Optional[str] = None
        # Name of the application.
        self._display_name: Optional[str] = None
        # The unique identifier of the application object in Azure AD.
        self._object_id: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The name of the application publisher.
        self._publisher: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OauthApplicationEvidence:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OauthApplicationEvidence
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return OauthApplicationEvidence()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Name of the application.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Name of the application.
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
            "app_id": lambda n : setattr(self, 'app_id', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "object_id": lambda n : setattr(self, 'object_id', n.get_str_value()),
            "publisher": lambda n : setattr(self, 'publisher', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def object_id(self,) -> Optional[str]:
        """
        Gets the objectId property value. The unique identifier of the application object in Azure AD.
        Returns: Optional[str]
        """
        return self._object_id
    
    @object_id.setter
    def object_id(self,value: Optional[str] = None) -> None:
        """
        Sets the objectId property value. The unique identifier of the application object in Azure AD.
        Args:
            value: Value to set for the objectId property.
        """
        self._object_id = value
    
    @property
    def publisher(self,) -> Optional[str]:
        """
        Gets the publisher property value. The name of the application publisher.
        Returns: Optional[str]
        """
        return self._publisher
    
    @publisher.setter
    def publisher(self,value: Optional[str] = None) -> None:
        """
        Sets the publisher property value. The name of the application publisher.
        Args:
            value: Value to set for the publisher property.
        """
        self._publisher = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("appId", self.app_id)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("objectId", self.object_id)
        writer.write_str_value("publisher", self.publisher)
    

