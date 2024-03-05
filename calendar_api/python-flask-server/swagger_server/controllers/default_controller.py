import connexion
import six

from swagger_server.models.schedule import Schedule  # noqa: E501
from swagger_server.models.schedules_switch_body import SchedulesSwitchBody  # noqa: E501
from swagger_server import util


def schedules_get():  # noqa: E501
    """Get a list of all schedules

     # noqa: E501


    :rtype: List[Schedule]
    """
    return 'do some magic!'


def schedules_guard_guard_id_get(guard_id):  # noqa: E501
    """Get schedules by guard ID

     # noqa: E501

    :param guard_id: 
    :type guard_id: str

    :rtype: List[Schedule]
    """
    return 'do some magic!'


def schedules_location_location_name_get(location_name):  # noqa: E501
    """Get schedules by location name

     # noqa: E501

    :param location_name: 
    :type location_name: str

    :rtype: List[Schedule]
    """
    return 'do some magic!'


def schedules_post(body):  # noqa: E501
    """Create a new schedule

    Creates a new schedule entry for a guard, checking for conflicts. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Schedule.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def schedules_schedule_id_delete(schedule_id):  # noqa: E501
    """Delete a schedule by ID

     # noqa: E501

    :param schedule_id: 
    :type schedule_id: str

    :rtype: None
    """
    return 'do some magic!'


def schedules_schedule_id_get(schedule_id):  # noqa: E501
    """Get a specific schedule by ID

     # noqa: E501

    :param schedule_id: 
    :type schedule_id: str

    :rtype: Schedule
    """
    return 'do some magic!'


def schedules_schedule_id_put(body, schedule_id):  # noqa: E501
    """Update a schedule by ID

    Updates an existing schedule, checking for conflicts. # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param schedule_id: 
    :type schedule_id: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = Schedule.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def schedules_switch_post(body):  # noqa: E501
    """Switch a schedule between two guards

    Allows the swapping of a specific schedule from one guard to another. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = SchedulesSwitchBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
