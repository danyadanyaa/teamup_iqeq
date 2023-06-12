from rest_framework import serializers

from api.models import Test


class TestSerializer(serializers.ModelSerializer):
    iq_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    eq_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)

    class Meta:
        model = Test
        fields = (
            'id',
            'iq_time',
            'iq_points',
            'eq_time',
            'eq_result',
        )
        read_only_fields = (
            'iq_points',
            'eq_result',
        )

    def create(self, validated_data):
        raise serializers.ValidationError('POST method not allowed')


class IqSerializer(serializers.ModelSerializer):
    iq_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)

    class Meta:
        model = Test
        fields = (
            'id',
            'login',
            'iq_time',
            'iq_points',
        )


class EqSerializer(serializers.ModelSerializer):
    eq_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)

    class Meta:
        model = Test
        fields = (
            'id',
            'login',
            'eq_time',
            'eq_result',
        )


class ResultSerializer(serializers.ModelSerializer):
    iq_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    eq_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)

    class Meta:
        model = Test
        fields = (
            'id',
            'login',
            'iq_time',
            'iq_points',
            'eq_time',
            'eq_result',
        )
        read_only_fields = (
            'id',
            'iq_time',
            'iq_points',
            'eq_time',
            'eq_result',
        )
