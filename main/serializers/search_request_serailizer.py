from ..utils.api_filters import ApiFilters


class SearchSerializer:

    @staticmethod
    def validate(request):
        term = request.GET.get('term')
        count = request.GET.get('count')
        filters = ApiFilters(request.GET.get('filters'))
        order_by = filters.get('order_by')

        try:
            if not isinstance(term, str):
                return False

            if not isinstance(int(count), int):
                return False

            if order_by and not isinstance(order_by, str):
                return False

        except Exception as e:

            return False

        return True
