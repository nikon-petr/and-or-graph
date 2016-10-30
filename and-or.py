import json, sys


def load_file():
    file = open('graph.json', 'r')
    with file:
        jdict = json.load(file)
        l = [ list(i.keys())[0] for i in jdict['vertices'] ]
        d = { list(v.keys())[0]: list(v.values())[0] for v in jdict['vertices'] }
    return l, d

class Graph:
    def __init__(self):
        self.list, self.dict = load_file()

    def __colculate_and_ref(self, ref):
        refs = ref.split('&')
        p = 1
        for i in refs:
            if float(self.dict[i]['p']) < p:
                p = float(self.dict[i]['p'])
        return p

    def __colculate_or_ref(self, key, p=None, ref_n=1):
        if p == None:
            k = self.dict[key]['weights'][ref_n-1]
            if self.dict.get(self.dict[key]['ref'][ref_n-1]) != None :
                p = self.dict[self.dict[key]['ref'][ref_n-1]]['p']
            else:
                p = self.__colculate_and_ref(self.dict[key]['ref'][ref_n-1])
        else:
            k = 1

        if len(self.dict[key]['weights']) == ref_n:
            return p
        elif len(self.dict[key]['weights']) == 1:
            return p * k
        k2 = self.dict[key]['weights'][ref_n]

        if self.dict.get(self.dict[key]['ref'][ref_n]) != None:
            p2 = self.dict[self.dict[key]['ref'][ref_n]]['p']
        else:
            p2 = self.__colculate_and_ref(self.dict[key]['ref'][ref_n])

        p = p * k + p2 * k2 - k * p * k2 * p2
        return self.__colculate_or_ref(key, p, ref_n+1)

    def __colculate_vertex(self, key):
        return self.__colculate_or_ref(key)

    def __pretty_print(self, l):
        l = sorted(l, key=lambda item: item[1], reverse=True)
        for i in l:
            print('%.2f : %s' % (i[1], i[0]))
        print()

    def __get_output(self):
        d = {}
        for i in self.list:
            if self.dict[i].get('output') == True:
                d[i] = float(self.dict[i]['p'])
        return list(d.items())

    def start_colculate(self):
        for v in self.list:
            if self.dict[v]['p'] == None:
                self.dict[v]['p'] = self.__colculate_vertex(v)
        self.__pretty_print(self.__get_output())

if __name__ == '__main__':
    graph = Graph()
    graph.start_colculate()
