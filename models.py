"""Represent models for near-Earth objects and their close approaches.

The `NearEarthObject` class represents a near-Earth object. Each has a
unique primary designation, an optional unique name, an optional
diameter, and a flag for whether the object is potentially hazardous.

The `CloseApproach` class represents a close approach to Earth by an
NEO. Each has an approach datetime, a nominal approach distance, and a
relative approach velocity.

A `NearEarthObject` maintains a collection of its close approaches,
and a `CloseApproach` maintains a reference to its NEO.

The functions that construct these objects use information extracted
from the data files from NASA, so these objects should be able to
handle all of the quirks of the data set, such as missing names and
unknown diameters.

You'll edit this file in Task 1.
"""
from helpers import cd_to_datetime, datetime_to_str


class NearEarthObject:
    """A near-Earth object (NEO).

    An NEO encapsulates semantic and physical parameters about the
    object, such as its primary designation (required, unique), IAU name
    (optional), diameter in kilometers (optional - sometimes unknown),
    and whether it's marked as potentially hazardous to Earth.

    A `NearEarthObject` also maintains a collection of its close
    approaches -initialized to an empty collection, but eventually
    populated in the `NEODatabase` constructor.
    """
    def __init__(self, designation, name, diameter, hazardous, **info):
        """
        Create a new `NearEarthObject`.

        :param designation: The primary designation for this
        `NearEarthObject`.
        :param name: The IAU name for this `NearEarthObject`.
        :param diameter: The diameter, in kilometers, of this
        `NearEarthObject`.
        :param hazardous: Whether or not this `NearEarthObject` is
        potentially hazardous.
        :param info: A dictionary of excess keyword arguments supplied
        to the constructor.
        """
        self.designation = str(designation)
        if name == '':
            self.name = None
        else:
            self.name = str(name)
        if diameter == '':
            self.diameter = float('nan')
        else:
            self.diameter = float(diameter)
        if hazardous == 'Y':
            self.hazardous = True
        else:
            self.hazardous = False

        # Create an empty initial collection of linked approaches.
        self.approaches = []

    @property
    def fullname(self):
        """
        Return a representation of the full name of this NEO.

        :param self: 'NearEarthObject' to call on designation and name
        attributes.
        :return: The string combination of designation and name,
        full name.
        """
        return f"{self.designation} {self.name}"

    def __str__(self):
        """
        Return a string describing the 'NearEarthObject' to be used
        when printing to terminal.

        :param self: 'NearEarthObject' to call on designation and name
        attributes.
        :return: The description of the 'NearEarthObject' by combining
        various attributes in to a human readable string output.
        """
        return (
            f"A NearEarthObject(designation={self.designation}, "
            f" name={self.name}, "
            f"diameter={self.diameter}, hazardous={self.hazardous})"
        )

    def __repr__(self):
        """
        Return `repr(self)`, a computer-readable string
        representation of this object.

        :param self: 'NearEarthObject' to call on designation and name
        attributes.
        :return: Return `repr(self)`, a computer-readable string
        representation of this object.
        """
        return (
            f"NearEarthObject(designation={self.designation!r}"
            f"name={self.name!r}, "
            f"diameter={self.diameter:.3f}, "
            f"hazardous={self.hazardous!r})"
        )


class CloseApproach:
    """A close approach to Earth by an NEO.

    A `CloseApproach` encapsulates information about the NEO's close
    approach to Earth, such as the date and time (in UTC) of closest
    approach, the nominal approach distance in astronomical units, and
    the relative approach velocity in kilometers per second.

    A `CloseApproach` also maintains a reference to its
    `NearEarthObject` - initially, this information (the NEO's primary
    designation) is saved in a private attribute, but the referenced NEO
    is eventually replaced in the `NEODatabase` constructor.
    """
    def __init__(self, time, distance, velocity, _designation, **info):
        """Create a new `CloseApproach`.

        :param designation: The primary designation for the
        `NearEarthObject` associated with this 'CloseApproach'
        :param distance: The distance from Earth at close approach.
        :parameter velocity: The velocity of the 'NearEarthObject'
        associated with this 'CloseApproach'
        :param info: A dictionary of excess keyword arguments supplied
        to the constructor.
        """
        self.time = cd_to_datetime(time)
        self.distance = float(distance)
        self.velocity = float(velocity)
        self._designation = str(_designation)
        self.neo = None

    @property
    def time_str(self):
        """Return a formatted representation of this `CloseApproach`'s
        approach time.

        The value in `self.time` should be a Python `datetime` object.
        While a `datetime` object has a string representation, the
        default representation includes seconds - significant figures
        that don't exist in our input data set.

        The `datetime_to_str` method converts a `datetime` object to a
        formatted string that can be used in human-readable
        representations and in serialization to CSV and JSON files.

        :param self: The 'CloseApproach' object, calling on the time
        attribute.
        :return: The converted time to datetime.
        """
        return datetime_to_str(self.time)

    def __str__(self):
        """
        Return a string describing the 'CloseApproach' object to be used
        when printing to terminal.

        :param self: 'CloseApproach' object to call on designation and
        name attributes.
        :return: The description of the 'CloseApproach' object by
        combining various attributes in to a human readable string
        output.
        """
        return (
            f"CloseApproach(time={self.time_str}, "
            f"distance={self.distance}, "
            f"velocity={self.velocity}, neo={self.neo})"
        )

    def __repr__(self):
        """
        Return `repr(self)`, a computer-readable string
        representation of this object.

        :param self: 'NearEarthObject' to call on designation and name
        attributes.
        :return: Return `repr(self)`, a computer-readable string
        representation of this object.
        """
        return (
            f"CloseApproach(time={self.time_str!r}, "
            f"distance={self.distance:.2f}, "
            f"velocity={self.velocity:.2f}, neo={self.neo!r})"
        )
