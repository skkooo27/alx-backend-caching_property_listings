import logging
from django.core.cache import cache
from django_redis import get_redis_connection
from .models import Property

logger = logging.getLogger(__name__)

def get_all_properties():
    properties = cache.get('all_properties')
    if properties is None:
        properties = list(Property.objects.all().values())
        cache.set('all_properties', properties, 3600)
    return properties

def get_redis_cache_metrics():
    redis_conn = get_redis_connection('default')
    info = redis_conn.info()
    hits = info.get('keyspace_hits', 0)
    misses = info.get('keyspace_misses', 0)
    total_requests = hits + misses
    hit_ratio = (hits / total_requests) * 100 if total_requests > 0 else 0
    metrics = {
        'hits': hits,
        'misses': misses,
        'hit_ratio': hit_ratio
    }
    logger.error(f"Cache metrics: {metrics}")
    return metrics
