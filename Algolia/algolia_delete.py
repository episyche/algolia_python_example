from algoliasearch.search_client import SearchClient

# replace with your ApplicationID and AdminAPIkey
client = SearchClient.create("XGTG0EJUW8", "edeaeabac36ba6570e7cb703bb658l")
index = client.init_index('first_index')

index.delete_object(1)
