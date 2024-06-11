import httpcore

def setup_http2_pool():
    return httpcore.ConnectionPool(http1=False, http2=True)
