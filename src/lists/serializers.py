from rest_framework import serializers
from lists.models import Item ,List


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ('id', 'text')


class ListSerializer(serializers.ModelSerializer):
    
    items = ItemSerializer(many=True, source='item_set')
    class Meta:
        model = List 
        fields = ('id', 'items',)
