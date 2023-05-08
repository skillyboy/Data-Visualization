from django.db import models
from datetime import datetime

class DataIndustry(models.Model):
    end_year = models.CharField(max_length=4, blank=True)
    intensity = models.IntegerField()
    sector = models.CharField(max_length=255)
    topic = models.CharField(max_length=255)
    insight = models.TextField()
    url = models.URLField()
    region = models.CharField(max_length=255, blank=True)
    start_year = models.CharField(max_length=4, blank=True)
    impact = models.CharField(max_length=255, blank=True)
    add_date = models.DateTimeField()
    publish_date = models.DateTimeField()
    country = models.CharField(max_length=255, blank=True)
    relevance = models.IntegerField()
    pestle = models.CharField(max_length=255)
    source = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    likelihood = models.IntegerField()
    
    class Meta:
        db_table = 'data'
        managed = True
        verbose_name = 'data'
        verbose_name_plural = 'datum'

    def __str__(self) -> str:
        title = self.title
        return title[:50]

    def _get_year(self):
        return str(self.published_date.year)
    
    

    # @classmethod
    # def parse(cls, data):
    #     parsed_data = {}
    #     parsed_data['end_year'] = data.get('end_year', '')
    #     parsed_data['intensity'] = data['intensity']
    #     parsed_data['sector'] = data['sector']
    #     parsed_data['topic'] = data['topic']
    #     parsed_data['insight'] = data['insight']
    #     parsed_data['url'] = data['url']
    #     parsed_data['region'] = data.get('region', '')
    #     parsed_data['start_year'] = data.get('start_year', '')
    #     parsed_data['impact'] = data.get('impact', '')
    #     parsed_data['added'] = datetime.strptime(data['added'], '%B, %d %Y %H:%M:%S')
    #     parsed_data['published'] = datetime.strptime(data['published'], '%B, %d %Y %H:%M:%S')
    #     parsed_data['country'] = data.get('country', '')
    #     parsed_data['relevance'] = data['relevance']
    #     parsed_data['pestle'] = data['pestle']
    #     parsed_data['source'] = data['source']
    #     parsed_data['title'] = data['title']
    #     parsed_data['likelihood'] = data['likelihood']
    #     return parsed_data
    

