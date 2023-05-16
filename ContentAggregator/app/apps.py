from django.apps import AppConfig


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'

# class ContentAggregatorConfig(AppConfig):
#     name = 'ContentAggregator'
#     verbose_name = 'Content Aggregator'
