from airport import Airport

class TestAirport(object):

    def test_has_hanger_array(self):
        airport = Airport()
        assert airport.hanger == []
        
