def project_decorator(func):
    def wrapper(*args, **kwargs):
        parser = func(*args, **kwargs)
        # 引数を追加
        return parser
    return wrapper