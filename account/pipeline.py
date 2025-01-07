# account/pipeline.py

def ensure_uid(backend, details, response, *args, **kwargs):
    """
    Ensures that the 'uid' is available in the pipeline.
    """
    if 'uid' not in kwargs:
        # 'id' is usually the unique identifier from Facebook's response
        kwargs['uid'] = response.get('id')
    return kwargs
