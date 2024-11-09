#########################################################################
#
# Copyright (C) 2021 OSGeo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#########################################################################

from rest_framework.routers import (
    DynamicRoute,
    Route,
)
from rest_framework_extensions.routers import ExtendedSimpleRouter


class ListPatchRouter(ExtendedSimpleRouter):
    """
    A router that enables PATCH requests on the `list` endpoint.

    This router is designed to provide API endpoints that accept PATCH requests targeting a viewset's `list` endpoint. It is useful for batch updates on multiple resources.

    **Use case example:**
    Consider the scenario of selecting remote resources for harvesting by the local GeoNode:

    1. The user views a (paginated) list of resources available on the remote service.
    2. The user then selects which resources should be harvested.
    3. Instead of requiring multiple PATCH requests for each individual resource's detail page to update the `should_be_harvested` property, the user can make a single PATCH request to `harvesters/{harvester-id}/harvestable-resources` to update the `should_be_harvested` property on multiple resources simultaneously.
    """

    routes = [
        # List route.
        Route(
            url=r"^{prefix}{trailing_slash}$",
            mapping={
                "get": "list",
                "post": "create",
                "patch": "update_list",
            },
            name="{basename}-list",
            detail=False,
            initkwargs={"suffix": "List"},
        ),
        # Dynamically generated list routes. Generated using
        # @action(detail=False) decorator on methods of the viewset.
        DynamicRoute(
            url=r"^{prefix}/{url_path}{trailing_slash}$", name="{basename}-{url_name}", detail=False, initkwargs={}
        ),
        # Detail route.
        Route(
            url=r"^{prefix}/{lookup}{trailing_slash}$",
            mapping={"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"},
            name="{basename}-detail",
            detail=True,
            initkwargs={"suffix": "Instance"},
        ),
        # Dynamically generated detail routes. Generated using
        # @action(detail=True) decorator on methods of the viewset.
        DynamicRoute(
            url=r"^{prefix}/{lookup}/{url_path}{trailing_slash}$",
            name="{basename}-{url_name}",
            detail=True,
            initkwargs={},
        ),
    ]
