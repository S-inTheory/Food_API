import requests
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


def get_data():
    response = requests.get('https://stepik.org/media/attachments/course/73594/foodboxes.json')
    if not response:
        return
    data_json = response.json()
    return data_json


def get_recipients():
    response = requests.get('https://stepik.org/media/attachments/course/73594/recipients.json')
    data_json = response.json()
    return data_json


@api_view(http_method_names=['GET'])
def recipients_list(request):
    response = get_recipients()
    if response:
        return Response(response)
    else:
        return Response(status=status.HTTP_408_REQUEST_TIMEOUT)


@api_view(http_method_names=['GET'])
def recipient_detail(request, id):
    response = None

    for recipient in get_recipients():
        print(recipient['id'])
        if recipient['id'] == int(id):
            response = recipient

    if response:
        return Response(response)
    else:
        return Response(status=status.HTTP_408_REQUEST_TIMEOUT)


@api_view(http_method_names=['GET'])
def data_list(request):
    result = []
    if request.query_params:
        min_price = request.query_params.get('min_price')
        min_weight = request.query_params.get('min_weight')

        for data in get_data():
            if min_price:
                if data['price'] >= int(min_price):
                    result.append(data)
            elif min_weight:
                if data['weight_grams'] >= int(min_weight):
                    result.append(data)

    else:
        result = get_data()
    if result:
        return Response(result)
    else:
        return Response(status=status.HTTP_408_REQUEST_TIMEOUT)


@api_view(http_method_names=['GET'])
def data_detail(request, id):
    response = None
    for data in get_data():
        if data['inner_id'] == int(id):
            response = data

    if response:
        return Response(response)
    else:
        return Response(status=status.HTTP_408_REQUEST_TIMEOUT)
