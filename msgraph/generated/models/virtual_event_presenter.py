from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .identity import Identity
    from .virtual_event_presenter_details import VirtualEventPresenterDetails

from .entity import Entity

@dataclass
class VirtualEventPresenter(Entity, Parsable):
    # Email address of the presenter.
    email: Optional[str] = None
    # Identity information of the presenter. The supported identities are: communicationsGuestIdentity and communicationsUserIdentity.
    identity: Optional[Identity] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Other details about the presenter. This property returns null when the virtual event type is virtualEventTownhall.
    presenter_details: Optional[VirtualEventPresenterDetails] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> VirtualEventPresenter:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: VirtualEventPresenter
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return VirtualEventPresenter()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .identity import Identity
        from .virtual_event_presenter_details import VirtualEventPresenterDetails

        from .entity import Entity
        from .identity import Identity
        from .virtual_event_presenter_details import VirtualEventPresenterDetails

        fields: dict[str, Callable[[Any], None]] = {
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "identity": lambda n : setattr(self, 'identity', n.get_object_value(Identity)),
            "presenterDetails": lambda n : setattr(self, 'presenter_details', n.get_object_value(VirtualEventPresenterDetails)),
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
        writer.write_str_value("email", self.email)
        writer.write_object_value("identity", self.identity)
        writer.write_object_value("presenterDetails", self.presenter_details)
    

