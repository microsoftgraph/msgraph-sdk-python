from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .alert_evidence import AlertEvidence
    from .stream import Stream

from .alert_evidence import AlertEvidence

@dataclass
class CloudApplicationEvidence(AlertEvidence, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.cloudApplicationEvidence"
    # Unique identifier of the application.
    app_id: Optional[int] = None
    # Name of the application.
    display_name: Optional[str] = None
    # Identifier of the instance of the Software as a Service (SaaS) application.
    instance_id: Optional[int] = None
    # Name of the instance of the SaaS application.
    instance_name: Optional[str] = None
    # The identifier of the SaaS application.
    saas_app_id: Optional[int] = None
    # The stream property
    stream: Optional[Stream] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudApplicationEvidence:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudApplicationEvidence
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloudApplicationEvidence()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .alert_evidence import AlertEvidence
        from .stream import Stream

        from .alert_evidence import AlertEvidence
        from .stream import Stream

        fields: dict[str, Callable[[Any], None]] = {
            "appId": lambda n : setattr(self, 'app_id', n.get_int_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "instanceId": lambda n : setattr(self, 'instance_id', n.get_int_value()),
            "instanceName": lambda n : setattr(self, 'instance_name', n.get_str_value()),
            "saasAppId": lambda n : setattr(self, 'saas_app_id', n.get_int_value()),
            "stream": lambda n : setattr(self, 'stream', n.get_object_value(Stream)),
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
        writer.write_int_value("appId", self.app_id)
        writer.write_str_value("displayName", self.display_name)
        writer.write_int_value("instanceId", self.instance_id)
        writer.write_str_value("instanceName", self.instance_name)
        writer.write_int_value("saasAppId", self.saas_app_id)
        writer.write_object_value("stream", self.stream)
    

