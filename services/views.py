from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.utils import timezone

from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from .models import (
    SquaresDifference,
    Triplet,
)


@api_view(["GET"])
def difference(request: Request):
    """
    /difference/ - Sum of Squares vs Squares of Sums

    Description:
        Service (Endpoint) that, given a number returns the difference between the 
        square_of_sums and the sum_of_squares of the first n natural numbers.

        Required Query Param: number

        
    JSON Payload that is Returned:
    { 
        'datetime': current_datetime,
        'value': the difference between square_of_sums and the sum_of_squares
        'number': the given number
        'occurrences' - How many times this triangle has been recalled,
        'last_datetime' - the time and date this triangle was recalled,
    }

    Error Handling:
    - A 400 is returned if there is a problem with the number query parameter

    """

    try:
        given_number = int(request.query_params.get("number"))
        not_an_int = False
    except Exception:
        not_an_int = True

    if not_an_int or given_number < 0 or given_number > 100:
        msg = ("Query parameter 'number' is required and must be an integer that is"
               " greater than or equal to 0 and less than or equal to 100!")

        return Response(msg, status=400)

    diff_data = get_object_or_404(SquaresDifference, given_number=given_number)

    current_datetime = timezone.now()
    response_data = {
        'datetime': current_datetime,
        'value': diff_data.value,
        'number': given_number,
        'occurrences': diff_data.occurrences,
        'last_datetime': diff_data.last_requested,
    }

    # Update the number of occurrences
    # and last requested timestamp
    diff_data.occurrences += 1
    diff_data.last_requested = current_datetime

    diff_data.save()
    diff_data.refresh_from_db()

    return Response(response_data)


@api_view(["GET"])
def triplet(request: Request):
    """
    /triplet/ - Pythagorean Triplet endpoint

    Description:
        Service (endpoint) that takes 3 integers (a, b and c) that represent the
        lengths of the 3 sides of a triangle and returns a flag showing whether
        or not the lengths represent a Pythagorean Triplet (a^2 + b^2 = c^2)

    QueryParams (all three required): a, b, c

    JSON Payload Returned:
    { 
        'datetime': current_datetime,
        'a', 'b', 'c' - the three sides of a triangle,
        'is_triplet' - True if a, b and c represent a Pythagorean Triplet,
        'product' - The product of a * b * c,
        'occurrences' - How many times this triangle has been recalled,
        'last_datetime' - the time and date this triangle was recalled,
    }

    Error Handling:
    - A 400 is returned if any of the a, b, or c parameters is not an integer

    """

    # Verify the request
    try:
        a = int(request.query_params.get("a"))
        b = int(request.query_params.get("b"))
        c = int(request.query_params.get("c"))
        all_ints = True
    except Exception:
        all_ints = False

    if not all_ints:
        msg = "Query parameters 'a', 'b' and 'c' are required and must be integers"
        return Response(msg, status=400)

    triplet = Triplet.get_or_create(a, b, c)

    current_datetime = timezone.now()
    response_data = {
        'datetime': current_datetime,
        'a': triplet.a,
        'b': triplet.b,
        'c': triplet.c,
        'is_triplet': triplet.is_triplet,
        'product': triplet.product,
        'occurrences': triplet.occurrences,
        'last_datetime': triplet.last_requested,
    }

    return Response(response_data)
