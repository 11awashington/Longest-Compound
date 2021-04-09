import urllib.request as request


class FindLCW:
    def __init__(self, url):
        self.array = self.get_text(url)
        self.combination = []

    def get_text(self, url): # grabs words from url
        web_page = request.urlopen(url)
        html = web_page.read()
        text = html.decode("utf-8")
        return sorted(text.split('\n'), key=len, reverse=True)

    def check_combination(self, i): # checks the combinations
        word = self.array[i]
        unique_array = [x for x in self.array if x != word]
        for item in unique_array:
            word = word.replace(item, '')
            if len(word) == 0: return True
        return False

    def get_combinations(self): # combination break down
        out = []
        item = list(map(lambda i: self.check_combination(i), range(0, len(self.array))))
        out = [self.array[x] for x in range(0, len(self.array)) if item[x]]
        return out

    def get_longest_compound(self):
        compounds = self.get_combinations()
        if compounds == []:
            print('Not Found')
        else:
            print(f'The longest combination is:  {max(compounds, key=len)}')


url = "https://gist.githubusercontent.com/bobbae/4ca309a1857158d5766d4ede4235cae0/raw/77d5e62835c80d30b87ab7f4a84a63a4a64f7cb2/words.txt"

FindLCW(url).get_longest_compound()
