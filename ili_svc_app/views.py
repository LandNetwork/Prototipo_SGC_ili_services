import tempfile
import os
import mimetypes

from rest_framework.request import HttpRequest
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.permissions import AllowAny
from rest_framework.parsers import MultiPartParser, FormParser
from django.http import FileResponse

from ili_svc_app.submodules.iliservices.core.ili2db import Ili2DB
from ili_svc_app.submodules.iliservices.db.pg_factory import PGFactory
from ili_svc_app.config.general_config import FORMATS_SUPPORTED, DB_SCHEMA

# Create your views here.

@api_view(['GET'])
@permission_classes([AllowAny])
def get_file(request: HttpRequest, pk: str):
    ili2db = Ili2DB()
    pg_factory = PGFactory()
    schema_name = DB_SCHEMA
    pg_params = {'schema': schema_name}
    db = pg_factory.get_db_connector(pg_params)
    # Export data
    xtf_export_path = tempfile.mktemp() + '.xtf'
    baskets = [pk]
    configuration = ili2db.get_export_configuration(db, xtf_export_path,'',baskets)
    res_export, msg_export = ili2db.export(db, configuration)
    print(res_export, msg_export)

    if os.path.exists(xtf_export_path):
        response = FileResponse(open(xtf_export_path, 'rb'), as_attachment=True)
        return response

    return Response(
        {"message": f"El basket ({pk}) no existe en la base de datos, valide e intente nuevamente!."},
        status.HTTP_404_NOT_FOUND
    )

@api_view(['POST'])
@permission_classes([AllowAny])
@parser_classes([MultiPartParser, FormParser])
def upload_file(request: HttpRequest):
    file = request.FILES.get('file')
    if not file:
        return Response(
            {"message": "No se ha encontrado un archivo en la solicitud."},
            status.HTTP_400_BAD_REQUEST
        )
    
    if mimetypes.types_map.get('.xtf') != 'application/xtf':
        # Agregar el nuevo tipo MIME
        mimetypes.add_type('application/xtf', '.xtf')
    content_type = mimetypes.guess_type(file.name)[0]
    if content_type not in FORMATS_SUPPORTED:
        return Response(
            {"message": f"El archivo ({file.name}) con el tipo de formato ({content_type}) no es soportado."},
            status.HTTP_400_BAD_REQUEST
        )
    
    ili2db = Ili2DB()
    pg_factory = PGFactory()
    schema_name = DB_SCHEMA
    pg_params = {'schema': schema_name}
    db = pg_factory.get_db_connector(pg_params)
    # Update data
    xtf_update_data_path = tempfile.mktemp() + '.xtf'
    with open(xtf_update_data_path, 'wb') as f:
        for chunk in file.chunks():
            f.write(chunk)
    
    configuration = ili2db.get_update_configuration(db, xtf_update_data_path, '')
    res_update, msg_update = ili2db.update(db, configuration)
    print(res_update, msg_update)

    if res_update:
        return Response({"message": msg_update}, status.HTTP_200_OK)
    else:
        return Response({"message": msg_update}, status.HTTP_400_BAD_REQUEST)
    
