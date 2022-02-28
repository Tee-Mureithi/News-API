import unittest

from Models import news

News = news.News

class ArticleTest(unittest.TestCase):

    '''

    Test Class to test the behaviour of the movie 
    
    '''

    def setUp(self):

        '''
        Setup method that will run before every Test
        '''
        self.new_news = News()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))

if __name__ == '__main__' :

    unittest.main()