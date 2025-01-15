from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .directory_object import DirectoryObject
    from .governance_insight import GovernanceInsight
    from .outlier_container_type import OutlierContainerType
    from .outlier_member_type import OutlierMemberType
    from .user import User

from .governance_insight import GovernanceInsight

@dataclass
class MembershipOutlierInsight(GovernanceInsight, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.membershipOutlierInsight"
    # Navigation link to the container directory object. For example, to a group.
    container: Optional[DirectoryObject] = None
    # Indicates the identifier of the container, for example, a group ID.
    container_id: Optional[str] = None
    # Navigation link to a member object who modified the record. For example, to a user.
    last_modified_by: Optional[User] = None
    # Navigation link to a member object. For example, to a user.
    member: Optional[DirectoryObject] = None
    # Indicates the identifier of the user.
    member_id: Optional[str] = None
    # The outlierContainerType property
    outlier_container_type: Optional[OutlierContainerType] = None
    # The outlierMemberType property
    outlier_member_type: Optional[OutlierMemberType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MembershipOutlierInsight:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MembershipOutlierInsight
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MembershipOutlierInsight()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .directory_object import DirectoryObject
        from .governance_insight import GovernanceInsight
        from .outlier_container_type import OutlierContainerType
        from .outlier_member_type import OutlierMemberType
        from .user import User

        from .directory_object import DirectoryObject
        from .governance_insight import GovernanceInsight
        from .outlier_container_type import OutlierContainerType
        from .outlier_member_type import OutlierMemberType
        from .user import User

        fields: dict[str, Callable[[Any], None]] = {
            "container": lambda n : setattr(self, 'container', n.get_object_value(DirectoryObject)),
            "containerId": lambda n : setattr(self, 'container_id', n.get_str_value()),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(User)),
            "member": lambda n : setattr(self, 'member', n.get_object_value(DirectoryObject)),
            "memberId": lambda n : setattr(self, 'member_id', n.get_str_value()),
            "outlierContainerType": lambda n : setattr(self, 'outlier_container_type', n.get_enum_value(OutlierContainerType)),
            "outlierMemberType": lambda n : setattr(self, 'outlier_member_type', n.get_enum_value(OutlierMemberType)),
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
        writer.write_object_value("container", self.container)
        writer.write_str_value("containerId", self.container_id)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_object_value("member", self.member)
        writer.write_str_value("memberId", self.member_id)
        writer.write_enum_value("outlierContainerType", self.outlier_container_type)
        writer.write_enum_value("outlierMemberType", self.outlier_member_type)
    

