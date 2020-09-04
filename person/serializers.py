from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


from general.constants import Gender
from .constants import Type
from .models import Person


class PersonSerializer(serializers.ModelSerializer):

    birth_date = serializers.DateField(source='person.birth_date')
    gender = serializers.ChoiceField(source='person.gender', choices=Gender.GENDER_CHOICES, default=Gender.MALE)
    type = serializers.ChoiceField(source='person.type', choices=Type.TYPE_CHOICES, default=Type.VISITOR)

    password = serializers.CharField(
        write_only=True,
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'birth_date', 'gender', 'type']

    def create(self, validated_data):
        person_data = validated_data.pop('person')
        """
        Needed in order to assign the username from Person to the User Model
        # validated_data['username'] = person_data['username']
        """
        validated_data['password'] = make_password(validated_data['password'])

        user = User.objects.create(**validated_data)
        Person.objects.create(user=user, **person_data)

        return user

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data.get('password'))

            instance.password = validated_data.get('password', instance.password)

        if 'username' in validated_data:

            instance.username = validated_data.get('username', instance.username)

        """
        fields = instance._meta.fields
        exclude = []
        for field in fields:

            field = field.name.split('.')[-1]  # to get coulmn name
            if field in exclude:
                continue
            exec("instance.%s = validated_data.get(field, instance.%s)" % (field, field))
        """

        instance.save()
        return instance
