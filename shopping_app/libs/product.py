from  data.search import binary_search


products=["Mobile","Book","Laptop"]

def list_products():
    return products;


def search_products(item):
    return binary_search(products,item)