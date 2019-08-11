from django.conf import settings

import boto3
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class SignS3(APIView):
    """
    View responsible for generating and returning the signature with which the client-side
    JavaScript can upload the image to S3.

    The following parameters should be included as part of a URL query string.

    `file_name`: full desired path of the file inside the bucket's media folder

    `file_type`: file MIME type
    """
    permission_classes = [AllowAny]

    def get(self, request, **kwargs):
        file_name = request.query_params.get('file_name')
        file_type = request.query_params.get('file_type')

        if not file_name or not file_type:
            return Response({
                'reason': 'file_name and file_type must be provided'
            }, status=status.HTTP_400_BAD_REQUEST)

        s3 = boto3.client('s3')
        file_name = file_name.replace(' ', '_')

        presigned_post = s3.generate_presigned_post(
            Bucket=settings.AWS_STORAGE_BUCKET_NAME,
            Key=f'{settings.MEDIAFILES_LOCATION}/{file_name}',
            Fields={"acl": "public-read", "Content-Type": file_type},
            Conditions=[
                {"acl": "public-read"},
                {"Content-Type": file_type}
            ],
            ExpiresIn=300
        )

        return Response({
            'data': presigned_post,
            'url': f'https://{settings.AWS_S3_CUSTOM_DOMAIN}/'
                   f'{settings.MEDIAFILES_LOCATION}/{file_name}'
        })
