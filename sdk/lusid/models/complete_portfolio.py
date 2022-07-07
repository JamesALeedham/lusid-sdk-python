# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.4575
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from lusid.configuration import Configuration


class CompletePortfolio(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'id': 'ResourceId',
        'href': 'str',
        'description': 'str',
        'display_name': 'str',
        'created': 'datetime',
        'parent_portfolio_id': 'ResourceId',
        'is_derived': 'bool',
        'type': 'str',
        'version': 'Version',
        'properties': 'list[ModelProperty]',
        'base_currency': 'str',
        'links': 'list[Link]'
    }

    attribute_map = {
        'id': 'id',
        'href': 'href',
        'description': 'description',
        'display_name': 'displayName',
        'created': 'created',
        'parent_portfolio_id': 'parentPortfolioId',
        'is_derived': 'isDerived',
        'type': 'type',
        'version': 'version',
        'properties': 'properties',
        'base_currency': 'baseCurrency',
        'links': 'links'
    }

    required_map = {
        'id': 'required',
        'href': 'optional',
        'description': 'optional',
        'display_name': 'optional',
        'created': 'optional',
        'parent_portfolio_id': 'optional',
        'is_derived': 'optional',
        'type': 'optional',
        'version': 'required',
        'properties': 'optional',
        'base_currency': 'optional',
        'links': 'optional'
    }

    def __init__(self, id=None, href=None, description=None, display_name=None, created=None, parent_portfolio_id=None, is_derived=None, type=None, version=None, properties=None, base_currency=None, links=None, local_vars_configuration=None):  # noqa: E501
        """CompletePortfolio - a model defined in OpenAPI"
        
        :param id:  (required)
        :type id: lusid.ResourceId
        :param href:  The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
        :type href: str
        :param description:  The long form description of the portfolio.
        :type description: str
        :param display_name:  The name of the portfolio.
        :type display_name: str
        :param created:  The effective datetime at which the portfolio was created. No transactions or constituents can be added to the portfolio before this date.
        :type created: datetime
        :param parent_portfolio_id: 
        :type parent_portfolio_id: lusid.ResourceId
        :param is_derived:  Whether or not this is a derived portfolio.
        :type is_derived: bool
        :param type:  The type of the portfolio. The available values are: Transaction, Reference, DerivedTransaction
        :type type: str
        :param version:  (required)
        :type version: lusid.Version
        :param properties:  The requested portfolio properties. These will be from the 'Portfolio' domain.
        :type properties: list[lusid.ModelProperty]
        :param base_currency:  If the portfolio is a transaction portfolio or derived transaction portfolio, this is the base currency of the portfolio.
        :type base_currency: str
        :param links:  Collection of links.
        :type links: list[lusid.Link]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._href = None
        self._description = None
        self._display_name = None
        self._created = None
        self._parent_portfolio_id = None
        self._is_derived = None
        self._type = None
        self._version = None
        self._properties = None
        self._base_currency = None
        self._links = None
        self.discriminator = None

        self.id = id
        self.href = href
        self.description = description
        self.display_name = display_name
        if created is not None:
            self.created = created
        if parent_portfolio_id is not None:
            self.parent_portfolio_id = parent_portfolio_id
        if is_derived is not None:
            self.is_derived = is_derived
        if type is not None:
            self.type = type
        self.version = version
        self.properties = properties
        self.base_currency = base_currency
        self.links = links

    @property
    def id(self):
        """Gets the id of this CompletePortfolio.  # noqa: E501


        :return: The id of this CompletePortfolio.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CompletePortfolio.


        :param id: The id of this CompletePortfolio.  # noqa: E501
        :type id: lusid.ResourceId
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def href(self):
        """Gets the href of this CompletePortfolio.  # noqa: E501

        The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.  # noqa: E501

        :return: The href of this CompletePortfolio.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this CompletePortfolio.

        The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.  # noqa: E501

        :param href: The href of this CompletePortfolio.  # noqa: E501
        :type href: str
        """

        self._href = href

    @property
    def description(self):
        """Gets the description of this CompletePortfolio.  # noqa: E501

        The long form description of the portfolio.  # noqa: E501

        :return: The description of this CompletePortfolio.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CompletePortfolio.

        The long form description of the portfolio.  # noqa: E501

        :param description: The description of this CompletePortfolio.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def display_name(self):
        """Gets the display_name of this CompletePortfolio.  # noqa: E501

        The name of the portfolio.  # noqa: E501

        :return: The display_name of this CompletePortfolio.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this CompletePortfolio.

        The name of the portfolio.  # noqa: E501

        :param display_name: The display_name of this CompletePortfolio.  # noqa: E501
        :type display_name: str
        """

        self._display_name = display_name

    @property
    def created(self):
        """Gets the created of this CompletePortfolio.  # noqa: E501

        The effective datetime at which the portfolio was created. No transactions or constituents can be added to the portfolio before this date.  # noqa: E501

        :return: The created of this CompletePortfolio.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this CompletePortfolio.

        The effective datetime at which the portfolio was created. No transactions or constituents can be added to the portfolio before this date.  # noqa: E501

        :param created: The created of this CompletePortfolio.  # noqa: E501
        :type created: datetime
        """

        self._created = created

    @property
    def parent_portfolio_id(self):
        """Gets the parent_portfolio_id of this CompletePortfolio.  # noqa: E501


        :return: The parent_portfolio_id of this CompletePortfolio.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._parent_portfolio_id

    @parent_portfolio_id.setter
    def parent_portfolio_id(self, parent_portfolio_id):
        """Sets the parent_portfolio_id of this CompletePortfolio.


        :param parent_portfolio_id: The parent_portfolio_id of this CompletePortfolio.  # noqa: E501
        :type parent_portfolio_id: lusid.ResourceId
        """

        self._parent_portfolio_id = parent_portfolio_id

    @property
    def is_derived(self):
        """Gets the is_derived of this CompletePortfolio.  # noqa: E501

        Whether or not this is a derived portfolio.  # noqa: E501

        :return: The is_derived of this CompletePortfolio.  # noqa: E501
        :rtype: bool
        """
        return self._is_derived

    @is_derived.setter
    def is_derived(self, is_derived):
        """Sets the is_derived of this CompletePortfolio.

        Whether or not this is a derived portfolio.  # noqa: E501

        :param is_derived: The is_derived of this CompletePortfolio.  # noqa: E501
        :type is_derived: bool
        """

        self._is_derived = is_derived

    @property
    def type(self):
        """Gets the type of this CompletePortfolio.  # noqa: E501

        The type of the portfolio. The available values are: Transaction, Reference, DerivedTransaction  # noqa: E501

        :return: The type of this CompletePortfolio.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CompletePortfolio.

        The type of the portfolio. The available values are: Transaction, Reference, DerivedTransaction  # noqa: E501

        :param type: The type of this CompletePortfolio.  # noqa: E501
        :type type: str
        """
        allowed_values = ["Transaction", "Reference", "DerivedTransaction"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def version(self):
        """Gets the version of this CompletePortfolio.  # noqa: E501


        :return: The version of this CompletePortfolio.  # noqa: E501
        :rtype: lusid.Version
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this CompletePortfolio.


        :param version: The version of this CompletePortfolio.  # noqa: E501
        :type version: lusid.Version
        """
        if self.local_vars_configuration.client_side_validation and version is None:  # noqa: E501
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

    @property
    def properties(self):
        """Gets the properties of this CompletePortfolio.  # noqa: E501

        The requested portfolio properties. These will be from the 'Portfolio' domain.  # noqa: E501

        :return: The properties of this CompletePortfolio.  # noqa: E501
        :rtype: list[lusid.ModelProperty]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this CompletePortfolio.

        The requested portfolio properties. These will be from the 'Portfolio' domain.  # noqa: E501

        :param properties: The properties of this CompletePortfolio.  # noqa: E501
        :type properties: list[lusid.ModelProperty]
        """

        self._properties = properties

    @property
    def base_currency(self):
        """Gets the base_currency of this CompletePortfolio.  # noqa: E501

        If the portfolio is a transaction portfolio or derived transaction portfolio, this is the base currency of the portfolio.  # noqa: E501

        :return: The base_currency of this CompletePortfolio.  # noqa: E501
        :rtype: str
        """
        return self._base_currency

    @base_currency.setter
    def base_currency(self, base_currency):
        """Sets the base_currency of this CompletePortfolio.

        If the portfolio is a transaction portfolio or derived transaction portfolio, this is the base currency of the portfolio.  # noqa: E501

        :param base_currency: The base_currency of this CompletePortfolio.  # noqa: E501
        :type base_currency: str
        """

        self._base_currency = base_currency

    @property
    def links(self):
        """Gets the links of this CompletePortfolio.  # noqa: E501

        Collection of links.  # noqa: E501

        :return: The links of this CompletePortfolio.  # noqa: E501
        :rtype: list[lusid.Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this CompletePortfolio.

        Collection of links.  # noqa: E501

        :param links: The links of this CompletePortfolio.  # noqa: E501
        :type links: list[lusid.Link]
        """

        self._links = links

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
        if not isinstance(other, CompletePortfolio):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CompletePortfolio):
            return True

        return self.to_dict() != other.to_dict()
