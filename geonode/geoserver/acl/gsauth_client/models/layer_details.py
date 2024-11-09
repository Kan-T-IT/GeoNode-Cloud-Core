# coding: utf-8

"""
    GeoServer ACL

    GeoServer Access Control List API  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from geonode.geoserver.acl.gsauth_client.configuration import Configuration


class LayerDetails(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name and the value is attribute type.
      attribute_map (dict): The key is attribute name and the value is json key in definition.
    """
    openapi_types = {
        'type': 'str',
        'default_style': 'str',
        'cql_filter_read': 'str',
        'cql_filter_write': 'str',
        'allowed_area': 'Geom',
        'spatial_filter_type': 'SpatialFilterType',
        'catalog_mode': 'CatalogMode',
        'allowed_styles': 'list[str]',
        'layer_attributes': 'list[LayerAttribute]'
    }

    attribute_map = {
        'type': 'type',
        'default_style': 'defaultStyle',
        'cql_filter_read': 'cqlFilterRead',
        'cql_filter_write': 'cqlFilterWrite',
        'allowed_area': 'allowedArea',
        'spatial_filter_type': 'spatialFilterType',
        'catalog_mode': 'catalogMode',
        'allowed_styles': 'allowedStyles',
        'layer_attributes': 'layerAttributes'
    }

    def __init__(self, type=None, default_style=None, cql_filter_read=None, cql_filter_write=None, allowed_area=None, spatial_filter_type=None, catalog_mode=None, allowed_styles=None, layer_attributes=None, local_vars_configuration=None):  # noqa: E501
        """LayerDetails - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._default_style = None
        self._cql_filter_read = None
        self._cql_filter_write = None
        self._allowed_area = None
        self._spatial_filter_type = None
        self._catalog_mode = None
        self._allowed_styles = None
        self._layer_attributes = None
        self.discriminator = None

        self.type = type
        self.default_style = default_style
        self.cql_filter_read = cql_filter_read
        self.cql_filter_write = cql_filter_write
        if allowed_area is not None:
            self.allowed_area = allowed_area
        self.spatial_filter_type = spatial_filter_type
        self.catalog_mode = catalog_mode
        self.allowed_styles = allowed_styles
        self.layer_attributes = layer_attributes

    @property
    def type(self):
        """Gets the type of this LayerDetails.  # noqa: E501


        :return: The type of this LayerDetails.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this LayerDetails.


        :param type: The type of this LayerDetails.  # noqa: E501
        :type type: str
        """
        allowed_values = [None,"VECTOR", "RASTER", "LAYERGROUP"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def default_style(self):
        """Gets the default_style of this LayerDetails.  # noqa: E501


        :return: The default_style of this LayerDetails.  # noqa: E501
        :rtype: str
        """
        return self._default_style

    @default_style.setter
    def default_style(self, default_style):
        """Sets the default_style of this LayerDetails.


        :param default_style: The default_style of this LayerDetails.  # noqa: E501
        :type default_style: str
        """

        self._default_style = default_style

    @property
    def cql_filter_read(self):
        """Gets the cql_filter_read of this LayerDetails.  # noqa: E501


        :return: The cql_filter_read of this LayerDetails.  # noqa: E501
        :rtype: str
        """
        return self._cql_filter_read

    @cql_filter_read.setter
    def cql_filter_read(self, cql_filter_read):
        """Sets the cql_filter_read of this LayerDetails.


        :param cql_filter_read: The cql_filter_read of this LayerDetails.  # noqa: E501
        :type cql_filter_read: str
        """

        self._cql_filter_read = cql_filter_read

    @property
    def cql_filter_write(self):
        """Gets the cql_filter_write of this LayerDetails.  # noqa: E501


        :return: The cql_filter_write of this LayerDetails.  # noqa: E501
        :rtype: str
        """
        return self._cql_filter_write

    @cql_filter_write.setter
    def cql_filter_write(self, cql_filter_write):
        """Sets the cql_filter_write of this LayerDetails.


        :param cql_filter_write: The cql_filter_write of this LayerDetails.  # noqa: E501
        :type cql_filter_write: str
        """

        self._cql_filter_write = cql_filter_write

    @property
    def allowed_area(self):
        """Gets the allowed_area of this LayerDetails.  # noqa: E501


        :return: The allowed_area of this LayerDetails.  # noqa: E501
        :rtype: Geom
        """
        return self._allowed_area

    @allowed_area.setter
    def allowed_area(self, allowed_area):
        """Sets the allowed_area of this LayerDetails.


        :param allowed_area: The allowed_area of this LayerDetails.  # noqa: E501
        :type allowed_area: Geom
        """

        self._allowed_area = allowed_area

    @property
    def spatial_filter_type(self):
        """Gets the spatial_filter_type of this LayerDetails.  # noqa: E501


        :return: The spatial_filter_type of this LayerDetails.  # noqa: E501
        :rtype: SpatialFilterType
        """
        return self._spatial_filter_type

    @spatial_filter_type.setter
    def spatial_filter_type(self, spatial_filter_type):
        """Sets the spatial_filter_type of this LayerDetails.


        :param spatial_filter_type: The spatial_filter_type of this LayerDetails.  # noqa: E501
        :type spatial_filter_type: SpatialFilterType
        """

        self._spatial_filter_type = spatial_filter_type

    @property
    def catalog_mode(self):
        """Gets the catalog_mode of this LayerDetails.  # noqa: E501


        :return: The catalog_mode of this LayerDetails.  # noqa: E501
        :rtype: CatalogMode
        """
        return self._catalog_mode

    @catalog_mode.setter
    def catalog_mode(self, catalog_mode):
        """Sets the catalog_mode of this LayerDetails.


        :param catalog_mode: The catalog_mode of this LayerDetails.  # noqa: E501
        :type catalog_mode: CatalogMode
        """

        self._catalog_mode = catalog_mode

    @property
    def allowed_styles(self):
        """Gets the allowed_styles of this LayerDetails.  # noqa: E501


        :return: The allowed_styles of this LayerDetails.  # noqa: E501
        :rtype: list[str]
        """
        return self._allowed_styles

    @allowed_styles.setter
    def allowed_styles(self, allowed_styles):
        """Sets the allowed_styles of this LayerDetails.


        :param allowed_styles: The allowed_styles of this LayerDetails.  # noqa: E501
        :type allowed_styles: list[str]
        """

        self._allowed_styles = allowed_styles

    @property
    def layer_attributes(self):
        """Gets the layer_attributes of this LayerDetails.  # noqa: E501


        :return: The layer_attributes of this LayerDetails.  # noqa: E501
        :rtype: list[LayerAttribute]
        """
        return self._layer_attributes

    @layer_attributes.setter
    def layer_attributes(self, layer_attributes):
        """Sets the layer_attributes of this LayerDetails.


        :param layer_attributes: The layer_attributes of this LayerDetails.  # noqa: E501
        :type layer_attributes: list[LayerAttribute]
        """

        self._layer_attributes = layer_attributes

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, LayerDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LayerDetails):
            return True

        return self.to_dict() != other.to_dict()
