import scrapy


class AdventMoviesSpider(scrapy.Spider):
    name = 'advent_movies'
    allowed_domains = ['https://www.imdb.com/search/title/?genres=adventure&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=5aab685f-35eb-40f3-95f7-c53f09d542c3&pf_rd_r=CSWWAVEY2T8GC1RVR6CM&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_2']
    start_urls = ['http://www.imdb.com/search/title/?genres=adventure&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=5aab685f-35eb-40f3-95f7-c53f09d542c3&pf_rd_r=CSWWAVEY2T8GC1RVR6CM&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_2/']

    def parse(self, response):
        movies=response.xpath("//div[@class='lister-item mode-advanced']")
        for movie in movies:
            name=movie.xpath(".//div[@class='lister-item-content']/h3/a/text()").get()
            rating=movie.xpath(".//div[@class='lister-item-content']/div/div/strong/text()").get()
            #duration=movie.xapth(".//div[@class='lister-item-content']/p[@class='text-muted ']/span[@class='runtime']/text()").get()
            description=movie.xpath("normalize-space(.//div[@class='lister-item-content']/p[@class='text-muted']/text())").get()

            yield{
            'name':name,
            'rating':rating,
            #'duration':duration,
            'Synopsis':description
            }
