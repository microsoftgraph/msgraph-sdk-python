from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import delegated_admin_access_container_type

@dataclass
class DelegatedAdminAccessContainer(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The identifier of the access container (for example, a security group). For 'securityGroup' access containers, this must be a valid ID of an Azure AD security group in the Microsoft partner's tenant.
    access_container_id: Optional[str] = None
    # The accessContainerType property
    access_container_type: Optional[delegated_admin_access_container_type.DelegatedAdminAccessContainerType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DelegatedAdminAccessContainer:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DelegatedAdminAccessContainer
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DelegatedAdminAccessContainer()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import delegated_admin_access_container_type

        from . import delegated_admin_access_container_type

        fields: Dict[str, Callable[[Any], None]] = {
            "accessContainerId": lambda n : setattr(self, 'access_container_id', n.get_str_value()),
            "accessContainerType": lambda n : setattr(self, 'access_container_type', n.get_enum_value(delegated_admin_access_container_type.DelegatedAdminAccessContainerType)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("accessContainerId", self.access_container_id)
        writer.write_enum_value("accessContainerType", self.access_container_type)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

