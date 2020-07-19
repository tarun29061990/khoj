from ..models import Location


class LocationSearchService:

    def get_locations(self, term, order_by=None, limit=None):

        order_by = order_by or "-popularity"
        if term:
            if limit:
                location_list = Location.objects.filter(display_name__istartswith=term).order_by(order_by)[:int(limit)]
            else:
                location_list = Location.objects.filter(display_name__istartswith=term).order_by(order_by)

            locations = location_list.all()
            response = []
            for location in locations:
                response.append({'id':location.id, 'name': location.name, 'display_name': location.display_name,'popularity': location.popularity})

            return {"data": response, "code":200}
        else:
            return {"data": "", "code": 400, "error": "Invalid Request!! Query Parameter term should have some value"}
