from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import identity

from . import identity

class ServicePrincipalIdentity(identity.Identity):
    def __init__(self,) -> None:
        """
        Instantiates a new ServicePrincipalIdentity and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.servicePrincipalIdentity"
        # The application identifier of the service principal.
        self._app_id: Optional[str] = None
    
    @property
    def app_id(self,) -> Optional[str]:
        """
        Gets the appId property value. The application identifier of the service principal.
        Returns: Optional[str]
        """
        return self._app_id
    
    @app_id.setter
    def app_id(self,value: Optional[str] = None) -> None:
        """
        Sets the appId property value. The application identifier of the service principal.
        Args:
            value: Value to set for the app_id property.
        """
        self._app_id = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ServicePrincipalIdentity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ServicePrincipalIdentity
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ServicePrincipalIdentity()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import identity

        fields: Dict[str, Callable[[Any], None]] = {
            "appId": lambda n : setattr(self, 'app_id', n.get_str_value()),
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
        writer.write_str_value("appId", self.app_id)
    

