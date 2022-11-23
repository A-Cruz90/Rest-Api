from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET','PUT','POST','DELETE'])
def product_list(request):


    return Response('Bet')