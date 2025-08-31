# TODO List for Django Property Listing Caching Project

## Setup Phase
- [x] 1. Create requirements.txt with necessary packages
- [x] 2. Install required Python packages (django, django-redis, psycopg2-binary)
- [x] 3. Create docker-compose.yml with PostgreSQL and Redis services
- [x] 4. Initialize Django project named alx_backend_caching_property_listings
- [x] 5. Create the properties Django app
- [x] 6. Configure settings.py for PostgreSQL database and Redis cache backend
- [x] 7. Create Property model with specified fields in properties/models.py
- [x] 8. Run initial migrations (makemigrations completed)

## Task 1: Cache Property List View
- [x] 9. Create property_list view in properties/views.py with @cache_page(15 minutes) decorator
- [x] 10. Set up URL configurations for the property list view (properties/urls.py and main urls.py)

## Task 2: Low-Level Caching for Property Queryset
- [x] 11. Create properties/utils.py with get_all_properties() function using low-level cache (1 hour)
- [x] 12. Update property_list view to use the cached queryset function

## Task 3: Cache Invalidation Using Signals
- [x] 13. Create properties/signals.py with cache invalidation handlers for Property model changes
- [x] 14. Update properties/apps.py to import signals in ready() method
- [x] 15. Update properties/__init__.py for proper app configuration

## Task 4: Cache Metrics Analysis
- [x] 16. Add get_redis_cache_metrics() function to properties/utils.py for cache analysis

## Testing and Verification
- [ ] 17. Start Docker services (PostgreSQL and Redis)
- [ ] 18. Run Django development server and test functionality
- [ ] 19. Verify caching works correctly
- [ ] 20. Test cache invalidation on Property changes
- [ ] 21. Check cache metrics functionality
