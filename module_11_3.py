def introspection_info(obj):
    info = {}
    info['type'] = type(obj)
    all_attributes = dir(obj)
    info['attributes'] = [i for i in all_attributes if not callable(getattr(obj, i))]
    info['methods'] = [i for i in all_attributes if callable(getattr(obj, i))]
    info['module'] = getattr(obj, '__module__', 'is unknown')

    return info

number_info = introspection_info(42)
print(number_info)