from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_app_security_session_control_type import CloudAppSecuritySessionControlType
    from .conditional_access_session_control import ConditionalAccessSessionControl

from .conditional_access_session_control import ConditionalAccessSessionControl

@dataclass
class CloudAppSecuritySessionControl(ConditionalAccessSessionControl, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.cloudAppSecuritySessionControl"
    # Possible values are: mcasConfigured, monitorOnly, blockDownloads, unknownFutureValue. For more information, see Deploy Conditional Access App Control for featured apps.
    cloud_app_security_type: Optional[CloudAppSecuritySessionControlType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudAppSecuritySessionControl:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudAppSecuritySessionControl
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloudAppSecuritySessionControl()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_app_security_session_control_type import CloudAppSecuritySessionControlType
        from .conditional_access_session_control import ConditionalAccessSessionControl

        from .cloud_app_security_session_control_type import CloudAppSecuritySessionControlType
        from .conditional_access_session_control import ConditionalAccessSessionControl

        fields: Dict[str, Callable[[Any], None]] = {
            "cloudAppSecurityType": lambda n : setattr(self, 'cloud_app_security_type', n.get_enum_value(CloudAppSecuritySessionControlType)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        from .cloud_app_security_session_control_type import CloudAppSecuritySessionControlType
        from .conditional_access_session_control import ConditionalAccessSessionControl

        writer.write_enum_value("cloudAppSecurityType", self.cloud_app_security_type)
    

