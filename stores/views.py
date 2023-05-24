from .serializers import CategorySerializer, ProductSerializer, StoreSerializer, ContactSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions, status
from userapp.permissions import IsOwner
from .models import Product, Store, Contact, Category, Tag, Image
from rest_framework.decorators import api_view, parser_classes
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from PIL import Image as Image_
from io import BytesIO


class CategoryViewset(ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = [ permissions.AllowAny]
    queryset = Category.objects.all()


class ProductUpload(APIView):
    permission_classes = [ permissions.IsAuthenticated ]
    parser_classes = [ MultiPartParser, FormParser]

    def post(self, request, format=None):
        print(request.data)
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


@parser_classes(['MultiPartParser', 'FormParser'])
@api_view(['GET', 'POST'])
def products(request):
    user = request.user
    store = Store.objects.get(owner=user)
    products = store.product_set
    
    if request.method == 'GET':
        data = ProductSerializer(products, many=True).data,
        return JsonResponse(data, safe=False)
        
    elif request.method == 'POST':
        title = request.data['title']
        quantity = request.data['quantity']
        selling_price = request.data['selling_price']
        images = request.FILES.getlist('images')
        
        print(f"Images -- :  {images}\n\n FILE TYPE {type(images)}")
        [ print("Image ", image) for image in images]

        imgs = []
        for j in images:
            print("TRAVERSING IMAGES ---")
            k = Image.objects.create(image = j, title='title')
            imgs.append(k)
            print("IMAGE ADDED === ", k)
            #print(Image_.fromstring('RGBA', (512, 512), j))
        
        #imgs = [ Image.objects.create(image=Image_.frombytes('1', (32,32), i)) for i in images]

        print("NEW IMAGES : ", imgs)

        if request.data['cost_price'] != None:
            cost_price = request.data['cost_price']
        else:
            cost_price = 0
        if request.data['active'] == "true":
            active = True
        else:
            active = False

        p = Product.objects.create(title=title, quantity=quantity, selling_price=selling_price, cost_price=cost_price,
         active=active, store=store)
         
        [ p.images.add(img) for img in imgs ]
        
        return JsonResponse({"message": f"{p.__str__()} has been created"})


@api_view(['GET'])
def store(request):
    user = request.user
    store = Store.objects.get(owner=user)
    contact = Contact.objects.get(store=store)
    return JsonResponse({
        "name": store.name,
        "contact_name": contact.name,
        "email": contact.email,
        "phone": contact.phone,
        "address": contact.address,
        "international": store.international,
        "country": store.country
    })


class StoreViewset(ModelViewSet):
    serializer_class = StoreSerializer
    permission_classes = [ permissions.IsAdminUser ] #RESTRICT TO ADMIN
    queryset = Store.objects.all()

    #def get_queryset(self):
    #   return Store.objects.filter(owner=self.request.user)

class ContactViewset(ModelViewSet):
    model = ContactSerializer
    permission_classes = [ permissions.IsAdminUser, IsOwner ]