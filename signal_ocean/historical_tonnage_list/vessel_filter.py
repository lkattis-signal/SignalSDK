# noqa: D100

from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import List, Iterable, Optional

from .vessel import Vessel
from .vessel_subclass import VesselSubclass


@dataclass(eq=False)
class VesselFilter:
    """Enables vessel filtering in a Historical Tonnage List query.

    All attributes in this class are optional, i.e. no filtering will be
    performed on attributes whose value is None.

    Attributes that accept a list of values are used to perform an *OR*
    comparison. In other words, when a non-empty list of values is used,
    the Historical Tonnage List will contain vessels that match on **any**
    of the specified values. Using an empty list will result in no filtering
    at all.

    VesselFilter is mutable in order to allow making adjustments to
    existing instances if query results are unsatisfactory.

    Attributes:
        push_types: Return vessels with the specified push types.
            Use constants defined in the PushType class for the values of
            this attribute.
        market_deployments: Return vessels with the specified market
            deployment types. Use constants defined in the MarketDeployment
            class for the values of this attribute.
        commercial_statuses: Return vessels with the specified
            commercial statuses. Use constants defined in the CommercialStatus
            class for the values of this attribute.
        vessel_subclass: Return vessels of the specified subclass.
            Use constants defined in the VesselSubclass class for the values
            of this attribute.
        add_willing_to_switch_subclass: When True, returns vessels
            that do not match the subclass but are willing to switch to it.
        latest_ais_since: The maximum age, in days, of the vessel's
            AIS information at the time the tonnage list was captured.
        operational_statuses: Return vessels with the specified
            operational statuses. Use constants defined in the
            OperationalStatus class for the values of this attribute.
        min_liquid_capacity: The minimum liquid capacity, in cubic
            meters, the vessel should be able to hold.
        max_liquid_capacity: The maximum liquid capacity, in cubic
            meters, the vessel should be able to hold.
        fixture_types: Return vessels with the specified
            fixture types. Use constants defined in the FixtureType class for
            the values of this attribute.
        last_cargo_types: Return vessels with the specified last
            cargo type IDs.
    """
    push_types: Optional[List[str]] = field(default_factory=list)
    market_deployments: Optional[List[str]] = field(default_factory=list)
    commercial_statuses: Optional[List[str]] = field(default_factory=list)
    vessel_subclass: Optional[str] = VesselSubclass.ALL
    add_willing_to_switch_subclass: Optional[bool] = False
    latest_ais_since: Optional[int] = None
    operational_statuses: Optional[List[str]] = field(default_factory=list)
    min_liquid_capacity: Optional[int] = None
    max_liquid_capacity: Optional[int] = None
    fixture_types: Optional[List[str]] = field(default_factory=list)

    def _to_query_string(self) -> dict:
        return {
            'pushType': self.push_types,
            'commercialStatus': self.commercial_statuses,
            'latestAisSince': self.latest_ais_since,
            'vesselSubclass': self.vessel_subclass,
            'addWillingToSwitchSubclass': self.add_willing_to_switch_subclass,
            'marketDeployment': self.market_deployments,
            'operationalStatus': self.operational_statuses,
            'minLiquidCapacity': self.min_liquid_capacity,
            'maxLiquidCapacity': self.max_liquid_capacity,
            'fixtureType': self.fixture_types
        }
