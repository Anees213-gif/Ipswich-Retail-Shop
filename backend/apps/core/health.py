from django.http import JsonResponse


def health(_):
    """
    Simple, fast health check endpoint that doesn't touch the database.
    Perfect for Railway health checks and load balancers.
    """
    return JsonResponse({"status": "ok"}, status=200)
