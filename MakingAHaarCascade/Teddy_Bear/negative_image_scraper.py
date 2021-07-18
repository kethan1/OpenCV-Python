from icrawler.builtin import BingImageCrawler

# items = [
#     'employees', 'fans', 'fire_alarm', 'handbag', 'human_faces', 'lemons',
#     'microvawes', 'oranges', 'outlet', 'ovens', 'painting', 'pancake',
#     'phones', 'pipes', 'plugs', 'pots', 'roads', 'stairs', 'strawberries',
#     'switches', 't-shirt', 'tables', 'tomatoes', 'toys', 'trees',
#     'water_bottle', 'watermelons', 'wires'
# ]

items = [
    "plants", "macbook", "iphone", "walls", "fan", "shutter", "chair", "pen", "pencil"
]

number = 100

for item in items:
    bing_crawler = BingImageCrawler(storage={'root_dir': f'Negative_Images/{item.replace(" ","_")}'})
    bing_crawler.crawl(keyword=item, filters=None, max_num=number, offset=0)
