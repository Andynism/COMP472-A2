import os

with os.scandir('output50/') as entries:
    astarH1Sol = 0
    astarH1Score = 0
    astarH1Search = 0
    astarH1Time = 0
    astarH2Sol = 0
    astarH2Search = 0
    astarH2Score = 0
    astarH2Time = 0
    gbfsH1Sol = 0
    gbfsH1Score = 0
    gbfsH1Search = 0
    gbfsH1Time = 0
    gbfsH2Sol = 0
    gbfsH2Score = 0
    gbfsH2Search = 0
    gbfsH2Time = 0
    ucsSol = 0
    ucsScore = 0
    ucsSearch = 0
    ucsTime = 0

    for f in entries:
        with open(f) as line:
            lines = line.read().splitlines()
            lastLine = lines[-1]
            score = lastLine.split()[0]
            timer = lastLine.split()[1]
            if 'astar' in f.name and 'h1' in f.name and 'solution' in f.name:
                astarH1Sol = astarH1Sol + len(lines)-1
                astarH1Score = astarH1Score + int(score)
                astarH1Time = astarH1Time + float(timer)
            elif 'astar' in f.name and 'h2' in f.name and 'solution' in f.name:
                astarH2Sol = astarH2Sol + len(lines)-1
                astarH2Score = astarH2Score + int(score)
                astarH2Time = astarH2Time + float(timer)
            elif 'gbfs' in f.name and 'h1' in f.name and 'solution' in f.name:
                gbfsH1Sol = gbfsH1Sol + len(lines)-1
                gbfsH1Score = gbfsH1Score + int(score)
                gbfsH1Time = gbfsH1Time + float(timer)
            elif 'gbfs' in f.name and 'h2' in f.name and 'solution' in f.name:
                gbfsH2Sol = gbfsH2Sol + len(lines)-1
                gbfsH2Score = gbfsH2Score + int(score)
                gbfsH2Time = gbfsH2Time + float(timer)
            elif 'ucs' in f.name and 'solution' in f.name:
                ucsSol = ucsSol + len(lines)-1
                ucsScore = ucsScore + int(score)
                ucsTime = ucsTime + float(timer)
            elif 'astar' in f.name and 'h1' in f.name and 'search' in f.name:
                astarH1Search = astarH1Search + len(lines)-1
            elif 'astar' in f.name and 'h2' in f.name and 'search' in f.name:
                astarH2Search = astarH2Search + len(lines)-1
            elif 'gbfs' in f.name and 'h1' in f.name and 'search' in f.name:
                gbfsH1Search = gbfsH1Search + len(lines)-1
            elif 'gbfs' in f.name and 'h2' in f.name and 'search' in f.name:
                gbfsH2Search = gbfsH2Search + len(lines)-1
            elif 'ucs' in f.name and 'search' in f.name:
                ucsSearch = ucsSearch + len(lines)-1


print("\n****** A* h1 ************************")
print("A* h1 solution length:",astarH1Sol)
print("A* h1 avg solution length:",astarH1Sol/50)
print("A* h1 score:",astarH1Score)
print("A* h1 avg score:",astarH1Score/50)
print("A* h1 search length:",astarH1Search)
print("A* h1 avg search length:",astarH1Search/50)
print("A* h1 time:",astarH1Time)
print("A* h1 avg time:",astarH1Time/50)
print("\n****** A* h2 ************************")
print("A* h2 solution length:",astarH2Sol)
print("A* h2 avg solution length:",astarH2Sol/50)
print("A* h2 score:",astarH2Score)
print("A* h2 avg score:",astarH2Score/50)
print("A* h2 search length:",astarH2Search)
print("A* h2 avg search length:",astarH2Search/50)
print("A* h2 time:",astarH2Time)
print("A* h2 avg time:",astarH2Time/50)
print("\n****** gbfs h1 ************************")
print("gbfs h1 solution length:",gbfsH1Sol)
print("gbfs h1 avg solution length:",gbfsH1Sol/50)
print("gbfs h1 score:",gbfsH1Score)
print("gbfs h1 avg score:",gbfsH1Score/50)
print("gbfs h1 search length:",gbfsH1Search)
print("gbfs h1 avg search length:",gbfsH1Search/50)
print("gbfs h1 time:",gbfsH1Time)
print("gbfs h1 avg time:",gbfsH1Time/50)
print("\n****** gbfs h2 ************************")
print("gbfs h2 solution length:",gbfsH2Sol)
print("gbfs h2 avg solution length:",gbfsH2Sol/50)
print("gbfs h2 score:",gbfsH2Score)
print("gbfs h2 avg score:",gbfsH2Score/50)
print("gbfs h2 search length:",gbfsH2Search)
print("gbfs h2 avg search length:",gbfsH2Search/50)
print("gbfs h2 time:",gbfsH2Time)
print("gbfs h2 avg time:",gbfsH2Time/50)
print("\n****** ucs ************************")
print("ucs solution length:",ucsSol)
print("ucs avg solution length:",ucsSol/50)
print("ucs score:",ucsScore)
print("ucs avg score:",ucsScore/50)
print("ucs search length:",ucsSearch)
print("ucs avg search length:",ucsSearch/50)
print("ucs time:",ucsTime)
print("ucs avg time:",ucsTime/50)