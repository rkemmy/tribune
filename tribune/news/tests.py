from django.test import TestCase
from .models import Editor,Article,tags

# Create your tests here.
class EditorTestClass(TestCase):

    #Set up method
    def setUp(self):
        self.remmy= Editor(first_name = 'Remmy', last_name = 'Kemunto', email = 'remmy@moringaschool.com')

    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.remmy,Editor))

    # Testing Save method
    def test_save_method(self):
        self.remmy.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors)> 0)

class ArticleTestClass(TestCase):

    def setUp(self):
        #Creating a new editor and saving it
        self.remmy =Editor(first_name = 'Remmy', last_name = 'Kemunto', email = 'remmy@moringaschool.com')
        self.remmy.save_editor()

        #Creating a new tag and saving it
        self.new_tag = tags(name = 'testing')
        self.new_tag.save()

        self.new_article = Article(title = 'Test article',post = 'This is a random test post', editor = self.remmy)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()

    def test_get_news_todays(self):
        today_news = Article.today_news()
        self.assertTrue(len(today_news)>0)

    def test_get_news_by_date(self):
        test_date = '2018-04-30'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        news_by_date = Article.days_news(date)
        self.assertTrue(len(news_by_date) == 0)
