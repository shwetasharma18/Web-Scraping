from task1 import *
from pprint import pprint
def group_by_year(moviesYear):
    yearList = []
    for i in moviesYear:
        if i['year'] not in yearList:
            yearList.append(i['year'])
    sortedYearDic = {}
    for x in yearList:
        # print(x) 
        listOfMovies = [] 
        for y in moviesYear:
            if x == y["year"]:
                listOfMovies.append(y)
        sortedYearDic[x] = listOfMovies
    return(sortedYearDic)

pprint(group_by_year(moviesData))

