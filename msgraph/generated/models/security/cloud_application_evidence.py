from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

alert_evidence = lazy_import('msgraph.generated.models.security.alert_evidence')

class CloudApplicationEvidence(alert_evidence.AlertEvidence):
    @property
    def app_id(self,) -> Optional[int]:
        """
        Gets the appId property value. Unique identifier of the application.
        Returns: Optional[int]
        """
        return self._app_id
    
    @app_id.setter
    def app_id(self,value: Optional[int] = None) -> None:
        """
        Sets the appId property value. Unique identifier of the application.
        Args:
            value: Value to set for the appId property.
        """
        self._app_id = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new CloudApplicationEvidence and sets the default values.
        """
        super().__init__()
        # Unique identifier of the application.
        self._app_id: Optional[int] = None
        # Name of the application.
        self._display_name: Optional[str] = None
        # Identifier of the instance of the Software as a Service (SaaS) application.
        self._instance_id: Optional[int] = None
        # Name of the instance of the SaaS application.
        self._instance_name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The identifier of the SaaS application.
        self._saas_app_id: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CloudApplicationEvidence:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CloudApplicationEvidence
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CloudApplicationEvidence()
    
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
            "app_id": lambda n : setattr(self, 'app_id', n.get_int_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "instance_id": lambda n : setattr(self, 'instance_id', n.get_int_value()),
            "instance_name": lambda n : setattr(self, 'instance_name', n.get_str_value()),
            "saas_app_id": lambda n : setattr(self, 'saas_app_id', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def instance_id(self,) -> Optional[int]:
        """
        Gets the instanceId property value. Identifier of the instance of the Software as a Service (SaaS) application.
        Returns: Optional[int]
        """
        return self._instance_id
    
    @instance_id.setter
    def instance_id(self,value: Optional[int] = None) -> None:
        """
        Sets the instanceId property value. Identifier of the instance of the Software as a Service (SaaS) application.
        Args:
            value: Value to set for the instanceId property.
        """
        self._instance_id = value
    
    @property
    def instance_name(self,) -> Optional[str]:
        """
        Gets the instanceName property value. Name of the instance of the SaaS application.
        Returns: Optional[str]
        """
        return self._instance_name
    
    @instance_name.setter
    def instance_name(self,value: Optional[str] = None) -> None:
        """
        Sets the instanceName property value. Name of the instance of the SaaS application.
        Args:
            value: Value to set for the instanceName property.
        """
        self._instance_name = value
    
    @property
    def saas_app_id(self,) -> Optional[int]:
        """
        Gets the saasAppId property value. The identifier of the SaaS application.
        Returns: Optional[int]
        """
        return self._saas_app_id
    
    @saas_app_id.setter
    def saas_app_id(self,value: Optional[int] = None) -> None:
        """
        Sets the saasAppId property value. The identifier of the SaaS application.
        Args:
            value: Value to set for the saasAppId property.
        """
        self._saas_app_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_int_value("appId", self.app_id)
        writer.write_str_value("displayName", self.display_name)
        writer.write_int_value("instanceId", self.instance_id)
        writer.write_str_value("instanceName", self.instance_name)
        writer.write_int_value("saasAppId", self.saas_app_id)
    

