from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

assigned_license = lazy_import('msgraph.generated.models.assigned_license')

class AssignLicensePostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the assignLicense method.
    """
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
    
    @property
    def add_licenses(self,) -> Optional[List[assigned_license.AssignedLicense]]:
        """
        Gets the addLicenses property value. The addLicenses property
        Returns: Optional[List[assigned_license.AssignedLicense]]
        """
        return self._add_licenses
    
    @add_licenses.setter
    def add_licenses(self,value: Optional[List[assigned_license.AssignedLicense]] = None) -> None:
        """
        Sets the addLicenses property value. The addLicenses property
        Args:
            value: Value to set for the addLicenses property.
        """
        self._add_licenses = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new assignLicensePostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The addLicenses property
        self._add_licenses: Optional[List[assigned_license.AssignedLicense]] = None
        # The removeLicenses property
        self._remove_licenses: Optional[List[Guid]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AssignLicensePostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AssignLicensePostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AssignLicensePostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "add_licenses": lambda n : setattr(self, 'add_licenses', n.get_collection_of_object_values(assigned_license.AssignedLicense)),
            "remove_licenses": lambda n : setattr(self, 'remove_licenses', n.get_collection_of_primitive_values(guid)),
        }
        return fields
    
    @property
    def remove_licenses(self,) -> Optional[List[Guid]]:
        """
        Gets the removeLicenses property value. The removeLicenses property
        Returns: Optional[List[Guid]]
        """
        return self._remove_licenses
    
    @remove_licenses.setter
    def remove_licenses(self,value: Optional[List[Guid]] = None) -> None:
        """
        Sets the removeLicenses property value. The removeLicenses property
        Args:
            value: Value to set for the removeLicenses property.
        """
        self._remove_licenses = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_object_values("addLicenses", self.add_licenses)
        writer.write_collection_of_primitive_values("removeLicenses", self.remove_licenses)
        writer.write_additional_data_value(self.additional_data)
    

