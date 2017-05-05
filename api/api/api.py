from rest_framework import routers

router = routers.DefaultRouter()
## register routes here:
DocumentViewSet(viewsets.ModelViewSet):
  ...
  def create(self, request, *args, **kwargs):
        # create the model here
        class Document(models.Model):
            name = models.CharField(max_length=50)
            image = models.ImageField()


        document = Document.objects.create(self.validated_data)
        ...

        # handle the file upload:
        if 'file' in request.data:

            image = request.data['file']
            # user_profile.image.delete()
            document.file.save(image.name, image)

        else:
            error = json.dumps({
                'No image file found on request'
            })
            return response.Response(error, status=status.HTTP_200_OK)
