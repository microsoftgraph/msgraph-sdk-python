from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .face_check_configuration import FaceCheckConfiguration
    from .verified_id_profile_configuration import VerifiedIdProfileConfiguration
    from .verified_id_profile_state import VerifiedIdProfileState
    from .verified_id_usage_configuration import VerifiedIdUsageConfiguration

from .entity import Entity

@dataclass
class VerifiedIdProfile(Entity, Parsable):
    # Description for the verified ID profile. Required.
    description: Optional[str] = None
    # The faceCheckConfiguration property
    face_check_configuration: Optional[FaceCheckConfiguration] = None
    # DateTime the profile was last modified. Optional.
    last_modified_date_time: Optional[datetime.datetime] = None
    # Display name for the verified ID profile. Required.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Defines profile processing priority if multiple profiles are configured. Optional.
    priority: Optional[int] = None
    # The state property
    state: Optional[VerifiedIdProfileState] = None
    # The verifiedIdProfileConfiguration property
    verified_id_profile_configuration: Optional[VerifiedIdProfileConfiguration] = None
    # Collection defining the usage purpose for the profile. Required.
    verified_id_usage_configurations: Optional[list[VerifiedIdUsageConfiguration]] = None
    # Decentralized Identifier (DID) string that represents the verifier in the verifiable credential exchange. Required.
    verifier_did: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> VerifiedIdProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: VerifiedIdProfile
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return VerifiedIdProfile()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .face_check_configuration import FaceCheckConfiguration
        from .verified_id_profile_configuration import VerifiedIdProfileConfiguration
        from .verified_id_profile_state import VerifiedIdProfileState
        from .verified_id_usage_configuration import VerifiedIdUsageConfiguration

        from .entity import Entity
        from .face_check_configuration import FaceCheckConfiguration
        from .verified_id_profile_configuration import VerifiedIdProfileConfiguration
        from .verified_id_profile_state import VerifiedIdProfileState
        from .verified_id_usage_configuration import VerifiedIdUsageConfiguration

        fields: dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "faceCheckConfiguration": lambda n : setattr(self, 'face_check_configuration', n.get_object_value(FaceCheckConfiguration)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "priority": lambda n : setattr(self, 'priority', n.get_int_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(VerifiedIdProfileState)),
            "verifiedIdProfileConfiguration": lambda n : setattr(self, 'verified_id_profile_configuration', n.get_object_value(VerifiedIdProfileConfiguration)),
            "verifiedIdUsageConfigurations": lambda n : setattr(self, 'verified_id_usage_configurations', n.get_collection_of_object_values(VerifiedIdUsageConfiguration)),
            "verifierDid": lambda n : setattr(self, 'verifier_did', n.get_str_value()),
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
        writer.write_str_value("description", self.description)
        writer.write_object_value("faceCheckConfiguration", self.face_check_configuration)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("name", self.name)
        writer.write_int_value("priority", self.priority)
        writer.write_enum_value("state", self.state)
        writer.write_object_value("verifiedIdProfileConfiguration", self.verified_id_profile_configuration)
        writer.write_collection_of_object_values("verifiedIdUsageConfigurations", self.verified_id_usage_configurations)
        writer.write_str_value("verifierDid", self.verifier_did)
    

