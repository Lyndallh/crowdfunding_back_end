from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:        
        model = CustomUser        
        fields ='__all__' 
        extra_kwargs = {'password': {'write_only': True}}

    # def create(self, validated_data):
            # user = CustomUser.objects.create(
            #     first_name = validated_data['first_name'],
            #     last_name = validated_data['last_name'],
            #     username = validated_data['username'],
            #     email = validated_data['email']
            # )
            # user.set_password(validated_data['password'])
            # user.save()
            # return user
        
    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)

# 
# class CustomUserDetailSerializer(CustomUserSerializer):
    
#     def update(self, instance, validated_data):
#         instance.username = validated_data.get('username', instance.username)
#         instance.first_name = validated_data.get('first_name', instance.first_name)
#         instance.last_name = validated_data.get('last_name', instance.last_name)
#         instance.email = validated_data.get('email', instance.email)
#         return instance
        
# This serializer looks a lot like our others, 
# but there's a couple of things going on herethat are unique to users!
# The extra_kwargs
        # We are passing an extra-piece of meta-information to our serializer.
        # Up until now, all our serializers have just been naively looking at our model andfiguring 
        # out for themselves how to serialize every field they find there. Passwords arespecial, 
        # though - we don't want our serializer to show our password to anyone!For this reason we tell 
        # the serializer that we have an extra "keyword argument" for thepassword field. This is an extra 
        # piece of info about how this field should be serialized.Specifically, it is write_only!The serializer 
        # will send it to the model when a new user is created, but will neverbounce it back to the user.
        # The create MethodFor any other model, the built-in create method that comes with all ModelSerializersubclasses
        # would be just fine. But once again, passwords require special treatment.
        # When we save a password in the database, we don't want to just save it as "plain text".If we did that, and somebody got unauthorised access to our data, they'd be able toread off all the passwords and break into every single user's account.Instead, what we save to the database is called a "hash". It's an encrypted version ofthe password.When a user goes to log in to their existing account, they supply their password. Wehash the password again, and then compare the new hash to the hash we saved in thedatabase when they created their account. If they match, we log the user in.Hashes are useful for this purpose, because it's easy to create a hash from a password,but very difficult to work backwards to find the password if all you have is the hash.That makes them much more secure for storing passwords.
