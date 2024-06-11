# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.schedule import Schedule  # noqa: E501
from swagger_server.models.schedules_switch_body import SchedulesSwitchBody  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_schedules_get(self):
        """Test case for schedules_get

        Get a list of all schedules
        """
        response = self.client.open(
            '/GJSCRAVEIRO/Calendar/1.0.0/schedules',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_schedules_guard_guard_id_get(self):
        """Test case for schedules_guard_guard_id_get

        Get schedules by guard ID
        """
        response = self.client.open(
            '/GJSCRAVEIRO/Calendar/1.0.0/schedules/guard/{guardId}'.format(guard_id='guard_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_schedules_location_location_name_get(self):
        """Test case for schedules_location_location_name_get

        Get schedules by location name
        """
        response = self.client.open(
            '/GJSCRAVEIRO/Calendar/1.0.0/schedules/location/{locationName}'.format(location_name='location_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_schedules_post(self):
        """Test case for schedules_post

        Create a new schedule
        """
        body = Schedule()
        response = self.client.open(
            '/GJSCRAVEIRO/Calendar/1.0.0/schedules',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_schedules_schedule_id_delete(self):
        """Test case for schedules_schedule_id_delete

        Delete a schedule by ID
        """
        response = self.client.open(
            '/GJSCRAVEIRO/Calendar/1.0.0/schedules/{scheduleId}'.format(schedule_id='schedule_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_schedules_schedule_id_get(self):
        """Test case for schedules_schedule_id_get

        Get a specific schedule by ID
        """
        response = self.client.open(
            '/GJSCRAVEIRO/Calendar/1.0.0/schedules/{scheduleId}'.format(schedule_id='schedule_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_schedules_schedule_id_put(self):
        """Test case for schedules_schedule_id_put

        Update a schedule by ID
        """
        body = Schedule()
        response = self.client.open(
            '/GJSCRAVEIRO/Calendar/1.0.0/schedules/{scheduleId}'.format(schedule_id='schedule_id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_schedules_switch_post(self):
        """Test case for schedules_switch_post

        Switch a schedule between two guards
        """
        body = SchedulesSwitchBody()
        response = self.client.open(
            '/GJSCRAVEIRO/Calendar/1.0.0/schedules/switch',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
