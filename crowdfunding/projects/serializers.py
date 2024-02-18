from rest_framework import serializers
from .models import Project, Pledge
from datetime import datetime

class PledgeSerializer(serializers.ModelSerializer):
    supporter = serializers.ReadOnlyField(source='supporter.id')
    class Meta:
        model = Pledge
        fields = '__all__'

class PledgeDetailSerializer(PledgeSerializer):
    pledges = PledgeSerializer(many=True, read_only =True)


class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    sum_pledges = serializers.ReadOnlyField()

    class Meta:        
        model = Project        
        fields = ('__all__')

class ProjectDetailSerializer(ProjectSerializer):
    pledges = PledgeSerializer(many=True, read_only =True)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        # Hard code test line
            # instance.description = "BLAH"
        instance.description = validated_data.get('description', instance.description)
        instance.goal = validated_data.get('goal', instance.goal)
        instance.image = validated_data.get('image', instance.image)
        instance.is_open = validated_data.get('is_open', instance.is_open)
        # Commented out original to keep original created date
            # instance.date_created = validated_data.get('date_created', instance.date_created)
        # Update the date_modified with timestamp        
        instance.date_modified = datetime.now()
        instance.date_close = validated_data.get('date_close', instance.date_close)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance

    
