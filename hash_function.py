
cache = {}
def get_page(url): 
    if cache.get(url):
        return cache[url]  # Returns cached data
    else: 
        data = get_data_from_server(url)
        cache[url] = data   # Saves this data in your cache first 
        return data


