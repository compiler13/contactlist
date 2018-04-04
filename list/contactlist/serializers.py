from rest_framework import serializers
from contactlist.models import(Contact)

class ContactSerializers(serializers.ModelSerializer):
    

    class Meta:
        model = Contact
        fields = (
            'id',
            'name',
            'phone',
            'email',
            'profession',
        )


class ContactBasicSerializers(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = (
            'name',
            'phone',
            'email',
            'profession',
        )