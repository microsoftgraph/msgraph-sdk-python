from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .agreement_acceptance import AgreementAcceptance
    from .agreement_file import AgreementFile
    from .agreement_file_localization import AgreementFileLocalization
    from .entity import Entity
    from .terms_expiration import TermsExpiration

from .entity import Entity

@dataclass
class Agreement(Entity, Parsable):
    # Read-only. Information about acceptances of this agreement.
    acceptances: Optional[list[AgreementAcceptance]] = None
    # Display name of the agreement. The display name is used for internal tracking of the agreement but isn't shown to end users who view the agreement. Supports $filter (eq).
    display_name: Optional[str] = None
    # Default PDF linked to this agreement.
    file: Optional[AgreementFile] = None
    # PDFs linked to this agreement. This property is in the process of being deprecated. Use the  file property instead. Supports $expand.
    files: Optional[list[AgreementFileLocalization]] = None
    # Indicates whether end users are required to accept this agreement on every device that they access it from. The end user is required to register their device in Microsoft Entra ID, if they haven't already done so. Supports $filter (eq).
    is_per_device_acceptance_required: Optional[bool] = None
    # Indicates whether the user has to expand the agreement before accepting. Supports $filter (eq).
    is_viewing_before_acceptance_required: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Expiration schedule and frequency of agreement for all users. Supports $filter (eq).
    terms_expiration: Optional[TermsExpiration] = None
    # The duration after which the user must reaccept the terms of use. The value is represented in ISO 8601 format for durations. Supports $filter (eq).
    user_reaccept_required_frequency: Optional[datetime.timedelta] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Agreement:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Agreement
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Agreement()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .agreement_acceptance import AgreementAcceptance
        from .agreement_file import AgreementFile
        from .agreement_file_localization import AgreementFileLocalization
        from .entity import Entity
        from .terms_expiration import TermsExpiration

        from .agreement_acceptance import AgreementAcceptance
        from .agreement_file import AgreementFile
        from .agreement_file_localization import AgreementFileLocalization
        from .entity import Entity
        from .terms_expiration import TermsExpiration

        fields: dict[str, Callable[[Any], None]] = {
            "acceptances": lambda n : setattr(self, 'acceptances', n.get_collection_of_object_values(AgreementAcceptance)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "file": lambda n : setattr(self, 'file', n.get_object_value(AgreementFile)),
            "files": lambda n : setattr(self, 'files', n.get_collection_of_object_values(AgreementFileLocalization)),
            "isPerDeviceAcceptanceRequired": lambda n : setattr(self, 'is_per_device_acceptance_required', n.get_bool_value()),
            "isViewingBeforeAcceptanceRequired": lambda n : setattr(self, 'is_viewing_before_acceptance_required', n.get_bool_value()),
            "termsExpiration": lambda n : setattr(self, 'terms_expiration', n.get_object_value(TermsExpiration)),
            "userReacceptRequiredFrequency": lambda n : setattr(self, 'user_reaccept_required_frequency', n.get_timedelta_value()),
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
        writer.write_collection_of_object_values("acceptances", self.acceptances)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("file", self.file)
        writer.write_collection_of_object_values("files", self.files)
        writer.write_bool_value("isPerDeviceAcceptanceRequired", self.is_per_device_acceptance_required)
        writer.write_bool_value("isViewingBeforeAcceptanceRequired", self.is_viewing_before_acceptance_required)
        writer.write_object_value("termsExpiration", self.terms_expiration)
        writer.write_timedelta_value("userReacceptRequiredFrequency", self.user_reaccept_required_frequency)
    

