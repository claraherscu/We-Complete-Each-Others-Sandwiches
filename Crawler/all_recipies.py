import scrapy
import time
import json

class RecipeSpider(scrapy.Spider):
    num_of_iteration = 50
    name = "Recipes"
    start_urls = []

    file = open('C:\\Users\\Daniel\\PycharmProjects\\scrapy\\allrecipies\\links.json')
    list = json.load(file)
    file.close()

    for dict in list:
        for link in dict['links']:
            if 'recipe/' in link:
                start_urls.append(link)

    start_urls = start_urls[0:10]
    visited_urls = []

    def parse(self, response):

        # get the url of the cd:
        url = response.url
        self.visited_urls.append(url)


        # get the recipe name:
        recipe_name = response.css('h1::text').extract_first()


        recipe_rating = 0
        recipe_review_count = 0
        recipe_image_link = ''

        # get the rating and review count:
        sections = response.css('section')
        for section in sections:
            if 'recipe-summary' in section.css('::attr(class)').extract_first():
                for div in section.css('div'):
                    if div.css('::attr(class)').extract_first() == 'rating-stars':
                        recipe_rating = float(div.css('::attr(data-ratingstars)').extract_first())
                    elif div.css('::attr(class)').extract_first() == 'summary-stats-box':
                        for span in div.css('span'):
                            if span.css('::attr(class)').extract_first() == 'review-count':
                                recipe_review_count = int(span.css('::text').extract_first().split()[0])

        # get the picture:
        photos = response.css('img')
        for photo in photos:
            if photo.css('::attr(class)').extract_first() == 'rec-photo':
                recipe_image_link = photo.css('::attr(src)').extract_first()

        # get the ingredients:
        recipe_ingredient_list = []
        for ul in response.css('ul'):
            if ul.css('::attr(class)').extract_first() is not None and \
                'checklist dropdownwrapper list-ingredients' in ul.css('::attr(class)').extract_first():
                for span in ul.css('span'):
                    if span.css('::attr(class)').extract_first() is not None and \
                                    span.css('::attr(class)').extract_first() == 'recipe-ingred_txt added':
                        recipe_ingredient_list.append(span.css('::text').extract_first())

        # get the categories:
        categories = []
        uls = response.css('ul')
        lis = None
        for ul in uls:
            if (ul.css('::attr(class)')):
                if ('breadcrumbs' in ul.css('::attr(class)').extract_first()):
                    lis = ul
        if (lis):
            for li in lis.css('li'):
                categories.append(li.css('a').css('span').css('::text').extract_first().strip())


        # send the data to the json!
        yield {
            'url':url,
            'recipe_name':recipe_name,
            'recipe_rating':recipe_rating,
            'recipe_review_count':recipe_review_count,
            'recipe_image_link':recipe_image_link,
            'recipe_ingredient_list':recipe_ingredient_list,
            'categories':categories,
        }


        # get all the links of the recipes:
        links = []
        for ul in response.css('ul'):
            if ul.css('::attr(class)').extract_first() == 'recipe-carousel':
                for item in ul.css('li'):
                    if item.css('::attr(class)').extract_first() == 'slider-card':
                        link = item.css('a')
                        if response.urljoin(link.css('::attr(href)').extract_first()) not in self.visited_urls:
                            links.append(response.urljoin(link.css('::attr(href)').extract_first()))

        time.sleep(0.3)
        if len(links) > 0:
            for link in links:
                yield scrapy.Request(link, callback=self.parse)