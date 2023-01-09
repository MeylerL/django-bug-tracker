from rest_framework import serializers

from bug_page.models import BugDetail

class ApiSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BugDetail
        fields = '__all__'
