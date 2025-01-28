from collections import defaultdict


if __name__ == '__main__':
    # tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
    # tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    # tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
    # tickets = [["EZE","AXA"],["TIA","ANU"],["ANU","JFK"],["JFK","ANU"],["ANU","EZE"],["TIA","ANU"],["AXA","TIA"],["TIA","JFK"],["ANU","TIA"],["JFK","TIA"]]
    d = defaultdict(list)
    for [source, destination] in tickets:
        d[source].append(destination)
    # print(tickets)
    print(d)
    for keys in d.keys():
        d[keys] = sorted(d[keys])
    print(d)
    route = []
    def dfs(airport):
        while d[airport]:
            dfs(d[airport].pop(0))
        route.append(airport)

    dfs("JFK")

    print(route[::-1])