from airport import Airport
import pytest

class TestAirport(object):

    def test_has_hanger_array(self):
        airport = Airport()
        assert airport.hanger == []

    def test_land_puts_plane_in_hanger(self):
        airport = Airport()
        plane = 'plane'
        airport.land(plane)
        assert plane in airport.hanger

    def test_take_off_removes_from_hanger(self):
        airport = Airport()
        plane = 'plane'
        airport.take_off(plane, 'sunny')
        assert plane not in airport.hanger

    def test_does_not_take_off_when_stormy(self):
        airport = Airport()
        plane = 'plane'
        with pytest.raises(RuntimeError):
            airport.take_off(plane, 'stormy')
