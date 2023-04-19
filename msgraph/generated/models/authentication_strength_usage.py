from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import conditional_access_policy

class AuthenticationStrengthUsage(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new authenticationStrengthUsage and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The mfa property
        self._mfa: Optional[List[conditional_access_policy.ConditionalAccessPolicy]] = None
        # The none property
        self._none_: Optional[List[conditional_access_policy.ConditionalAccessPolicy]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
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
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AuthenticationStrengthUsage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AuthenticationStrengthUsage
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AuthenticationStrengthUsage()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import conditional_access_policy

        fields: Dict[str, Callable[[Any], None]] = {
            "mfa": lambda n : setattr(self, 'mfa', n.get_collection_of_object_values(conditional_access_policy.ConditionalAccessPolicy)),
            "none": lambda n : setattr(self, 'none_', n.get_collection_of_object_values(conditional_access_policy.ConditionalAccessPolicy)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def mfa(self,) -> Optional[List[conditional_access_policy.ConditionalAccessPolicy]]:
        """
        Gets the mfa property value. The mfa property
        Returns: Optional[List[conditional_access_policy.ConditionalAccessPolicy]]
        """
        return self._mfa
    
    @mfa.setter
    def mfa(self,value: Optional[List[conditional_access_policy.ConditionalAccessPolicy]] = None) -> None:
        """
        Sets the mfa property value. The mfa property
        Args:
            value: Value to set for the mfa property.
        """
        self._mfa = value
    
    @property
    def none_(self,) -> Optional[List[conditional_access_policy.ConditionalAccessPolicy]]:
        """
        Gets the none property value. The none property
        Returns: Optional[List[conditional_access_policy.ConditionalAccessPolicy]]
        """
        return self._none_
    
    @none_.setter
    def none_(self,value: Optional[List[conditional_access_policy.ConditionalAccessPolicy]] = None) -> None:
        """
        Sets the none property value. The none property
        Args:
            value: Value to set for the none_ property.
        """
        self._none_ = value
    
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
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_object_values("mfa", self.mfa)
        writer.write_collection_of_object_values("none", self.none_)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

