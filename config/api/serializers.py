from rest_framework import serializers

class TransactionSerializer(serializers.Serializer):
    description = serializers.CharField()
    vendor = serializers.CharField(required=False, allow_blank=True)
    company_id = serializers.CharField()
    industry = serializers.CharField()
    chart_of_accounts = serializers.ListField(child=serializers.CharField())
    historical_transactions = serializers.ListField()