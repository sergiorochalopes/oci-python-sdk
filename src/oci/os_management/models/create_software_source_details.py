# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateSoftwareSourceDetails(object):
    """
    Description of a software source to be created on the management system
    """

    #: A constant which can be used with the arch_type property of a CreateSoftwareSourceDetails.
    #: This constant has a value of "IA_32"
    ARCH_TYPE_IA_32 = "IA_32"

    #: A constant which can be used with the arch_type property of a CreateSoftwareSourceDetails.
    #: This constant has a value of "X86_64"
    ARCH_TYPE_X86_64 = "X86_64"

    #: A constant which can be used with the arch_type property of a CreateSoftwareSourceDetails.
    #: This constant has a value of "AARCH64"
    ARCH_TYPE_AARCH64 = "AARCH64"

    #: A constant which can be used with the arch_type property of a CreateSoftwareSourceDetails.
    #: This constant has a value of "SPARC"
    ARCH_TYPE_SPARC = "SPARC"

    #: A constant which can be used with the arch_type property of a CreateSoftwareSourceDetails.
    #: This constant has a value of "AMD64_DEBIAN"
    ARCH_TYPE_AMD64_DEBIAN = "AMD64_DEBIAN"

    #: A constant which can be used with the checksum_type property of a CreateSoftwareSourceDetails.
    #: This constant has a value of "SHA1"
    CHECKSUM_TYPE_SHA1 = "SHA1"

    #: A constant which can be used with the checksum_type property of a CreateSoftwareSourceDetails.
    #: This constant has a value of "SHA256"
    CHECKSUM_TYPE_SHA256 = "SHA256"

    #: A constant which can be used with the checksum_type property of a CreateSoftwareSourceDetails.
    #: This constant has a value of "SHA384"
    CHECKSUM_TYPE_SHA384 = "SHA384"

    #: A constant which can be used with the checksum_type property of a CreateSoftwareSourceDetails.
    #: This constant has a value of "SHA512"
    CHECKSUM_TYPE_SHA512 = "SHA512"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateSoftwareSourceDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateSoftwareSourceDetails.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateSoftwareSourceDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreateSoftwareSourceDetails.
        :type description: str

        :param arch_type:
            The value to assign to the arch_type property of this CreateSoftwareSourceDetails.
            Allowed values for this property are: "IA_32", "X86_64", "AARCH64", "SPARC", "AMD64_DEBIAN"
        :type arch_type: str

        :param maintainer_name:
            The value to assign to the maintainer_name property of this CreateSoftwareSourceDetails.
        :type maintainer_name: str

        :param maintainer_email:
            The value to assign to the maintainer_email property of this CreateSoftwareSourceDetails.
        :type maintainer_email: str

        :param maintainer_phone:
            The value to assign to the maintainer_phone property of this CreateSoftwareSourceDetails.
        :type maintainer_phone: str

        :param checksum_type:
            The value to assign to the checksum_type property of this CreateSoftwareSourceDetails.
            Allowed values for this property are: "SHA1", "SHA256", "SHA384", "SHA512"
        :type checksum_type: str

        :param parent_id:
            The value to assign to the parent_id property of this CreateSoftwareSourceDetails.
        :type parent_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateSoftwareSourceDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateSoftwareSourceDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'description': 'str',
            'arch_type': 'str',
            'maintainer_name': 'str',
            'maintainer_email': 'str',
            'maintainer_phone': 'str',
            'checksum_type': 'str',
            'parent_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'description': 'description',
            'arch_type': 'archType',
            'maintainer_name': 'maintainerName',
            'maintainer_email': 'maintainerEmail',
            'maintainer_phone': 'maintainerPhone',
            'checksum_type': 'checksumType',
            'parent_id': 'parentId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._compartment_id = None
        self._display_name = None
        self._description = None
        self._arch_type = None
        self._maintainer_name = None
        self._maintainer_email = None
        self._maintainer_phone = None
        self._checksum_type = None
        self._parent_id = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateSoftwareSourceDetails.
        OCID for the Compartment


        :return: The compartment_id of this CreateSoftwareSourceDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateSoftwareSourceDetails.
        OCID for the Compartment


        :param compartment_id: The compartment_id of this CreateSoftwareSourceDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateSoftwareSourceDetails.
        User friendly name for the software source


        :return: The display_name of this CreateSoftwareSourceDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateSoftwareSourceDetails.
        User friendly name for the software source


        :param display_name: The display_name of this CreateSoftwareSourceDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this CreateSoftwareSourceDetails.
        Information specified by the user about the software source


        :return: The description of this CreateSoftwareSourceDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateSoftwareSourceDetails.
        Information specified by the user about the software source


        :param description: The description of this CreateSoftwareSourceDetails.
        :type: str
        """
        self._description = description

    @property
    def arch_type(self):
        """
        **[Required]** Gets the arch_type of this CreateSoftwareSourceDetails.
        The architecture type supported by the Software Source

        Allowed values for this property are: "IA_32", "X86_64", "AARCH64", "SPARC", "AMD64_DEBIAN"


        :return: The arch_type of this CreateSoftwareSourceDetails.
        :rtype: str
        """
        return self._arch_type

    @arch_type.setter
    def arch_type(self, arch_type):
        """
        Sets the arch_type of this CreateSoftwareSourceDetails.
        The architecture type supported by the Software Source


        :param arch_type: The arch_type of this CreateSoftwareSourceDetails.
        :type: str
        """
        allowed_values = ["IA_32", "X86_64", "AARCH64", "SPARC", "AMD64_DEBIAN"]
        if not value_allowed_none_or_none_sentinel(arch_type, allowed_values):
            raise ValueError(
                "Invalid value for `arch_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._arch_type = arch_type

    @property
    def maintainer_name(self):
        """
        Gets the maintainer_name of this CreateSoftwareSourceDetails.
        Name of the person maintaining this software source


        :return: The maintainer_name of this CreateSoftwareSourceDetails.
        :rtype: str
        """
        return self._maintainer_name

    @maintainer_name.setter
    def maintainer_name(self, maintainer_name):
        """
        Sets the maintainer_name of this CreateSoftwareSourceDetails.
        Name of the person maintaining this software source


        :param maintainer_name: The maintainer_name of this CreateSoftwareSourceDetails.
        :type: str
        """
        self._maintainer_name = maintainer_name

    @property
    def maintainer_email(self):
        """
        Gets the maintainer_email of this CreateSoftwareSourceDetails.
        Email address of the person maintaining this software source


        :return: The maintainer_email of this CreateSoftwareSourceDetails.
        :rtype: str
        """
        return self._maintainer_email

    @maintainer_email.setter
    def maintainer_email(self, maintainer_email):
        """
        Sets the maintainer_email of this CreateSoftwareSourceDetails.
        Email address of the person maintaining this software source


        :param maintainer_email: The maintainer_email of this CreateSoftwareSourceDetails.
        :type: str
        """
        self._maintainer_email = maintainer_email

    @property
    def maintainer_phone(self):
        """
        Gets the maintainer_phone of this CreateSoftwareSourceDetails.
        Phone number of the person maintaining this software source


        :return: The maintainer_phone of this CreateSoftwareSourceDetails.
        :rtype: str
        """
        return self._maintainer_phone

    @maintainer_phone.setter
    def maintainer_phone(self, maintainer_phone):
        """
        Sets the maintainer_phone of this CreateSoftwareSourceDetails.
        Phone number of the person maintaining this software source


        :param maintainer_phone: The maintainer_phone of this CreateSoftwareSourceDetails.
        :type: str
        """
        self._maintainer_phone = maintainer_phone

    @property
    def checksum_type(self):
        """
        Gets the checksum_type of this CreateSoftwareSourceDetails.
        The yum repository checksum type used by this software source

        Allowed values for this property are: "SHA1", "SHA256", "SHA384", "SHA512"


        :return: The checksum_type of this CreateSoftwareSourceDetails.
        :rtype: str
        """
        return self._checksum_type

    @checksum_type.setter
    def checksum_type(self, checksum_type):
        """
        Sets the checksum_type of this CreateSoftwareSourceDetails.
        The yum repository checksum type used by this software source


        :param checksum_type: The checksum_type of this CreateSoftwareSourceDetails.
        :type: str
        """
        allowed_values = ["SHA1", "SHA256", "SHA384", "SHA512"]
        if not value_allowed_none_or_none_sentinel(checksum_type, allowed_values):
            raise ValueError(
                "Invalid value for `checksum_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._checksum_type = checksum_type

    @property
    def parent_id(self):
        """
        Gets the parent_id of this CreateSoftwareSourceDetails.
        OCID for the parent software source, if there is one


        :return: The parent_id of this CreateSoftwareSourceDetails.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """
        Sets the parent_id of this CreateSoftwareSourceDetails.
        OCID for the parent software source, if there is one


        :param parent_id: The parent_id of this CreateSoftwareSourceDetails.
        :type: str
        """
        self._parent_id = parent_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateSoftwareSourceDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateSoftwareSourceDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateSoftwareSourceDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateSoftwareSourceDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateSoftwareSourceDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateSoftwareSourceDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateSoftwareSourceDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateSoftwareSourceDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
