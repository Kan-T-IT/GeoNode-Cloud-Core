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


class Rule(object):
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
        'id': 'str',
        'priority': 'int',
        'ext_id': 'str',
        'name': 'str',
        'description': 'str',
        'instance': 'str',
        'access': 'GrantType',
        'limits': 'RuleLimits',
        'role': 'str',
        'user': 'str',
        'address_range': 'str',
        'service': 'str',
        'request': 'str',
        'subfield': 'str',
        'workspace': 'str',
        'layer': 'str'
    }

    attribute_map = {
        'id': 'id',
        'priority': 'priority',
        'ext_id': 'extId',
        'name': 'name',
        'description': 'description',
        'instance': 'instance',
        'access': 'access',
        'limits': 'limits',
        'role': 'role',
        'user': 'user',
        'address_range': 'addressRange',
        'service': 'service',
        'request': 'request',
        'subfield': 'subfield',
        'workspace': 'workspace',
        'layer': 'layer'
    }

    def __init__(self, id=None, priority=None, ext_id=None, name=None, description=None, instance=None, access=None, limits=None, role=None, user=None, address_range=None, service=None, request=None, subfield=None, workspace=None, layer=None, local_vars_configuration=None):  # noqa: E501
        """Rule - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._priority = None
        self._ext_id = None
        self._name = None
        self._description = None
        self._instance = None
        self._access = None
        self._limits = None
        self._role = None
        self._user = None
        self._address_range = None
        self._service = None
        self._request = None
        self._subfield = None
        self._workspace = None
        self._layer = None
        self.discriminator = None

        self.id = id
        self.priority = priority
        self.ext_id = ext_id
        self.name = name
        self.description = description
        self.instance = instance
        self.access = access
        self.limits = limits
        self.role = role
        self.user = user
        self.address_range = address_range
        self.service = service
        self.request = request
        self.subfield = subfield
        self.workspace = workspace
        self.layer = layer

    @property
    def id(self):
        """Gets the id of this Rule.  # noqa: E501


        :return: The id of this Rule.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Rule.


        :param id: The id of this Rule.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def priority(self):
        """Gets the priority of this Rule.  # noqa: E501


        :return: The priority of this Rule.  # noqa: E501
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this Rule.


        :param priority: The priority of this Rule.  # noqa: E501
        :type priority: int
        """
        if self.local_vars_configuration.client_side_validation and priority is None:  # noqa: E501
            raise ValueError("Invalid value for `priority`, must not be `None`")  # noqa: E501

        self._priority = priority

    @property
    def ext_id(self):
        """Gets the ext_id of this Rule.  # noqa: E501


        :return: The ext_id of this Rule.  # noqa: E501
        :rtype: str
        """
        return self._ext_id

    @ext_id.setter
    def ext_id(self, ext_id):
        """Sets the ext_id of this Rule.


        :param ext_id: The ext_id of this Rule.  # noqa: E501
        :type ext_id: str
        """

        self._ext_id = ext_id

    @property
    def name(self):
        """Gets the name of this Rule.  # noqa: E501


        :return: The name of this Rule.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Rule.


        :param name: The name of this Rule.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this Rule.  # noqa: E501


        :return: The description of this Rule.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Rule.


        :param description: The description of this Rule.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def instance(self):
        """Gets the instance of this Rule.  # noqa: E501


        :return: The instance of this Rule.  # noqa: E501
        :rtype: str
        """
        return self._instance

    @instance.setter
    def instance(self, instance):
        """Sets the instance of this Rule.


        :param instance: The instance of this Rule.  # noqa: E501
        :type instance: str
        """

        self._instance = instance

    @property
    def access(self):
        """Gets the access of this Rule.  # noqa: E501


        :return: The access of this Rule.  # noqa: E501
        :rtype: GrantType
        """
        return self._access

    @access.setter
    def access(self, access):
        """Sets the access of this Rule.


        :param access: The access of this Rule.  # noqa: E501
        :type access: GrantType
        """

        self._access = access

    @property
    def limits(self):
        """Gets the limits of this Rule.  # noqa: E501


        :return: The limits of this Rule.  # noqa: E501
        :rtype: RuleLimits
        """
        return self._limits

    @limits.setter
    def limits(self, limits):
        """Sets the limits of this Rule.


        :param limits: The limits of this Rule.  # noqa: E501
        :type limits: RuleLimits
        """

        self._limits = limits

    @property
    def role(self):
        """Gets the role of this Rule.  # noqa: E501


        :return: The role of this Rule.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this Rule.


        :param role: The role of this Rule.  # noqa: E501
        :type role: str
        """

        self._role = role

    @property
    def user(self):
        """Gets the user of this Rule.  # noqa: E501


        :return: The user of this Rule.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this Rule.


        :param user: The user of this Rule.  # noqa: E501
        :type user: str
        """

        self._user = user

    @property
    def address_range(self):
        """Gets the address_range of this Rule.  # noqa: E501

        IPv4 address with optional /nn on the end with values from 0 - 32  # noqa: E501

        :return: The address_range of this Rule.  # noqa: E501
        :rtype: str
        """
        return self._address_range

    @address_range.setter
    def address_range(self, address_range):
        """Sets the address_range of this Rule.

        IPv4 address with optional /nn on the end with values from 0 - 32  # noqa: E501

        :param address_range: The address_range of this Rule.  # noqa: E501
        :type address_range: str
        """
        if (self.local_vars_configuration.client_side_validation and
                address_range is not None and not re.search(r'^([0-9]{1,3}\.){3}[0-9]{1,3}(\/([0-9]|[1-2][0-9]|3[0-2]))?$', address_range)):  # noqa: E501
            raise ValueError(r"Invalid value for `address_range`, must be a follow pattern or equal to `/^([0-9]{1,3}\.){3}[0-9]{1,3}(\/([0-9]|[1-2][0-9]|3[0-2]))?$/`")  # noqa: E501

        self._address_range = address_range

    @property
    def service(self):
        """Gets the service of this Rule.  # noqa: E501


        :return: The service of this Rule.  # noqa: E501
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this Rule.


        :param service: The service of this Rule.  # noqa: E501
        :type service: str
        """

        self._service = service

    @property
    def request(self):
        """Gets the request of this Rule.  # noqa: E501


        :return: The request of this Rule.  # noqa: E501
        :rtype: str
        """
        return self._request

    @request.setter
    def request(self, request):
        """Sets the request of this Rule.


        :param request: The request of this Rule.  # noqa: E501
        :type request: str
        """

        self._request = request

    @property
    def subfield(self):
        """Gets the subfield of this Rule.  # noqa: E501


        :return: The subfield of this Rule.  # noqa: E501
        :rtype: str
        """
        return self._subfield

    @subfield.setter
    def subfield(self, subfield):
        """Sets the subfield of this Rule.


        :param subfield: The subfield of this Rule.  # noqa: E501
        :type subfield: str
        """

        self._subfield = subfield

    @property
    def workspace(self):
        """Gets the workspace of this Rule.  # noqa: E501


        :return: The workspace of this Rule.  # noqa: E501
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this Rule.


        :param workspace: The workspace of this Rule.  # noqa: E501
        :type workspace: str
        """

        self._workspace = workspace

    @property
    def layer(self):
        """Gets the layer of this Rule.  # noqa: E501


        :return: The layer of this Rule.  # noqa: E501
        :rtype: str
        """
        return self._layer

    @layer.setter
    def layer(self, layer):
        """Sets the layer of this Rule.


        :param layer: The layer of this Rule.  # noqa: E501
        :type layer: str
        """

        self._layer = layer

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
        if not isinstance(other, Rule):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Rule):
            return True

        return self.to_dict() != other.to_dict()
