import graphene
from graphene_django.types import DjangoObjectType
from .models import NYC_data
import requests


class expdata(DjangoObjectType):
    class Meta:
        model=NYC_data

class Query(graphene.ObjectType):
    all_data=graphene.List(expdata)

    def resolve_all_data(self,info,**kwargs):
         
         #Quarry for Transfer the api data to the database
         
        # a=requests.get('https://data.cityofnewyork.us/resource/8y4t-faws.json').json()
        # for i in a:
            # ny=NYC_data()
            # ny.zip_code=i['zip_code']
            # ny.street_name=i['street_name']
            # ny.block_NO=i['block']
            # ny.Lot_No=i['gross_sqft']
            # ny.Built_Year=i['year']
            # ny.Building_class=i['bldg_class']
            # ny.Owner=i['owner']
            # ny.save()
            # print('zip code '+i['zip_code'])
            # print('Adderess: '+i['street_name']+', block NO. '+i['block']+', Lot No. '+i['gross_sqft']+', Built Year '+i['year']+ ', Building class '+i['bldg_class'] + ', Owner '+i['owner']+', State NYC' )
        return NYC_data.objects.all()

 
