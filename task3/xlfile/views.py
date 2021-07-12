# python import
import pandas as pd
import os

# django import
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

# rest framework import
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.

main_path = default_storage.location

class FileUpload(APIView):
    # parser_classes = [JSONParser]

    def post(self,request):
        
        try:
            xlfile = request.data['xlfile']
        except:
            return Response(
                status=status.HTTP_200_OK,
                data={
                    'error' : 'something went wrong'
                }
            )
        contenttype = xlfile.content_type
        if xlfile.name.endswith('.xlsx') and contenttype == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
            path = default_storage.save('xlfile.xlsx',ContentFile(xlfile.read()))
            df = pd.read_excel('{}\{}'.format(main_path,path))
            data = df['ABC'].value_counts().to_json()
            os.remove('{}\{}'.format(main_path,path))
            return Response(
                status=status.HTTP_200_OK,
                data=data
            )
        else:
            return Response(
                status=status.HTTP_200_OK,
                data={
                    'error' : 'file must be .xlsx format'
                }
            )
