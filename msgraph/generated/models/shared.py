from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

identity_set = lazy_import('msgraph.generated.models.identity_set')

class Shared(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new shared and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # The identity of the owner of the shared item. Read-only.
        self._owner: Optional[identity_set.IdentitySet] = None
        # Indicates the scope of how the item is shared: anonymous, organization, or users. Read-only.
        self._scope: Optional[str] = None
        # The identity of the user who shared the item. Read-only.
        self._shared_by: Optional[identity_set.IdentitySet] = None
        # The UTC date and time when the item was shared. Read-only.
        self._shared_date_time: Optional[datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Shared:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Shared
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Shared()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "owner": lambda n : setattr(self, 'owner', n.get_object_value(identity_set.IdentitySet)),
            "scope": lambda n : setattr(self, 'scope', n.get_str_value()),
            "shared_by": lambda n : setattr(self, 'shared_by', n.get_object_value(identity_set.IdentitySet)),
            "shared_date_time": lambda n : setattr(self, 'shared_date_time', n.get_datetime_value()),
        }
        return fields
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def owner(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the owner property value. The identity of the owner of the shared item. Read-only.
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._owner
    
    @owner.setter
    def owner(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the owner property value. The identity of the owner of the shared item. Read-only.
        Args:
            value: Value to set for the owner property.
        """
        self._owner = value
    
    @property
    def scope(self,) -> Optional[str]:
        """
        Gets the scope property value. Indicates the scope of how the item is shared: anonymous, organization, or users. Read-only.
        Returns: Optional[str]
        """
        return self._scope
    
    @scope.setter
    def scope(self,value: Optional[str] = None) -> None:
        """
        Sets the scope property value. Indicates the scope of how the item is shared: anonymous, organization, or users. Read-only.
        Args:
            value: Value to set for the scope property.
        """
        self._scope = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("owner", self.owner)
        writer.write_str_value("scope", self.scope)
        writer.write_object_value("sharedBy", self.shared_by)
        writer.write_datetime_value("sharedDateTime", self.shared_date_time)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def shared_by(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the sharedBy property value. The identity of the user who shared the item. Read-only.
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._shared_by
    
    @shared_by.setter
    def shared_by(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the sharedBy property value. The identity of the user who shared the item. Read-only.
        Args:
            value: Value to set for the sharedBy property.
        """
        self._shared_by = value
    
    @property
    def shared_date_time(self,) -> Optional[datetime]:
        """
        Gets the sharedDateTime property value. The UTC date and time when the item was shared. Read-only.
        Returns: Optional[datetime]
        """
        return self._shared_date_time
    
    @shared_date_time.setter
    def shared_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the sharedDateTime property value. The UTC date and time when the item was shared. Read-only.
        Args:
            value: Value to set for the sharedDateTime property.
        """
        self._shared_date_time = value
    

