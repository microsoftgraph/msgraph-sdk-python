from __future__ import annotations
from datetime import timedelta
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

access_review_query_scope = lazy_import('msgraph.generated.models.access_review_query_scope')

class AccessReviewInactiveUsersQueryScope(access_review_query_scope.AccessReviewQueryScope):
    def __init__(self,) -> None:
        """
        Instantiates a new AccessReviewInactiveUsersQueryScope and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.accessReviewInactiveUsersQueryScope"
        # Defines the duration of inactivity. Inactivity is based on the last sign in date of the user compared to the access review instance's start date. If this property is not specified, it's assigned the default value PT0S.
        self._inactive_duration: Optional[Timedelta] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessReviewInactiveUsersQueryScope:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessReviewInactiveUsersQueryScope
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AccessReviewInactiveUsersQueryScope()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "inactive_duration": lambda n : setattr(self, 'inactive_duration', n.get_object_value(Timedelta)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def inactive_duration(self,) -> Optional[Timedelta]:
        """
        Gets the inactiveDuration property value. Defines the duration of inactivity. Inactivity is based on the last sign in date of the user compared to the access review instance's start date. If this property is not specified, it's assigned the default value PT0S.
        Returns: Optional[Timedelta]
        """
        return self._inactive_duration
    
    @inactive_duration.setter
    def inactive_duration(self,value: Optional[Timedelta] = None) -> None:
        """
        Sets the inactiveDuration property value. Defines the duration of inactivity. Inactivity is based on the last sign in date of the user compared to the access review instance's start date. If this property is not specified, it's assigned the default value PT0S.
        Args:
            value: Value to set for the inactiveDuration property.
        """
        self._inactive_duration = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("inactiveDuration", self.inactive_duration)
    

