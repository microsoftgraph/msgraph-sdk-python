from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

cloud_app_security_session_control_type = lazy_import('msgraph.generated.models.cloud_app_security_session_control_type')
conditional_access_session_control = lazy_import('msgraph.generated.models.conditional_access_session_control')

class CloudAppSecuritySessionControl(conditional_access_session_control.ConditionalAccessSessionControl):
    @property
    def cloud_app_security_type(self,) -> Optional[cloud_app_security_session_control_type.CloudAppSecuritySessionControlType]:
        """
        Gets the cloudAppSecurityType property value. Possible values are: mcasConfigured, monitorOnly, blockDownloads, unknownFutureValue. For more information, see Deploy Conditional Access App Control for featured apps.
        Returns: Optional[cloud_app_security_session_control_type.CloudAppSecuritySessionControlType]
        """
        return self._cloud_app_security_type
    
    @cloud_app_security_type.setter
    def cloud_app_security_type(self,value: Optional[cloud_app_security_session_control_type.CloudAppSecuritySessionControlType] = None) -> None:
        """
        Sets the cloudAppSecurityType property value. Possible values are: mcasConfigured, monitorOnly, blockDownloads, unknownFutureValue. For more information, see Deploy Conditional Access App Control for featured apps.
        Args:
            value: Value to set for the cloudAppSecurityType property.
        """
        self._cloud_app_security_type = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new CloudAppSecuritySessionControl and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.cloudAppSecuritySessionControl"
        # Possible values are: mcasConfigured, monitorOnly, blockDownloads, unknownFutureValue. For more information, see Deploy Conditional Access App Control for featured apps.
        self._cloud_app_security_type: Optional[cloud_app_security_session_control_type.CloudAppSecuritySessionControlType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CloudAppSecuritySessionControl:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CloudAppSecuritySessionControl
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CloudAppSecuritySessionControl()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "cloud_app_security_type": lambda n : setattr(self, 'cloud_app_security_type', n.get_enum_value(cloud_app_security_session_control_type.CloudAppSecuritySessionControlType)),
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
        writer.write_enum_value("cloudAppSecurityType", self.cloud_app_security_type)
    

