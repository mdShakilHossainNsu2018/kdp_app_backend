from PyDictionary import PyDictionary
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

dictionary = PyDictionary()


# print(dictionary.meaning("indentation"))
# print(dictionary.synonym("Life"))
# print(dictionary.antonym("Life"))

@api_view(['GET'])
@renderer_classes([JSONRenderer])
def hello_world(request):
    if request.method == 'GET':
        query = request.query_params.get('q')
        # meaning = dictionary.meaning(query)
        # print(meaning)
        synonym = dictionary.synonym(query)
        print(synonym)
        antonym = dictionary.antonym(query)
        print(antonym)
        return Response(
            {"message": "Request successful...",
             "data": {'word': query, 'synonym': synonym, 'antonym': antonym}})
    return Response({"message": "Something wrong."}, status=status.HTTP_200_OK)
