from googleapiclient.discovery import build

my_api_key = "AIzaSyCtGCw9MJW9qEGZ2gSZCUQ-1Zw86Sx2pPs"
my_cse_id = "006167428610136932446:vshomdf1k8x"

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']

results = google_search(
    input("What do you want to search about?"), my_api_key, my_cse_id, num=int(input("how many searches?")))
for x in results:
    print(x)