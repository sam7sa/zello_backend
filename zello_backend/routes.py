def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('blog', '/blog/{id:\d+}/{slug}')
    config.add_route('blog_action', '/blog/{action}')
    config.add_route('auth', '/sign/{action}')
    config.add_route('sellings_json', '/sellings')
    config.add_route('sellings_json_', '/sellings/')
    config.add_route('selling_json', '/sellings/{selling_id}')
