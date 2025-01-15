from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..access_review_set import AccessReviewSet
    from ..app_consent_approval_route import AppConsentApprovalRoute
    from ..entitlement_management import EntitlementManagement
    from ..privileged_access_root import PrivilegedAccessRoot
    from ..terms_of_use_container import TermsOfUseContainer
    from .lifecycle_workflows_container import LifecycleWorkflowsContainer

@dataclass
class IdentityGovernance(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The accessReviews property
    access_reviews: Optional[AccessReviewSet] = None
    # The appConsent property
    app_consent: Optional[AppConsentApprovalRoute] = None
    # The entitlementManagement property
    entitlement_management: Optional[EntitlementManagement] = None
    # The lifecycleWorkflows property
    lifecycle_workflows: Optional[LifecycleWorkflowsContainer] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The privilegedAccess property
    privileged_access: Optional[PrivilegedAccessRoot] = None
    # The termsOfUse property
    terms_of_use: Optional[TermsOfUseContainer] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IdentityGovernance:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IdentityGovernance
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return IdentityGovernance()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..access_review_set import AccessReviewSet
        from ..app_consent_approval_route import AppConsentApprovalRoute
        from ..entitlement_management import EntitlementManagement
        from ..privileged_access_root import PrivilegedAccessRoot
        from ..terms_of_use_container import TermsOfUseContainer
        from .lifecycle_workflows_container import LifecycleWorkflowsContainer

        from ..access_review_set import AccessReviewSet
        from ..app_consent_approval_route import AppConsentApprovalRoute
        from ..entitlement_management import EntitlementManagement
        from ..privileged_access_root import PrivilegedAccessRoot
        from ..terms_of_use_container import TermsOfUseContainer
        from .lifecycle_workflows_container import LifecycleWorkflowsContainer

        fields: dict[str, Callable[[Any], None]] = {
            "accessReviews": lambda n : setattr(self, 'access_reviews', n.get_object_value(AccessReviewSet)),
            "appConsent": lambda n : setattr(self, 'app_consent', n.get_object_value(AppConsentApprovalRoute)),
            "entitlementManagement": lambda n : setattr(self, 'entitlement_management', n.get_object_value(EntitlementManagement)),
            "lifecycleWorkflows": lambda n : setattr(self, 'lifecycle_workflows', n.get_object_value(LifecycleWorkflowsContainer)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "privilegedAccess": lambda n : setattr(self, 'privileged_access', n.get_object_value(PrivilegedAccessRoot)),
            "termsOfUse": lambda n : setattr(self, 'terms_of_use', n.get_object_value(TermsOfUseContainer)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_object_value("accessReviews", self.access_reviews)
        writer.write_object_value("appConsent", self.app_consent)
        writer.write_object_value("entitlementManagement", self.entitlement_management)
        writer.write_object_value("lifecycleWorkflows", self.lifecycle_workflows)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("privilegedAccess", self.privileged_access)
        writer.write_object_value("termsOfUse", self.terms_of_use)
        writer.write_additional_data_value(self.additional_data)
    

